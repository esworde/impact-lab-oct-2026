import asyncio
from copy import deepcopy
import json
import os
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from webapp import main
from webapp.builder import compose
from webapp.personalization import Profile
from webapp.planning import AuthoredPlan, materialize


class AIPlanningTests(unittest.TestCase):
    def setUp(self):
        main.requests_today.clear()
        main.chat_slots = asyncio.Semaphore(4)
        self.ctx = TestClient(main.app)
        self.client = self.ctx.__enter__()
        self.profile = Profile(language='it', citizenship='italian', citizenship_confirmed=True,
            stage='here', stay_duration='year-plus', housing='found', taxcode='yes', digital_id='yes',
            residence_status='elsewhere', residence_intent='undecided', grant='yes', health_coverage='unknown').model_dump()
        self.blocks = ['arrival','housing','transport','health']
        self.base = compose(self.blocks, 'it','italian',self.profile)

    def tearDown(self):
        self.ctx.__exit__(None, None, None)

    def authored(self, base=None):
        base = base or self.base
        return AuthoredPlan(base_revision=base['plan_revision'], plan_revision='ai-123456789abc',
            language='it', title='La tua vita a Milano', subtitle='Il piano per una casa già trovata',
            rationale='Parti dal controllo della borsa prima di scegliere la tua situazione anagrafica.',
            steps=[dict(id=s['id'], title='Azione personalizzata: '+s['title'],
                        body='La tua situazione richiede una verifica con il servizio indicato nella fonte.',
                        checklist=['Ho chiarito il punto per il mio caso'], why='Hai già trovato una sistemazione.',
                        source_urls=[s['source']]) for s in base['steps']])

    def fake_claude(self, calls):
        class FakeClaude:
            def __init__(self, **kwargs): self.messages = self
            async def create(self, **kwargs):
                calls.append(kwargs)
                context = json.loads(kwargs['messages'][0]['content'])
                source = context['sources'][0]['id']
                output = dict(title='Il tuo piano scritto da Claude', subtitle='Un caso con casa già trovata',
                    rationale='Confronta borsa e scelta anagrafica, poi organizza i servizi quotidiani.',
                    block_order=[b['id'] for b in context['services']],
                    steps=[dict(id=s['id'], title='Piano AI: '+s['title'], body='Hai una sistemazione: verifica le indicazioni pertinenti con il servizio e conserva i riferimenti.',
                        checklist=['Ho verificato questo passaggio per il mio caso'], why='Questo passo dipende dalla situazione che hai descritto.', source_ids=[source])
                        for s in context['required_steps_this_batch']])
                return SimpleNamespace(model='test-haiku', stop_reason='tool_use',
                    usage=SimpleNamespace(input_tokens=2000,output_tokens=800),
                    content=[SimpleNamespace(type='tool_use',name='build_student_plan',input=output)])
            async def close(self): pass
        return FakeClaude

    def test_authored_actions_preserve_choices_sources_and_required_checks(self):
        plan = materialize(self.base, self.authored(), main.knowledge.sources())
        self.assertTrue(plan['ai_generated'])
        self.assertNotEqual(plan['steps'][0]['body'], self.base['steps'][0]['body'])
        for original, authored in zip(self.base['steps'], plan['steps']):
            self.assertEqual(original['source'], authored['source'])
            self.assertTrue(set(original['checklist']).issubset(authored['checklist']))
            self.assertEqual(original.get('choices'), authored.get('choices'))
        self.assertEqual(plan['base_revision'], self.base['plan_revision'])

    def test_reject_missing_steps_unknown_sources_and_changed_dependencies(self):
        memory = self.authored()
        missing = memory.model_copy(deep=True)
        missing.steps.pop()
        with self.assertRaises(ValueError): materialize(self.base, missing, main.knowledge.sources())
        bad = memory.model_copy(deep=True)
        bad.steps[0].source_urls = ['https://untrusted.example/invented-service']
        with self.assertRaises(ValueError): materialize(self.base, bad, main.knowledge.sources())
        bad = memory.model_copy(deep=True)
        bad.steps[0],bad.steps[1] = bad.steps[1],bad.steps[0]
        with self.assertRaises(ValueError): materialize(self.base, bad, main.knowledge.sources())
        bad = memory.model_copy(update={'base_revision':'stale'})
        with self.assertRaises(ValueError): materialize(self.base, bad, main.knowledge.sources())

    def test_ai_endpoint_and_replanning_preserve_verified_prefix(self):
        calls = []
        body = {'blocks':self.blocks,'profile':self.profile}
        with patch.dict(os.environ,{'ANTHROPIC_API_KEY':'test-key'}),patch.object(main.anthropic,'AsyncAnthropic',self.fake_claude(calls)):
            response = self.client.post('/api/plan/generate',json=body)
            self.assertEqual(response.status_code,200,response.text)
            original = response.json()
            self.assertEqual(original['usage']['model_calls'],1)
            self.assertEqual(calls[0]['max_tokens'],4000)
            self.assertEqual(calls[0]['tool_choice']['name'],'build_student_plan')
            change = {**body,'residence_choice':'temporary','previous':original,'preserve_through':original['decision_step_id']}
            response = self.client.post('/api/plan/generate',json=change)
            self.assertEqual(response.status_code,200,response.text)
            updated = response.json()
            self.assertEqual(updated['plan_revision'],original['plan_revision'])
            self.assertEqual(updated['steps'][:3],original['steps'][:3])
            self.assertTrue(any(s['id'].startswith('temporary--') for s in updated['steps']))
            sent = json.loads(calls[-1]['messages'][0]['content'])['required_steps_this_batch']
            self.assertFalse(any(s['id']=='arrival--giulia-status' for s in sent))
            translated=self.client.post('/api/plan/generate',json={**body,
                'profile':{**self.profile,'language':'en'},'previous':original})
            self.assertEqual(translated.status_code,200,translated.text)
            self.assertNotEqual(translated.json()['plan_revision'],original['plan_revision'])
            edited=self.client.post('/api/plan/generate',json={**body,
                'profile':{**self.profile,'stay_duration':'under-year'}})
            self.assertEqual(edited.status_code,200,edited.text)
            self.assertNotEqual(edited.json()['plan_revision'],original['plan_revision'])

    def test_missing_answers_or_provider_key_do_not_produce_fake_ai_plans(self):
        with patch.dict(os.environ,{'ANTHROPIC_API_KEY':''}):
            missing = self.client.post('/api/plan/generate',json={'blocks':['bank']})
            self.assertEqual(missing.status_code,422)
            self.assertEqual(missing.json()['detail'],'PLAN_NEEDS_ANSWERS')
            response = self.client.post('/api/plan/generate',json={'blocks':self.blocks,'profile':self.profile})
            self.assertEqual(response.status_code,503)
        with patch.dict(os.environ,{'ANTHROPIC_API_KEY':'test-key','CHAT_REQUESTS_PER_DAY':'0'}):
            response = self.client.post('/api/plan/generate',json={'blocks':self.blocks,'profile':self.profile})
            self.assertEqual(response.status_code,429)

    def test_large_plan_batches_are_bounded_and_cover_all_steps(self):
        calls=[]
        blocks=[b['id'] for b in main.JOURNEYS]
        with patch.dict(os.environ,{'ANTHROPIC_API_KEY':'test-key'}),patch.object(main.anthropic,'AsyncAnthropic',self.fake_claude(calls)):
            response=self.client.post('/api/plan/generate',json={'blocks':blocks,'profile':self.profile})
        self.assertEqual(response.status_code,200,response.text)
        plan=response.json()
        self.assertEqual(len(plan['steps']),len(compose(blocks,'it','italian',self.profile)['steps']))
        self.assertGreater(len(calls),1)
        self.assertTrue(all(len(json.loads(c['messages'][0]['content'])['required_steps_this_batch'])<=15 for c in calls))

    def test_chat_uses_saved_ai_actions_and_rejects_stale_snapshot(self):
        calls=[]
        class FakeClaude:
            def __init__(self, **kwargs): self.messages=self
            async def create(self, **kwargs):
                calls.append(kwargs)
                if len(calls)==1:
                    return SimpleNamespace(stop_reason='tool_use', content=[SimpleNamespace(type='tool_use',id='search1',name='search_guides',input={'query':'student domicile'})])
                return SimpleNamespace(stop_reason='end_turn',model='test-haiku',content=[SimpleNamespace(type='text',text='Verifica con il servizio indicato.')])
            async def close(self): pass
        plan=materialize(self.base,self.authored(),main.knowledge.sources())
        body=dict(messages=[{'role':'user','content':'Spiega questo passo'}],profile=self.profile,
                  journey_id='custom',custom_blocks=self.blocks,step_id=plan['steps'][0]['id'],generated_plan=plan)
        with patch.dict(os.environ,{'ANTHROPIC_API_KEY':'test-key'}),patch.object(main.anthropic,'AsyncAnthropic',FakeClaude):
            response=self.client.post('/api/chat',json=body)
            self.assertEqual(response.status_code,200,response.text)
            self.assertIn(plan['steps'][0]['body'],calls[0]['system'])
            self.assertIn(plan['steps'][0]['why'],calls[0]['system'])
            body['generated_plan']['base_revision']='stale'
            self.assertEqual(self.client.post('/api/chat',json=body).status_code,422)


if __name__ == '__main__': unittest.main()
