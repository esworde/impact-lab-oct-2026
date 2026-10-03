"""Reviewed navigation/checklists, not automatic eligibility decisions."""
from webapp.personas import arrival_for, DOMICILE, ITALIAN_RESIDENCE
from webapp.howto import additional, CATALOG

BASE = 'https://studyandwork.yesmilano.it/en'
FIRST = BASE + '/study/how-to/first-steps'
RENT = BASE + '/study/how-to/rents'
RESIDENCE = BASE + '/study/how-to/take-residence-milano-students'
TAX = BASE + '/study/how-to/get-italian-tax-code-codice-fiscale'
PASS = BASE + '/study/how-to/get-your-student-transportation-pass'
HEALTH = BASE + '/study/how-to/national-health-service-students-step-step'
DESK = BASE + '/international-student-desk'


def b(it, en):
    return {'it': it, 'en': en}


def step(id, title, body, source, checklist, audiences=None):
    return {'id': id, 'title': b(*title), 'body': b(*body), 'source': source,
            'checklist': [b(*item) for item in checklist], 'audiences': audiences}


JOURNEYS = [
    {'id': 'arrival', 'icon': 'arrival', 'tone': 'rose',
     'title': b('Milano, si comincia.', 'Milan, here I come.'),
     'subtitle': b('Il tuo arrivo, un passo alla volta.', 'Your arrival, one step at a time.'),
     'tag': b('PRIMI PASSI', 'FIRST STEPS'),
     'questions': [b('Sto per arrivare a Milano. Da dove inizio?', 'I am moving to Milan. Where do I start?'),
                   b('Quali documenti devo preparare?', 'Which documents should I prepare?')],
     'steps': [
         step('plan', ('Metti a fuoco il tuo arrivo', 'Make an arrival plan'),
              ('Parti dalla guida First Steps. Separa ciò che puoi preparare prima del viaggio da ciò che farai una volta a Milano.', 'Start with the First Steps guide. Separate what you can prepare before travelling from what you will do in Milan.'), FIRST,
              [('Ho letto la guida ai primi passi', 'I read the first-steps guide'), ('Ho preparato la mia lista di priorità', 'I made a list of priorities')]),
         step('visa', ('Verifica il percorso visto', 'Check the visa route'),
              ('Consulta la guida e il consolato competente per capire quale procedura si applica al tuo caso. L’assistente può aiutarti a leggere i requisiti.', 'Consult the guide and the relevant consulate to understand which process applies to your situation. The assistant can help explain the requirements.'), BASE + '/study/how-to/student-visa',
              [('Ho verificato le indicazioni per il mio caso', 'I checked the guidance for my situation')], ['non-eu']),
         step('home', ('Trova un primo punto di appoggio', 'Find a place to land'),
              ('Esplora le opzioni abitative e leggi cosa controllare prima di firmare un contratto. Puoi approfondire nel percorso Casa.', 'Explore housing options and read what to check before signing a contract. Continue in the Housing journey for more detail.'), RENT,
              [('Ho scelto le zone da esplorare', 'I chose areas to explore'), ('Ho controllato i punti essenziali del contratto', 'I checked the essential contract points')]),
         step('tax', ('Orientati sul codice fiscale', 'Understand the tax code'),
              ('Verifica se hai già un codice fiscale e consulta il percorso ufficiale per richiederlo, se necessario.', 'Check whether you already have an Italian tax code and consult the official guide to apply if needed.'), TAX,
              [('Ho verificato se ho già un codice fiscale', 'I checked whether I already have a tax code'), ('Ho letto come procedere se mi serve', 'I read how to proceed if I need one')]),
         step('permit', ('Verifica i documenti di soggiorno', 'Check residence-permit guidance'),
              ('Leggi la guida sul permesso di soggiorno e verifica modalità e tempi aggiornati presso le autorità competenti.', 'Read the residence-permit guide and check current procedures and deadlines with the relevant authorities.'), BASE + '/study/how-to/residence-permit-students',
              [('Ho verificato la procedura applicabile', 'I checked the applicable process')], ['non-eu']),
         step('settle', ('Organizza i primi giorni', 'Organise your first days'),
              ('Trasporti, assistenza sanitaria e un punto di riferimento: scegli il prossimo percorso in base a ciò che ti serve adesso.', 'Transport, healthcare and someone to ask: choose the next journey based on what you need now.'), FIRST,
              [('Ho individuato il prossimo passo', 'I identified my next step'), ('So come contattare lo Student Desk', 'I know how to contact the Student Desk')]),
     ]},
    {'id': 'housing', 'icon': 'housing', 'tone': 'sand',
     'title': b('Un posto da chiamare casa.', 'A place to call home.'),
     'subtitle': b('Dalla ricerca alle chiavi. Con più chiarezza.', 'From searching to getting the keys. With clarity.'),
     'tag': b('CASA & COINQUILINI', 'HOUSING & ROOMMATES'),
     'questions': [b('Cosa controllo prima di firmare un affitto?', 'What should I check before signing a lease?'),
                   b('Come funziona il deposito cauzionale?', 'How does a rental deposit work?')],
     'steps': [
         step('needs', ('Definisci la casa che cerchi', 'Define what you need'),
              ('Stanza o appartamento? Durata, budget e collegamenti con l’università sono un buon punto di partenza. Non serve condividere indirizzi o dati personali.', 'Room or apartment? Duration, budget and connections to your university are a good starting point. You do not need to share addresses or personal details.'), RENT,
              [('Ho definito budget e durata', 'I defined a budget and duration'), ('Ho valutato i collegamenti con l’università', 'I considered transport to university')]),
         step('viewing', ('Prepara le domande per la visita', 'Prepare questions for the viewing'),
              ('La guida raccoglie le domande da fare prima di firmare: spese, condizioni della casa e cosa è incluso. Chiedi chiarimenti prima di decidere.', 'The guide lists questions to ask before signing: costs, property condition and what is included. Get clarification before deciding.'), RENT,
              [('Ho preparato le domande da fare', 'I prepared my questions'), ('Ho chiarito costi e servizi inclusi', 'I clarified included costs and services')]),
         step('contract', ('Leggi il contratto con attenzione', 'Read the contract carefully'),
              ('Confronta il tipo di contratto proposto con la guida per studenti. Per dubbi specifici usa i servizi di supporto indicati nella fonte.', 'Compare the proposed contract type with the student guide. For specific concerns use the support services listed in the source.'), RENT,
              [('Ho identificato il tipo di contratto', 'I identified the contract type'), ('Ho chiarito le clausole che non capivo', 'I clarified clauses I did not understand')]),
         step('deposit', ('Chiarisci deposito e pagamenti', 'Clarify the deposit and payments'),
              ('Controlla nella guida la sezione sul deposito e concorda come documentare i pagamenti. L’assistente può spiegarti i termini.', 'Check the deposit section in the guide and clarify how payments will be documented. The assistant can explain the terms.'), RENT,
              [('Ho chiarito importi e condizioni del deposito', 'I clarified the deposit amount and conditions'), ('Ho verificato come documentare i pagamenti', 'I checked how to document payments')]),
         step('handover', ('Organizza ingresso e adempimenti', 'Organise moving in and next actions'),
              ('Verifica registrazione del contratto, utenze e indicazioni TARI. Consulta le fonti prima di completare gli adempimenti.', 'Check contract registration, utilities and TARI guidance. Consult the sources before completing any formalities.'), RENT,
              [('Ho verificato registrazione e spese', 'I checked registration and costs'), ('Ho letto le indicazioni TARI', 'I read the TARI guidance')]),
     ]},
    {'id': 'transport', 'icon': 'transport', 'tone': 'blue',
     'title': b('La città, a portata di metro.', 'Your city, a metro ride away.'),
     'subtitle': b('Orientati tra abbonamenti e spostamenti.', 'Find your way around passes and transport.'),
     'tag': b('MUOVERSI A MILANO', 'GETTING AROUND'),
     'questions': [b('Quale abbonamento trasporti fa per me?', 'Which transport pass should I choose?'),
                   b('Come ottengo la tessera ATM?', 'How do I get an ATM travel card?')],
     'steps': [
         step('routes', ('Metti a fuoco i tuoi spostamenti', 'Plan your regular journeys'),
              ('Considera dove studierai e le tratte che percorrerai. Poi confronta le opzioni della guida.', 'Consider where you will study and your regular routes. Then compare the guide’s options.'), PASS,
              [('Ho individuato le mie tratte principali', 'I identified my main routes')]),
         step('pass', ('Confronta abbonamenti e requisiti', 'Compare passes and requirements'),
              ('Leggi la guida per studenti e verifica le condizioni aggiornate sul sito dell’operatore. Prezzi e agevolazioni possono cambiare.', 'Read the student guide and check current conditions on the operator’s website. Prices and discounts can change.'), PASS,
              [('Ho confrontato le opzioni applicabili', 'I compared applicable options'), ('Ho verificato le tariffe alla fonte', 'I checked fares at the source')]),
         step('card', ('Segui la procedura per la tessera', 'Follow the travel-card process'),
              ('Usa il canale indicato nella guida per richiedere la tessera o caricare l’abbonamento. Verifica cosa preparare prima di iniziare.', 'Use the channel listed in the guide to apply for a card or load a pass. Check what you need before starting.'), PASS,
              [('Ho verificato il canale e i documenti richiesti', 'I checked the channel and required documents')]),
     ]},
    {'id': 'health', 'icon': 'health', 'tone': 'sage',
     'title': b('Prenditi cura di te.', 'Make room for your wellbeing.'),
     'subtitle': b('Capisci come accedere all’assistenza sanitaria.', 'Understand how to access healthcare.'),
     'tag': b('SALUTE & BENESSERE', 'HEALTH & WELLBEING'),
     'questions': [b('Come funziona l’assistenza sanitaria per studenti?', 'How does healthcare work for students?'),
                   b('Da dove comincio per scegliere un medico?', 'Where do I start to find a doctor?')],
     'steps': [
         step('coverage', ('Verifica la tua copertura', 'Check your coverage'),
              ('La guida distingue diverse situazioni. Individua la sezione pertinente senza condividere dati medici o personali in chat.', 'The guide distinguishes different situations. Find the relevant section without sharing medical or personal information in chat.'), HEALTH,
              [('Ho individuato la sezione relativa al mio caso', 'I identified the section relevant to my situation')]),
         step('access', ('Leggi il percorso di accesso', 'Read the access process'),
              ('Consulta requisiti, documenti e canali nella fonte e verifica le indicazioni aggiornate con il servizio competente.', 'Consult requirements, documents and channels in the source and verify current guidance with the relevant service.'), HEALTH,
              [('Ho letto documenti e canali di accesso', 'I read the document and access guidance')]),
         step('next', ('Individua chi contattare', 'Find who to contact'),
              ('Segui i riferimenti della guida per chiarire i prossimi passi, compresa la scelta del medico quando applicabile.', 'Follow the guide’s contacts to clarify your next steps, including selecting a doctor where applicable.'), HEALTH,
              [('Ho individuato il riferimento corretto', 'I identified the right contact')]),
     ]},

]


