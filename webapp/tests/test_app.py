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
            self.assertEqual(len(journeys), 15)
            self.assertTrue(all(s['source'].startswith('https://') for j in journeys for s in j['steps']))

    def test_catalogue_cases_all_have_indexed_guides_and_tools(self):
        from webapp.howto import CATALOG
        pages = json.loads((main.ROOT / 'data/seed.json').read_text())
        indexed = {p['url'] for p in pages}
        expected = {'arrival','visa','housing','permit','taxcode','transport','health',
                    'residence','temporary','bank','phone','support','identity','work','language'}
        self.assertEqual({entry['id'] for entry in CATALOG}, expected)
        self.assertTrue(all(entry['indexed_url'] in indexed for entry in CATALOG))
        for citizenship in ['italian','eu','non-eu','international']:
            journeys = localized('en', citizenship)
            self.assertEqual({j['id'] for j in journeys}, expected)
            self.assertTrue(all(j['steps'] and j['guide_url'] and j['source_title'] for j in journeys))
        self.assertEqual([sum(c['group']==g for c in CATALOG) for g in ['before','first','settled']], [3,8,4])
        tool = next(t for t in main.TOOLS if t['name']=='suggest_journey')
        self.assertEqual(set(tool['input_schema']['properties']['journey_id']['enum']), expected)

    def test_inapplicable_profiles_only_get_scope_orientation(self):
        italian = {j['id']:j for j in localized('it','italian')}
        non_eu = {j['id']:j for j in localized('en','non-eu')}
        self.assertEqual(len(italian['visa']['steps']), 1)
        self.assertEqual(len(italian['permit']['steps']), 1)
        self.assertEqual(len(non_eu['temporary']['steps']), 1)
        self.assertEqual(len(non_eu['visa']['steps']), 3)
        self.assertEqual(len(non_eu['permit']['steps']), 3)
        self.assertTrue(all('/KA-00595/' in s['source'] for s in italian['temporary']['steps']))

    def test_persona_plans_address_different_student_barriers(self):
        giulia = localized('it', 'italian')[0]
        reza = localized('en', 'non-eu')[0]
        self.assertEqual(giulia['persona'], 'Giulia')
        self.assertEqual(reza['persona'], 'Reza')
        self.assertEqual(len(giulia['steps']), 6)
        self.assertEqual(len(reza['steps']), 8)
        options = next(s for s in giulia['steps'] if s['id'] == 'giulia-status')
        self.assertEqual({c['id'] for c in options['choices']}, {'keep','temporary','transfer'})
        self.assertTrue(all(s['owner'] and s['validation'] for s in giulia['steps'] + reza['steps']))
        ids = [s['id'] for s in reza['steps']]
        self.assertLess(ids.index('permit'), ids.index('tax'))
        self.assertLess(ids.index('receipt'), ids.index('reza-residence'))
        self.assertIn('not mandatory', next(s for s in reza['steps'] if s['id']=='reza-residence')['body'])

    def test_persona_faqs_have_clean_content_and_update_dates(self):
        pages = json.loads((main.ROOT / 'data/seed.json').read_text())
        faqs = [p for p in pages if 'servizicrm.comune.milano.it' in p['url']]
        self.assertGreaterEqual(len(faqs), 4)
        self.assertTrue(all(p['stated_updated_date'] for p in faqs))
        self.assertTrue(all('Potrebbe' not in p['markdown'] and 'W3siQX' not in p['markdown'] for p in faqs))


