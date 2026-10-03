"""Compose reviewed card workflows; the model may only select existing blocks."""
from copy import deepcopy
import hashlib
import json

from webapp.journeys import localized


def compose(blocks, language='it', citizenship='international'):
    available = {j['id']: j for j in localized(language, citizenship)}
    if not blocks or len(blocks) > 15 or len(set(blocks)) != len(blocks) or any(b not in available for b in blocks):
        raise ValueError('Invalid or duplicate blocks')
    selected = [available[b] for b in blocks]
    revision = hashlib.sha256(json.dumps([(j['id'], j['plan_revision']) for j in selected]).encode()).hexdigest()[:12]
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
                blocks=blocks, steps=steps,
                priority=('Le conferme servono a seguire il piano. Verifica scadenze e attività urgenti anche in parallelo.' if it else
                          'Confirmations help you follow the plan. Check deadlines and urgent tasks in parallel too.') +
                         (' ' + available['arrival']['priority'] if citizenship == 'non-eu' and ('arrival' in blocks or 'permit' in blocks) else ''))