# Exact coverage and ordering of the public catalogue; unrelated resources remain searchable in chat.
_by_id = {j['id']: j for j in JOURNEYS + additional(b, step, BASE)}
JOURNEYS = [{**_by_id[entry['id']], 'group': entry['group'],
             'guide_url': entry['guide_url'], 'indexed_url': entry['indexed_url'],
             'source_title': entry['source_title']} for entry in CATALOG]


def localized(language='it', citizenship='international'):
    def translate(value):
        if isinstance(value, dict):
            if set(value) == {'it', 'en'}:
                return value[language]
            return {k: translate(v) for k, v in value.items() if k != 'audiences'}
        if isinstance(value, list):
            return [translate(v) for v in value]
        return value
    result = []
    for journey in JOURNEYS:
        if journey['id'] == 'arrival':
            persona_plan = arrival_for(citizenship)
            if persona_plan:
                journey = {**journey, **persona_plan}
                journey['questions'] = ([b('Devo cambiare residenza? E la borsa di studio?', 'Should I change residence? What about my grant?'),
                                         b('Come chiedo il domicilio temporaneo?', 'How do I request temporary student domicile?')]
                                        if citizenship == 'italian' else
                                        [b('Permesso, codice fiscale e residenza: in che ordine?', 'Permit, tax code and residence: in which order?'),
                                         b('Non ho SPID: come accedo ai servizi?', 'I have no SPID: how do I access services?')])
        if journey['id'] == 'temporary' and citizenship == 'italian':
            journey = {**journey, 'steps': [{**s, 'source': DOMICILE} for s in journey['steps']]}
        if journey['id'] == 'residence' and citizenship == 'italian':
            journey = {**journey, 'steps': [{**s, 'source': ITALIAN_RESIDENCE} for s in journey['steps']]}
        item = translate(journey)
        item.setdefault('plan_revision', 'guided-1')
        item['steps'] = [translate(s) for s in journey['steps']
                         if not s['audiences'] or citizenship in s['audiences']]
        result.append(item)
    return result
