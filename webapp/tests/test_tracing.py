"""Exercise the real tracing and Anthropic SDKs without contacting either service."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


class TracingTests(unittest.TestCase):
    def test_optional_tracing_and_real_sdk_observations(self):
        # Each configuration needs a fresh process: SDK instrumentation is global.
        for mode in ['missing-keys', 'disabled', 'enabled']:
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as temp:
                result = subprocess.run(
                    [sys.executable, '-m', 'webapp.tests.test_tracing', mode],
                    cwd=Path(__file__).resolve().parents[2],
                    env={**os.environ, 'DATABASE_PATH': str(Path(temp) / 'test.sqlite'),
                         'ANTHROPIC_API_KEY': 'test-anthropic-key',
                         'LANGFUSE_PUBLIC_KEY': '' if mode == 'missing-keys' else 'pk-lf-test',
                         'LANGFUSE_SECRET_KEY': 'sk-lf-test',
                         'LANGFUSE_TRACING_ENABLED': 'false' if mode == 'disabled' else 'true',
                         'LANGFUSE_MEDIA_UPLOAD_ENABLED': 'false',
                         'LANGFUSE_SAMPLE_RATE': '1', 'OTEL_SDK_DISABLED': 'false'},
                    capture_output=True, text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


def check(mode):
    if mode != 'enabled':
        with patch('langfuse.get_client') as get_client, patch(
                'opentelemetry.instrumentation.anthropic.AnthropicInstrumentor.instrument') as instrument:
            from webapp import tracing
            assert tracing.langfuse is None
            assert not get_client.called and not instrument.called
            assert tracing.observe(name='disabled')(lambda: 42)() == 42
        return

    import anthropic
    import httpx2
    from fastapi.testclient import TestClient
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor, SpanExportResult
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter

    exporter = InMemorySpanExporter()
    provider = TracerProvider()
    provider.add_span_processor(SimpleSpanProcessor(exporter))
    trace.set_tracer_provider(provider)
    real_claude = anthropic.AsyncAnthropic
    fail_provider = False

    def respond(request):
        if fail_provider:
            return httpx2.Response(500, json={'type': 'error', 'error': {'type': 'api_error', 'message': 'Test error'}})
        payload = json.loads(request.content)
        tool = payload['tool_choice'].get('name')
        if tool == 'search_guides':
            content = [{'type': 'tool_use', 'id': 'search1', 'name': tool, 'input': {'query': 'rental deposit'}}]
        elif tool == 'select_blocks':
            content = [{'type': 'tool_use', 'id': 'select1', 'name': tool,
                        'input': {'blocks': ['bank'], 'citizenship': 'italian', 'stage': 'here'}}]
        elif tool == 'build_student_plan':
            context = json.loads(payload['messages'][0]['content'])
            output = dict(title='Your student plan', subtitle='Check the public service guidance',
                          rationale='Verify the documents and next actions with the relevant service.',
                          block_order=[b['id'] for b in context['services']],
                          steps=[dict(id=s['id'], title=s['title'], body='Check this step with the public service linked in the guide.',
                                      why='Follow the required service steps.', checklist=['I checked the service guidance'],
                                      source_ids=[context['sources'][0]['id']]) for s in context['required_steps_this_batch']])
            content = [{'type': 'tool_use', 'id': 'plan1', 'name': tool, 'input': output}]
        else:
            content = [{'type': 'text', 'text': 'Check the rental guide for deposit details.'}]
        return httpx2.Response(200, json={'id': 'msg_test', 'type': 'message', 'role': 'assistant',
            'model': payload['model'], 'content': content, 'stop_reason': 'tool_use' if tool else 'end_turn',
            'stop_sequence': None, 'usage': {'input_tokens': 100, 'output_tokens': 20}})

    def claude(**options):
        return real_claude(**{**options, 'max_retries': 0},
                          http_client=httpx2.AsyncClient(transport=httpx2.MockTransport(respond)))

    # Simulate an unavailable Langfuse exporter; application requests must still succeed.
    with patch('opentelemetry.exporter.otlp.proto.http.trace_exporter.OTLPSpanExporter.export',
               return_value=SpanExportResult.FAILURE):
        from webapp import main, tracing
        assert tracing.langfuse is not None
        with patch.object(main.anthropic, 'AsyncAnthropic', claude), patch.object(
                tracing.langfuse, 'flush', wraps=tracing.langfuse.flush) as flush:
            with TestClient(main.app) as client:
                chat = {'messages': [{'role': 'user', 'content': 'Explain the deposit'}]}
                response = client.post('/api/chat', json=chat)
                assert response.status_code == 200, response.text
                assert response.json()['usage']['model_calls'] == 2
                response = client.post('/api/plan/suggest', json={'story': 'I need a student bank account.'})
                assert response.status_code == 200, response.text
                response = client.post('/api/plan/generate', json={'blocks': ['bank'], 'profile': {
                    'language': 'en', 'citizenship': 'italian', 'citizenship_confirmed': True,
                    'stage': 'here', 'stay_duration': 'year-plus', 'taxcode': 'yes'}})
                assert response.status_code == 200, response.text
                fail_provider = True
                assert client.post('/api/chat', json=chat).status_code == 502
            assert flush.call_count == 1
        tracing.langfuse.shutdown()

    spans = exporter.get_finished_spans()
    roots = [s for s in spans if s.name.startswith('studiami.')]
    assert len(roots) == 4
    assert len({s.context.trace_id for s in roots}) == 4
    generations = [s for s in spans if s.name == 'anthropic.chat']
    assert len(generations) == 5
    successful = [s for s in generations if s.status.status_code.name != 'ERROR']
    assert len(successful) == 4
    for span in successful:
        assert span.attributes['gen_ai.usage.input_tokens'] == 100
        assert span.attributes['gen_ai.usage.output_tokens'] == 20
        assert span.attributes['gen_ai.response.model']
        assert any('prompt' in key or 'input.messages' in key for key in span.attributes)
        assert any('completion' in key or 'output.messages' in key for key in span.attributes)
        assert span.parent.span_id in {r.context.span_id for r in roots}
    assert any(s.name == 'search-guides' and s.context.trace_id == roots[0].context.trace_id for s in spans)
    assert any(s.name == 'read-guide' for s in spans)
    assert any(s.status.status_code.name == 'ERROR' for s in generations)
    assert not any('test-anthropic-key' in str(s.attributes) or 'sk-lf-test' in str(s.attributes) for s in spans)


if __name__ == '__main__':
    check(sys.argv[1])
