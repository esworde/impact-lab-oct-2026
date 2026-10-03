import asyncio
import json
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from webapp.journeys import localized
from webapp.knowledge import Knowledge
from webapp import main


class KnowledgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.k = Knowledge(Path(self.temp.name) / 'test.sqlite')

    def tearDown(self):
        self.temp.cleanup()

    def page(self, body):
        return {'url': 'https://example.com/guide', 'title': 'Student guide',
                'markdown': '# Student guide\n\n' + body * 20, 'provider': 'test'}

    def test_refresh_replaces_search_and_preserves_old_version(self):
        self.k.upsert(self.page('A rental deposit is explained here. '))
        self.assertTrue(self.k.retrieve('deposit'))
        self.k.upsert(self.page('Public transportation is explained here. '))
        self.assertFalse(self.k.retrieve('deposit'))
        self.assertTrue(self.k.retrieve('transportation'))
        with self.k.connect() as db:
            self.assertEqual(db.execute('SELECT count(*) FROM versions').fetchone()[0], 1)

    def test_unchanged_refresh_does_not_duplicate_sections(self):
        page = self.page('Student housing and contracts. ')
        self.k.upsert(page)
        count = self.k.stats()['sections']
        self.k.upsert(page)
        self.assertEqual(self.k.stats()['sections'], count)
        with self.k.connect() as db:
            self.assertEqual(db.execute('SELECT count(*) FROM versions').fetchone()[0], 0)
        self.k.retrieve('" OR * : ; DROP TABLE pages; --')
        self.assertEqual(self.k.stats()['pages'], 1)

    def test_real_snapshot_has_substantive_sources(self):
        self.k.seed(main.ROOT / 'data/seed.json')
        results = self.k.retrieve('rental deposit')
        self.assertTrue(results)
        self.assertTrue(any('rent' in r['url'] for r in results))
        self.assertTrue(all(r['provider'] == 'firecrawl' for r in results))
        self.assertGreaterEqual(self.k.stats()['pages'], 20)


class JourneyTests(unittest.TestCase):
    def test_document_routes_differ_by_citizenship(self):
        def arrival_ids(citizenship):
            return {s['id'] for s in localized('en', citizenship)[0]['steps']}
        self.assertIn('visa', arrival_ids('non-eu'))
        self.assertNotIn('visa', arrival_ids('eu'))
        self.assertNotIn('permit', arrival_ids('italian'))
        for kind in ['italian','international','eu','non-eu']:
            journeys = localized('it', kind)
            self.assertEqual(len(journeys), 6)
            self.assertTrue(all(s['source'].startswith('https://') for j in journeys for s in j['steps']))


class ApiTests(unittest.TestCase):
    def setUp(self):
        main.requests_this_hour.clear()
        main.chat_slots = asyncio.Semaphore(4)
        self.client_context = TestClient(main.app)
        self.client = self.client_context.__enter__()

    def tearDown(self):
        self.client_context.__exit__(None, None, None)

    def test_public_pages_and_missing_key(self):
        self.assertEqual(self.client.get('/health').status_code, 200)
        self.assertIn('frame-ancestors', self.client.get('/').headers['content-security-policy'])
        with patch.dict(os.environ, {'ANTHROPIC_API_KEY': ''}):
            response = self.client.post('/api/chat', json={'messages':[{'role':'user','content':'Help with housing'}]})
            self.assertEqual(response.status_code, 503)
            self.assertEqual(response.json()['detail'], 'CLAUDE_NOT_CONFIGURED')
        sources = self.client.get('/api/sources').json()
        self.assertGreaterEqual(len(sources), 20)
        self.assertTrue(all('markdown' not in source for source in sources))
        self.assertNotIn('API_KEY', self.client.get('/api/status').text)

    def test_input_limits_and_invalid_context(self):
        response = self.client.post('/api/chat', json={'messages':[{'role':'user','content':'x'*5001}]})
        self.assertEqual(response.status_code, 422)
        with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'test-key'}):
            response = self.client.post('/api/chat', json={'messages':[{'role':'user','content':'hello'}], 'journey_id':'not-a-journey'})
            self.assertEqual(response.status_code, 422)

    def test_claude_tool_loop_reads_sqlite_and_returns_provenance(self):
        calls=[]
        class FakeClaude:
            def __init__(self, **kwargs):
                self.messages=self
            async def create(self, **kwargs):
                calls.append(kwargs)
                if len(calls)==1:
                    return SimpleNamespace(stop_reason='tool_use', content=[SimpleNamespace(type='tool_use',id='search1',name='search_guides',input={'query':'rental deposit'})])
                return SimpleNamespace(stop_reason='end_turn', model='test-model', content=[SimpleNamespace(type='text',text='Read the deposit guide and check the terms at the source.')])
            async def close(self):
                pass
        with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'test-key'}), patch.object(main.anthropic,'AsyncAnthropic',FakeClaude):
            response = self.client.post('/api/chat',json={'messages':[{'role':'user','content':'Explain the deposit'}], 'profile':{'citizenship':'non-eu','language':'en','stage':'arriving'},'journey_id':'housing','step_id':'deposit'})
        self.assertEqual(response.status_code,200,response.text)
        self.assertTrue(response.json()['sources'])
        retrieved = json.loads(calls[1]['messages'][-2]['content'][0]['content'])
        self.assertTrue(any('rent' in r['url'] for r in retrieved))
        self.assertIn('deposit', calls[0]['system'])
        self.assertEqual(calls[0]['tool_choice']['name'],'search_guides')


if __name__ == '__main__':
    unittest.main()