class ApiTests(unittest.TestCase):
    def setUp(self):
        main.requests_today.clear()
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

    def test_composed_plan_preserves_choices_and_scopes_and_avoids_collisions(self):
        from webapp.builder import compose
        custom = compose(['arrival','housing','transport'], 'it', 'italian')
        originals = {j['id']:j for j in localized('it','italian')}
        self.assertEqual(len(custom['steps']),sum(len(originals[b]['steps']) for b in custom['blocks']))
        self.assertEqual(len({s['id'] for s in custom['steps']}),len(custom['steps']))
        choice = next(s for s in custom['steps'] if s.get('choices'))
        dependent = next(s for s in custom['steps'] if s.get('follows_choice'))
        self.assertEqual(dependent['follows_choice'],choice['id'])
        self.assertEqual(choice['id'],'arrival--giulia-status')
        self.assertIn('temporary',dependent['routes'])
        self.assertEqual(custom['plan_revision'],compose(['arrival','housing','transport'],'en','italian')['plan_revision'])
        self.assertNotEqual(custom['plan_revision'],compose(['housing','arrival','transport'],'it','italian')['plan_revision'])
        self.assertEqual(len(compose(['permit'],'it','italian')['steps']),1)
        reza = compose(['housing','permit'],'en','non-eu')
        self.assertIn('8 working days',reza['priority'])
        for blocks in [[],['housing','housing'],['invented']]:
            self.assertEqual(self.client.post('/api/plan/compose',json={'blocks':blocks}).status_code,422)
        self.assertEqual(self.client.post('/api/plan/compose',json={'blocks':['housing','transport']}).status_code,200)

    def test_plan_selector_one_model_call_and_rejects_invented_blocks(self):
        calls=[]
        selection={'blocks':['arrival','housing','transport'],'citizenship':'italian','stage':'here',
                   'answers':{'stay_duration':'year-plus','housing':'found','taxcode':'yes','grant':'yes','citizenship_confirmed':True}}
        class FakeClaude:
            def __init__(self,**kwargs): self.messages=self
            async def create(self,**kwargs):
                calls.append(kwargs)
                return SimpleNamespace(model='test-model',usage=SimpleNamespace(input_tokens=1200,output_tokens=80),
                    content=[SimpleNamespace(type='tool_use',name='select_blocks',input=selection)])
            async def close(self): pass
        body={'story':'Sono una studentessa italiana con borsa e dubbi sulla residenza.'}
        with patch.dict(os.environ,{'ANTHROPIC_API_KEY':'test-key'}),patch.object(main.anthropic,'AsyncAnthropic',FakeClaude):
            response=self.client.post('/api/plan/suggest',json=body)
            self.assertEqual(response.status_code,200,response.text)
            self.assertEqual(response.json()['blocks'],selection['blocks'])
            self.assertEqual(response.json()['usage']['model_calls'],1)
            self.assertEqual(response.json()['profile']['stay_duration'],'year-plus')
            self.assertEqual(response.json()['profile']['housing'],'found')
            self.assertFalse(response.json()['profile']['citizenship_confirmed'])
            adaptive=self.client.post('/api/plan/compose',json=response.json()).json()
            self.assertEqual(adaptive['questions'][0]['key'],'citizenship')
            self.assertNotIn('housing--needs',{s['id'] for s in adaptive['steps']})
            self.assertNotIn('taxcode--request',{s['id'] for s in adaptive['steps']})
            self.assertFalse(adaptive['ready'])
            self.assertNotIn('story',response.json())
            self.assertEqual(calls[0]['max_tokens'],650)
            self.assertEqual(calls[0]['tool_choice']['name'],'select_blocks')
            selection['blocks']=['invented']
            self.assertEqual(self.client.post('/api/plan/suggest',json=body).status_code,502)
            selection['blocks']=['housing','housing']
            self.assertEqual(self.client.post('/api/plan/suggest',json=body).status_code,502)
        with patch.dict(os.environ,{'ANTHROPIC_API_KEY':''}):
            self.assertEqual(self.client.post('/api/plan/suggest',json=body).status_code,503)
        with patch.dict(os.environ,{'ANTHROPIC_API_KEY':'test-key','CHAT_REQUESTS_PER_DAY':'0'}):
            self.assertEqual(self.client.post('/api/plan/suggest',json=body).status_code,429)
        self.assertEqual(self.client.post('/api/plan/suggest',json={'story':'x'*2001}).status_code,422)

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
            response = self.client.post('/api/chat',json={'messages':[{'role':'user','content':'Explain the deposit'}], 'profile':{'citizenship':'non-eu','language':'en','stage':'arriving'},'journey_id':'custom','custom_blocks':['housing','transport'],'step_id':'housing--deposit','validated_step_ids':['housing--needs','housing--viewing','housing--contract']})
        self.assertEqual(response.status_code,200,response.text)
        self.assertTrue(response.json()['sources'])
        retrieved = json.loads(calls[1]['messages'][-2]['content'][0]['content'])
        self.assertTrue(any('rent' in r['url'] for r in retrieved))
        self.assertIn('deposit', calls[0]['system'])
        self.assertEqual(calls[0]['tool_choice']['name'],'search_guides')
        self.assertIn('user_confirmed_steps', calls[0]['system'])
        self.assertIn('never confirm or unlock', calls[0]['system'])


if __name__ == '__main__':
    unittest.main()
