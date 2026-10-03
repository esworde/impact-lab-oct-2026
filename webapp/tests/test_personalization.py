import json
from pathlib import Path
import unittest
from webapp.builder import compose
from webapp.personalization import Profile, SHORT_STAY, questions_for
from webapp.journeys import JOURNEYS


class PersonalizedPlanTests(unittest.TestCase):
    def profile(self, **changes):
        return Profile(citizenship='italian', citizenship_confirmed=True, stay_duration='year-plus',
            housing='found', taxcode='yes', digital_id='yes', residence_status='elsewhere',
            residence_intent='undecided', grant='yes', health_coverage='yes').model_copy(update=changes).model_dump()

    def plan(self, profile=None, blocks=None, choice=None):
        p=profile or self.profile()
        return compose(blocks or ['arrival','housing','transport','health'],p['language'],p['citizenship'],p,choice)

    def test_answers_change_steps_and_services_not_just_card_order(self):
        known=self.plan()
        unknown=self.plan(self.profile(housing='searching',taxcode='no',grant='no',health_coverage='no'))
        ids=lambda j:{s['id'] for s in j['steps']}
        self.assertNotIn('housing--needs',ids(known))
        self.assertIn('housing--needs',ids(unknown))
        self.assertNotIn('taxcode--request',ids(known))
        self.assertIn('taxcode--request',ids(unknown))
        self.assertIn('arrival--giulia-study',ids(known))
        self.assertNotIn('arrival--giulia-study',ids(unknown))
        self.assertNotIn('health--coverage',ids(known))
        self.assertIn('health--coverage',ids(unknown))
        self.assertNotEqual(known['plan_revision'],unknown['plan_revision'])
        self.assertTrue(all(j['personalization_reason'] for j in known['block_summaries']))
        self.assertNotIn('already have',next(s['body'] for s in known['steps'] if s['id']=='arrival--giulia-study'))

    def test_residence_decisions_change_sources_checklists_and_services(self):
        keep=self.plan(choice='keep'); temporary=self.plan(choice='temporary'); transfer=self.plan(choice='transfer')
        ids=lambda j:{s['id'] for s in j['steps']}
        self.assertIn('arrival--keep-residence',ids(keep))
        self.assertFalse(any(id.startswith(('temporary--','residence--')) for id in ids(keep)))
        self.assertTrue(any(id.startswith('temporary--') for id in ids(temporary)))
        self.assertFalse(any(id.startswith('residence--') for id in ids(temporary)))
        self.assertTrue(any(id.startswith('residence--') for id in ids(transfer)))
        self.assertFalse(any(id.startswith('temporary--') for id in ids(transfer)))
        prep=next(s for s in temporary['steps'] if s['id']=='temporary--prepare')
        self.assertTrue(prep['draft']);self.assertIn('/KA-00595/',prep['source'])
        self.assertTrue(any('dichiarazione' in c for c in prep['checklist']))
        access=next(s for s in transfer['steps'] if s['id']=='residence--access')
        self.assertIn('ANPR',access['body']);self.assertIn('/KA-00371/',access['source'])
        no_id=self.plan(self.profile(digital_id='no'),choice='transfer')
        self.assertIn('contattato',next(s for s in no_id['steps'] if s['id']=='residence--access')['checklist'][0])
        decision=temporary['decision_step_id']
        prefix=lambda j:j['steps'][:next(i for i,s in enumerate(j['steps']) if s['id']==decision)+1]
        self.assertEqual(prefix(keep),prefix(temporary))
        self.assertEqual(prefix(temporary),prefix(transfer))
        self.assertEqual(keep['plan_revision'],temporary['plan_revision'])
        self.assertEqual(transfer['answers']['residence_intent'],'transfer')

    def test_non_eu_short_stay_and_application_status_have_distinct_routes(self):
        p=self.profile(citizenship='non-eu',stage='here',grant='no',residence_intent='transfer',permit='none')
        short=self.plan({**p,'stay_duration':'short'},['permit'])
        self.assertEqual([s['id'] for s in short['steps']],['permit--short-stay'])
        self.assertEqual(short['steps'][0]['source'],SHORT_STAY)
        pending=self.plan({**p,'permit':'pending'},['permit'])
        self.assertEqual([s['id'] for s in pending['steps']],['permit--follow-up'])
        valid=self.plan({**p,'permit':'valid'},['permit'])
        self.assertEqual([s['id'] for s in valid['steps']],['permit--validity'])
        first=self.plan(p,['permit'])
        self.assertIn('permit--kit',{s['id'] for s in first['steps']})
        self.assertIn('8 working days',self.plan({**p,'language':'en'},['permit'])['priority'])
        uncertain=self.plan({**p,'stay_duration':'unknown'},['permit'])
        self.assertNotIn('permit--kit',{s['id'] for s in uncertain['steps']})
        receipt_res=self.plan({**p,'permit':'pending'},['residence'])
        self.assertIn('ricevuta',next(s for s in receipt_res['steps'] if s['id']=='residence--documents')['body'])

    def test_eu_duration_and_existing_residence_control_the_temporary_route(self):
        p=self.profile(citizenship='eu',stay_duration='under-year',residence_intent='temporary',grant='no')
        temporary=self.plan(p,['temporary'])
        self.assertIn('temporary--prepare',{s['id'] for s in temporary['steps']})
        self.assertNotIn('/KA-00595/',next(s for s in temporary['steps'] if s['id']=='temporary--prepare')['source'])
        longer=self.plan({**p,'stay_duration':'year-plus'},['temporary'])
        self.assertNotIn('temporary--prepare',{s['id'] for s in longer['steps']})
        decision=next(s for s in longer['steps'] if s.get('choices'))
        self.assertNotIn('temporary',{c['id'] for c in decision['choices']})
        resident=self.plan(self.profile(residence_status='milan',residence_intent='temporary'),['arrival','temporary','residence'])
        self.assertFalse(any(s['id'].startswith(('temporary--','residence--')) for s in resident['steps']))
        self.assertEqual({c['id'] for c in resident['excluded']},{'temporary','residence'})

    def test_bank_documents_match_pending_or_valid_permit_and_ask_when_missing(self):
        p=self.profile(citizenship='non-eu',stage='here',permit=None)
        self.assertEqual({q['key'] for q in questions_for(p,['bank'])},{'permit'})
        pending=self.plan({**p,'permit':'pending'},['bank'])
        valid=self.plan({**p,'permit':'valid'},['bank'])
        documents=lambda j:next(s for s in j['steps'] if s['id']=='bank--documents')
        self.assertIn('ricevuta',documents(pending)['checklist'][1])
        self.assertIn('permesso italiano valido',documents(valid)['checklist'][1])
        self.assertNotIn('taxcode--request',{s['id'] for s in pending['steps']})
        self.assertTrue(pending['ready'])

    def test_missing_answers_generate_relevant_followups_and_explicit_unknown_is_allowed(self):
        p=Profile(citizenship='italian').model_dump()
        questions=questions_for(p,['phone'])
        self.assertEqual({q['key'] for q in questions},{'stay_duration','taxcode'})
        self.assertFalse(self.plan(p,['phone'])['ready'])
        p.update(stay_duration='unknown',taxcode='unknown')
        self.assertTrue(self.plan(p,['phone'])['ready'])
        p=Profile().model_dump()
        self.assertEqual(questions_for(p,['arrival'])[0]['key'],'citizenship')
        p['citizenship_confirmed']=True
        self.assertNotIn('citizenship',{q['key'] for q in questions_for(p,['arrival'])})
        known=self.profile(citizenship='non-eu',stage='arriving',country=None,visa=None)
        self.assertEqual({q['key'] for q in questions_for(known,['visa'])},{'country','visa'})

    def test_all_cases_keep_unique_steps_and_indexed_primary_sources(self):
        pages=json.loads((Path(__file__).parents[1]/'data/seed.json').read_text())
        sources={p['url'] for p in pages}
        blocks=[j['id'] for j in JOURNEYS]
        for citizenship in ['italian','eu','non-eu','international']:
            for stay in ['short','under-year','year-plus','unknown']:
                p=self.profile(citizenship=citizenship,stay_duration=stay,country='unknown',permit='pending',visa='yes')
                plan=self.plan(p,blocks)
                self.assertTrue(plan['steps'])
                self.assertEqual(len(plan['steps']),len({s['id'] for s in plan['steps']}))
                self.assertLess(len(plan['steps']),100)
                self.assertTrue(all(s['checklist'] for s in plan['steps']))
                # Both canonical YesMilano hosts reference the same indexed guide path.
                for s in plan['steps']:
                    url=s['source'].replace('https://www.yesmilano.it/en/study/how-to/','https://studyandwork.yesmilano.it/en/study/how-to/')
                    self.assertTrue(url in sources or s['source'] in sources,s['source'])
