"""Compose reviewed card workflows; the model may only select existing blocks."""
from copy import deepcopy
import hashlib
import json

from webapp.journeys import localized
from webapp.personalization import adaptive_cards, questions_for


def compose(blocks, language='it', citizenship='international', profile=None, residence_choice=None, suppressed=()):
    available = {j['id']: j for j in localized(language, citizenship)}
    if not blocks or len(blocks) > 15 or len(set(blocks)) != len(blocks) or any(b not in available for b in blocks):
        raise ValueError('Invalid or duplicate blocks')
    if len(set(suppressed)) != len(suppressed) or any(b not in available for b in suppressed):
        raise ValueError('Invalid excluded blocks')
    selected = [available[b] for b in blocks]
    excluded = []; decision_id = None; choice = None; questions = []
    if profile is not None:
        profile = {**profile, 'language':language, 'citizenship':citizenship}
        selected, excluded, decision_id, choice = adaptive_cards(profile, blocks, residence_choice, suppressed)
        questions = questions_for(profile, blocks)
        if not selected:
            selected = [{**available['arrival'], 'steps':[{'id':'review','title':'Rivedi i servizi selezionati' if language=='it' else 'Review selected services',
                'body':'Le risposte escludono i servizi selezionati. Rivedi i blocchi o chiarisci i dubbi con lo Student Desk.' if language=='it' else 'Your answers exclude the selected services. Review blocks or clarify questions with the Student Desk.',
                'checklist':['Ho verificato quali servizi mi servono' if language=='it' else 'I checked which services I need'],
                'source':'https://studyandwork.yesmilano.it/en/international-student-desk'}]}]
    revision = hashlib.sha256(json.dumps({'templates':[(j['id'], j['plan_revision']) for j in available.values()], 'blocks':blocks, 'suppressed':list(suppressed), 'policy':'adaptive-1' if profile is not None else 'legacy',
        'profile':{k:v for k,v in (profile or {}).items() if k != 'language'}}).encode()).hexdigest()[:12]
    steps = []
    for j in selected:
        for original in j['steps']:
            s = deepcopy(original)
            s.update(id=f"{j['id']}--{s['id']}", block_id=j['id'], block_title=j['title'],
                     original_step_id=original['id'], icon=j['icon'])
            if s.get('follows_choice'):
                s['follows_choice'] = f"{j['id']}--{s['follows_choice']}"
            steps.append(s)
    it = language == 'it'
    return dict(id='custom', plan_revision='custom-' + revision, title='Il mio percorso.' if it else 'My journey.',
                subtitle='Le tue guide, in un unico piano. Un passo alla volta.' if it else 'Your guides in one plan. One step at a time.',
                tag='CREATO DA TE' if it else 'CREATED BY YOU', icon=selected[0]['icon'], tone=selected[0]['tone'],
                blocks=blocks, steps=steps, adaptive=profile is not None, questions=questions, ready=not questions,
                excluded=excluded, decision_step_id=decision_id, residence_choice=choice,
                initial_choices={decision_id:choice} if decision_id and choice in {'keep','temporary','transfer'} else {},
                block_summaries=[{k:j.get(k) for k in ['id','title','subtitle','icon','tone','personalization_reason','order_locked']} | {'step_count':len(j['steps']), 'step_titles':[s['title'] for s in j['steps']]} for j in selected],
                answers={k:v for k,v in {**(profile or {}), **({'residence_intent':choice} if choice else {})}.items() if v is not None and k not in {'language','citizenship_confirmed'}},
                priority=('Le conferme servono a seguire il piano. Verifica scadenze e attività urgenti anche in parallelo.' if it else
                          'Confirmations help you follow the plan. Check deadlines and urgent tasks in parallel too.') +
                         (' ' + available['arrival']['priority'] if citizenship == 'non-eu' and ('arrival' in blocks or 'permit' in blocks) and (profile is None or profile.get('stay_duration') not in {'short',None,'unknown'}) and (profile is None or profile.get('permit') in {None,'none'}) else ''))
