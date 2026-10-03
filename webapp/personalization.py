"""Source-backed plan rules. Unknown answers lead to verification, never guessed eligibility."""
from copy import deepcopy
from typing import Literal
from pydantic import BaseModel, Field

from webapp.personas import arrival_for, DOMICILE, ITALIAN_RESIDENCE, VALID_PERMIT, LEASE, TARI
from webapp.journeys import localized

SHORT_STAY = 'https://italiana.esteri.it/italiana/opportunity/studying-in-italy/visas-and-permits/'
DESK = 'https://studyandwork.yesmilano.it/en/international-student-desk'


class Profile(BaseModel):
    language: Literal['it','en'] = 'it'
    citizenship: Literal['italian','international','eu','non-eu'] = 'international'
    stage: Literal['arriving','here'] = 'arriving'
    citizenship_confirmed: bool = False
    stay_duration: Literal['short','under-year','year-plus','unknown'] | None = None
    country: str | None = Field(default=None, min_length=2, max_length=50)
    housing: Literal['searching','found','unknown'] | None = None
    taxcode: Literal['yes','no','unknown'] | None = None
    taxcode_document: Literal['available','missing','unknown'] | None = None
    digital_id: Literal['yes','no','unknown'] | None = None
    residence_status: Literal['elsewhere','milan','unknown'] | None = None
    residence_intent: Literal['undecided','keep','temporary','transfer'] | None = None
    grant: Literal['yes','no','unknown'] | None = None
    visa: Literal['yes','no','unknown'] | None = None
    permit: Literal['none','pending','valid','unknown'] | None = None
    health_coverage: Literal['yes','no','unknown'] | None = None


def text(language, it, en):
    return it if language == 'it' else en


def question(key, title, options, language, why, kind='choice'):
    return {'key':key, 'title':text(language,*title), 'why':text(language,*why), 'kind':kind,
            'options':[{'id':id,'title':text(language,*label)} for id,label in options]}


def questions_for(profile, blocks):
    p = profile
    lang = p['language']
    all_services = 'arrival' in blocks
    relevant = lambda ids: all_services or bool(set(ids) & set(blocks))
    yes_no = [('yes',('Sì','Yes')),('no',('No','No')),('unknown',('Da verificare','To check'))]
    questions = [question('stay_duration',('Quanto pensi di restare a Milano per studiare?','How long will you stay in Milan to study?'),[
        ('short',('Fino a 90 giorni','Up to 90 days')),('under-year',('Oltre 90 giorni, meno di un anno','Over 90 days, under one year')),
        ('year-plus',('Un anno o più','One year or longer')),('unknown',('Da verificare','To check'))],lang,
        ('La durata cambia le guide su ingresso, soggiorno, registrazione e casa.','Duration changes entry, stay, registration and housing guidance.'))]
    if p['citizenship'] == 'non-eu' and relevant(['visa','permit','residence','bank']):
        if p['stage']=='arriving' or 'visa' in blocks:
            questions.append(question('country',('Qual è il Paese della tua cittadinanza?','What is your country of citizenship?'),[],lang,
            ('Serve per la verifica sul portale visti del consolato, senza dedurre i requisiti dalla lingua. Scrivi solo il Paese o “da verificare”.','Use it when checking the consular visa portal; language does not determine requirements. Enter only the country or “to check”.'),'country'))
        if p['stage'] == 'arriving':
            questions.append(question('visa',('Hai già il visto per questo soggiorno?','Do you already have a visa for this stay?'),yes_no,lang,
                ('Se lo hai già, eviti una nuova richiesta e verifichi il documento esistente.','An existing visa leads to verification rather than a new application.')))
        else:
            questions.append(question('permit',('A che punto sono i documenti di soggiorno?','What is the status of your stay documents?'),[
                ('none',('Richiesta non ancora presentata','Application not yet submitted')),('pending',('Richiesta presentata, ho la ricevuta','Submitted, I have the receipt')),
                ('valid',('Ho un permesso italiano valido','I have a valid Italian permit')),('unknown',('Da verificare','To check'))],lang,
                ('Non ti faremo ripresentare un kit già consegnato.','We will not ask you to submit an already-submitted kit again.')))
    if relevant(['housing','residence','temporary']):
        questions.append(question('housing',('Hai già trovato la tua sistemazione?','Have you found accommodation?'),[
            ('searching',('Sto cercando','Still searching')),('found',('Ho una sistemazione','I have accommodation')),('unknown',('Da verificare','To check'))],lang,
            ('Con una casa già trovata, passi ai controlli sul contratto e ai documenti abitativi.','With accommodation found, focus on the contract and housing evidence.')))
    if relevant(['taxcode','bank','phone','residence','temporary','identity']):
        questions.append(question('taxcode',('Hai già un codice fiscale italiano?','Do you already have an Italian tax code?'),yes_no,lang,
            ('Se è già disponibile, togliamo i passaggi per richiederlo. Non scrivere il codice.','If already available, remove application steps. Do not enter the code.')))
    if relevant(['residence','temporary','identity']):
        questions.append(question('residence_status',('Sei già residente anagraficamente a Milano?','Are you already registered as a Milan resident?'),[
            ('milan',('Sì, residente a Milano','Yes, registered in Milan')),('elsewhere',('No, la residenza è altrove','No, registered elsewhere')),('unknown',('Da verificare','To check'))],lang,
            ('Residenza e abitare temporaneamente in città sono cose diverse.','Registered residence and temporarily living in the city are different.')))
        if p.get('residence_status') != 'milan':
            opts=[('undecided',('Devo ancora capire le opzioni','I need to compare the options')),('keep',('Vorrei mantenere la residenza attuale','I would like to keep my existing residence'))]
            if p['citizenship']=='italian' or (p['citizenship']=='eu' and p.get('stay_duration')!='year-plus'):
                opts.append(('temporary',('Vorrei chiedere il domicilio/registrazione temporanea','I would like temporary domicile/registration')))
            opts.append(('transfer',('Vorrei trasferire la residenza','I would like to transfer residence')))
            questions.append(question('residence_intent',('Che scelta vuoi valutare sulla residenza?','Which residence option do you want to consider?'),opts,lang,
                ('La scelta cambia servizi e checklist, e si verifica con il Comune. Puoi rivederla durante il percorso.','Your choice changes services and checklists and needs checking with the City. You can revise it in the journey.')))
        questions.append(question('digital_id',('Hai SPID o una CIE utilizzabile online?','Do you have SPID or an ID card usable online?'),yes_no,lang,
            ('Adattiamo il canale di accesso: servizio online o contatto per le alternative.','Adapt access: the online service or help with alternatives.')))
        questions.append(question('grant',('Hai una borsa di studio o dubbi su borsa e ISEE?','Do you have a study grant or questions about grants and ISEE?'),yes_no,lang,
            ('Se pertinente, prima della scelta inseriamo il contatto con il diritto allo studio.','When relevant, contact student aid before deciding.')))
    if relevant(['health']):
        questions.append(question('health_coverage',('Hai già verificato la tua copertura sanitaria per il soggiorno?','Have you checked your healthcare coverage for this stay?'),yes_no,lang,
            ('Una copertura già verificata sposta il piano verso l’accesso alle cure. Non chiediamo informazioni mediche.','Checked coverage moves the plan towards accessing care. No medical details are requested.')))
    missing=[q for q in questions if p.get(q['key']) is None]
    if not p.get('citizenship_confirmed'):
        missing.insert(0,question('citizenship',('Quale cittadinanza deve seguire il piano?','Which citizenship route should the plan follow?'), [('italian',('Italiana','Italian')),('eu',('UE','EU')),('non-eu',('Non UE','Non-EU')),('international',('Da verificare','To check'))],lang,('Non deduciamo la cittadinanza dal nome o dalla lingua.','We do not infer citizenship from a name or language.')))
    return missing


def adaptive_cards(profile, blocks, residence_choice=None, suppressed=()):
    """Return active source-based cards, with explicit explanations for changes."""
    p=profile; lang=p['language']; say=lambda it,en:text(lang,it,en)
    catalog={j['id']:deepcopy(j) for j in localized(lang,p['citizenship'])}
    ids=list(blocks); explanations={}; excluded=[]
    italian=p['citizenship']=='italian'; eu=p['citizenship']=='eu'; non_eu=p['citizenship']=='non-eu'
    choice=residence_choice or p.get('residence_intent') or 'undecided'
    duration=p.get('stay_duration')
    short=duration=='short'; long=duration=='year-plus'
    residence_needed=bool({'arrival','residence','temporary','identity'} & set(blocks))
    route_choice=None
    def note(id,it,en): explanations[id]=say(it,en)
    def remove(id,it,en):
        if id in ids:
            ids.remove(id); excluded.append({'id':id,'title':catalog[id]['title'],'reason':say(it,en)})
    def add(id,it,en):
        if id not in ids and id not in suppressed: ids.append(id)
        note(id,it,en)
    def update(id,sid,**kwargs):
        s=next((s for s in catalog[id]['steps'] if s['id']==sid),None)
        if s: s.update(kwargs)
    def keep_steps(id,names): catalog[id]['steps']=[s for s in catalog[id]['steps'] if s['id'] in names]
    def new_step(id,title,body,source,checks,owner):
        return dict(id=id,title=say(*title),body=say(*body),source=source,checklist=[say(*c) for c in checks],owner=say(*owner))

    # Arrival is a routing block, not a duplicate of all the detailed service cards.
    if 'arrival' in ids:
        orientation=new_step('orientation',('Il tuo arrivo, con le informazioni che hai dato','Your arrival, based on your answers'),
            ('Rivedi durata del soggiorno, sistemazione e documenti nel riepilogo del profilo. I servizi qui sotto seguono queste risposte; se un’informazione è incerta, trovi un controllo con l’ufficio competente.',
             'Review stay duration, accommodation and documents in your profile summary. Services below follow those answers; uncertain information leads to a check with the relevant office.'),DESK,
            [('Ho riletto il profilo e so quali informazioni verificare','I reviewed my profile and know which answers need checking')],('YesMilano · Student Desk','YesMilano · Student Desk'))
        catalog['arrival']['steps']=[orientation]
        catalog['arrival']['subtitle']=say('Il punto di partenza per i servizi del tuo caso.','A starting point for services matching your situation.')
        for id in ['housing','transport','health']:
            add(id,'Incluso nel piano di arrivo per organizzare la vita quotidiana.','Included in your arrival plan for everyday student life.')
        if p.get('taxcode')!='yes': add('taxcode','Il codice fiscale non risulta ancora disponibile o verificato.','Your tax code is not yet available or checked.')
        if non_eu:
            if p['stage']=='arriving': add('visa','Prima del viaggio, verifica l’ingresso per il tuo soggiorno.','Before travel, check entry for your stay.')
            add('permit','Adatta i documenti di soggiorno alla durata e allo stato della richiesta.','Match stay documents to duration and application status.')

    # Add decision support before the relevant municipal services.
    if residence_needed and p.get('residence_status')!='milan':
        if 'arrival' not in ids:
            ids.insert(0,'arrival');catalog['arrival']['steps']=[]
        if p.get('grant') in {'yes','unknown'}:
            study=deepcopy(localized(lang,'italian')[0]['steps'][0])
            study['body']=say('Hai indicato una borsa o un dubbio da chiarire. Prima di decidere su domicilio o residenza, verifica il tuo bando e l’ISEE con il diritto allo studio dell’università; il piano non determina l’idoneità.',
                'You reported a grant or an open question. Before deciding about domicile or residence, check your call and ISEE with university student aid; the plan does not determine eligibility.')
            catalog['arrival']['steps'].append(study)
        if italian or eu:
            decision=deepcopy(localized(lang,'italian')[0]['steps'][1]);decision['id']='giulia-status'
            decision['body']=say('Confronta la scelta indicata nel profilo con le fonti del Comune. Mantenere la residenza, chiedere una registrazione temporanea e trasferire la residenza portano a servizi e controlli diversi. Scegli qui l’opzione da verificare: il resto del piano si aggiorna.',
                'Compare your profile choice with City sources. Keeping residence, temporary registration and transferring residence lead to different services and checks. Choose the option to verify here: the rest of the plan updates.')
            decision['source']=DOMICILE if italian else catalog['temporary']['guide_url']
            if eu:
                decision['choices'][1]['body']=say('Verifica la registrazione UE e la durata del soggiorno con l’Anagrafe.','Check EU registration and stay duration with the Registry.')
            if eu and long:
                decision['body']+=say(' Per la durata di un anno o più, la guida temporanea UE descrive un caso diverso: verifica la registrazione pertinente con l’Anagrafe prima di usare un modulo.',' For one year or longer, the EU temporary guide describes a different case: check the appropriate registration with the Registry before using a form.')
                decision['choices']=[c for c in decision['choices'] if c['id']!='temporary']
                if choice=='temporary': choice='undecided'
            catalog['arrival']['steps'].append(decision);route_choice='arrival--giulia-status'
        if choice=='temporary' and (italian or eu):
            remove('residence','Hai scelto la registrazione temporanea: togliamo la richiesta di trasferimento.','You chose temporary registration: remove the residence-transfer application.')
            add('temporary','Incluso per la tua scelta di domicilio/registrazione temporanea.','Included because you chose temporary domicile/registration.')
        elif choice=='transfer':
            remove('temporary','Hai scelto di trasferire la residenza: togliamo la richiesta temporanea.','You chose to transfer residence: remove the temporary application.')
            add('residence','Incluso per la tua scelta di trasferimento della residenza.','Included because you chose to transfer residence.')
        else:
            remove('temporary', 'La guida temporanea UE riguarda soggiorni inferiori a un anno: verifica un canale per la durata indicata.' if eu and long else 'Non hai scelto di presentare una richiesta temporanea.', 'The EU temporary guide covers stays under one year: check a route for your stated duration.' if eu and long else 'You have not chosen to submit a temporary application.')
            remove('residence','La scelta va chiarita prima di presentare una richiesta di trasferimento.','Clarify your choice before submitting a residence-transfer application.')
            if choice=='keep':
                catalog['arrival']['steps'].append(new_step('keep-residence',('Mantieni la residenza: verifica gli adempimenti','Keep residence: check the relevant formalities'),
                    ('Hai scelto di mantenere la residenza attuale. Chiarisci con l’Anagrafe gli adempimenti per la tua situazione e conserva le indicazioni. Il piano non include dichiarazioni da firmare per il domicilio temporaneo né una richiesta ANPR.',
                     'You chose to keep your current residence. Clarify applicable formalities with the Registry and keep its guidance. This plan includes neither a temporary-domicile declaration nor an ANPR transfer application.'),ITALIAN_RESIDENCE if italian else catalog['residence']['guide_url'],
                    [('Ho verificato la mia scelta con l’Anagrafe','I checked my choice with the Registry'),('Ho conservato le indicazioni ricevute','I kept the guidance received')],('Comune · Anagrafe','City · Registry')))
            elif not (italian or eu):
                catalog['arrival']['steps'].append(new_step('registry-contact',('Chiarisci la tua situazione anagrafica','Clarify your registration situation'),
                    ('La registrazione temporanea UE non si applica automaticamente al tuo profilo. Contatta l’Anagrafe o lo Student Desk per verificare il canale con i tuoi documenti di soggiorno.',
                     'EU temporary registration does not automatically apply to your profile. Contact the Registry or Student Desk to check the route for your stay documents.'),catalog['residence']['guide_url'],
                    [('Ho chiarito con l’ufficio il canale per il mio caso','I clarified the route for my case with the office')],('Comune · Anagrafe / Student Desk','City · Registry / Student Desk')))
    elif p.get('residence_status')=='milan':
        remove('residence','Hai dichiarato di essere già residente a Milano: evitiamo una nuova iscrizione.','You reported already being registered in Milan: avoid a new registration.')
        remove('temporary','Il domicilio temporaneo per fuorisede non è una nuova iscrizione per chi è già residente.','Temporary registration is not a new registration for an existing Milan resident.')

    if non_eu and 'residence' in ids and p.get('permit')!='valid':
        add('permit','Prima della pratica anagrafica, verifica i documenti di soggiorno e il loro stato.','Before the Registry application, check stay documents and their status.')

    # Nationality and length select the source route, not legal entitlement.
    if italian or eu:
        for id in ['visa','permit']:
            remove(id,'Il tuo profilo non è quello della guida per studenti non UE.','Your profile does not match the non-EU student guide.')
    elif not non_eu:
        for id in ['visa','permit']:
            if id in ids:
                keep_steps(id,{'route'})
                update(id,'route',body=say('La cittadinanza non è verificata: contatta oggi università o Student Desk per chiarire la procedura applicabile e i termini in base all’ingresso in Italia. Per il kit chiedi quale indirizzo temporaneo reale indicare e come aggiornare i documenti quando cambi alloggio; il domicilio del kit è diverso dalla residenza anagrafica. Non aspettare una casa definitiva per verificare le scadenze.',
                    'Citizenship is not checked: contact your university or Student Desk today to clarify the applicable procedure and deadlines based on entry into Italy. For a kit, ask which actual temporary address to use and how to update documents after moving; kit domicile is distinct from municipal residence registration. Do not wait for permanent housing to check deadlines.'),
                    checklist=[say('Ho chiarito cittadinanza, procedura e scadenze con il servizio competente','I clarified citizenship, procedure and deadlines with the competent service'),say('Ho verificato indirizzo temporaneo e aggiornamenti dei documenti','I checked the temporary address and document updates')])
                note(id,'Cittadinanza incerta: manteniamo un controllo urgente anziché escludere il servizio.','Citizenship uncertain: keep an urgent check rather than exclude the service.')
    if non_eu and 'visa' in ids:
        if p.get('country') and p['country'] not in {'unknown','da verificare','to check'}:
            update('visa','route',body=catalog['visa']['steps'][0]['body']+say(' Sul portale ufficiale usa il Paese di cittadinanza indicato: ',' On the official portal use your stated citizenship country: ')+p['country']+'.')
        update('visa','route',extra_sources=[{'url':'https://vistoperitalia.esteri.it/home.aspx','title':say('Verifica per Paese sul portale Visto per l’Italia','Country-specific check on the Visa for Italy portal')}])
        if p['stage']=='here' or p.get('visa')=='yes':
            keep_steps('visa',{'route'})
            update('visa','route',title=say('Verifica il documento d’ingresso che hai già','Check the entry document you already have'),
                   body=say('Non ripresentare una domanda di visto solo per completare il piano. Verifica tipo, validità e condizioni del tuo documento con il consolato o l’università.',
                            'Do not submit another visa application just to finish this plan. Check your document type, validity and conditions with the consulate or university.'),
                   checklist=[say('Ho verificato il documento d’ingresso e il referente per i dubbi','I checked my entry document and support contact')])
            note('visa','Hai già il visto o sei già arrivato: resta solo la verifica del documento.','You have a visa or already arrived: only document verification remains.')
        if short:
            keep_steps('visa',{'route'})
            update('visa','route',source=SHORT_STAY,title=say('Verifica ingresso per studio fino a 90 giorni','Check study entry for up to 90 days'),
                body=say('Per il soggiorno breve indicato, verifica sul portale del Ministero e con il consolato se serve un visto nel tuo caso. Usa Paese di cittadinanza, residenza e motivo del viaggio sul servizio ufficiale.',
                         'For your stated short stay, check the Ministry portal and consulate about visa requirements for your case. Use citizenship country, residence and purpose on the official service.'),
                checklist=[say('Ho verificato con la fonte i requisiti del mio soggiorno breve','I checked short-stay requirements with the source')])
    if non_eu and 'permit' in ids:
        if short:
            catalog['permit']['title']=say('Il soggiorno breve per studio.','A short study stay.')
            catalog['permit']['steps']=[new_step('short-stay',('Verifica la dichiarazione di presenza','Check the declaration of presence'),
                ('Hai indicato un soggiorno fino a 90 giorni. Segui la sezione studio per soggiorni brevi del Ministero: verifica con Questura o università la dichiarazione di presenza e le modalità legate al tuo ingresso. Non usare il kit per lungo soggiorno come percorso automatico.',
                 'You stated a stay up to 90 days. Follow the Ministry short-study-stay section: check the declaration of presence and entry-specific process with the Police or university. Do not automatically follow the long-stay kit process.'),SHORT_STAY,
                [('Ho verificato la procedura per il mio ingresso e durata','I checked the process for my entry and duration'),('Ho gestito la dichiarazione o verificato come viene assolta','I handled the declaration or checked how it is fulfilled')],('Questura / Università','Police / University'))]
            note('permit','La durata fino a 90 giorni cambia la guida: soggiorno breve anziché kit per lungo soggiorno.','Up to 90 days changes the route: short-stay guidance instead of the long-stay kit.')
        elif duration in {None,'unknown'}:
            keep_steps('permit',{'route'})
            update('permit','route',body=say('La durata non è ancora verificata. Chiarisci con l’università e l’autorità competente quale procedura di soggiorno si applica prima di preparare il kit.',
                'Stay duration is not yet checked. Clarify the applicable stay process with your university and the competent authority before preparing a kit.'),checklist=[say('Ho chiarito durata e procedura con il servizio competente','I clarified duration and procedure with the competent service')])
        elif p.get('permit')=='pending':
            catalog['permit']['steps']=[new_step('follow-up',('Segui la richiesta già presentata','Follow your submitted application'),
                ('Hai già presentato la richiesta e hai la ricevuta: non preparare un secondo kit. Verifica convocazione in Questura, documenti da portare e canale per seguire il rilascio.',
                 'You already submitted and have the receipt: do not prepare a second kit. Check the Police appointment, documents to bring and the issuance follow-up channel.'),catalog['permit']['guide_url'],
                [('Ho controllato ricevuta e convocazione','I checked my receipt and appointment'),('So come seguire il rilascio o chiedere assistenza','I know how to follow issuance or ask for support')],('Questura / Università','Police / University'))]
            note('permit','La richiesta è già presentata: passaggi per seguire il rilascio, nessun nuovo kit.','Application submitted: follow-up steps, no new kit.')
        elif p.get('permit')=='valid':
            catalog['permit']['steps']=[new_step('validity',('Verifica validità e prossime scadenze','Check validity and next deadlines'),
                ('Hai dichiarato un permesso italiano valido. Controlla durata e condizioni rispetto ai tuoi studi, e verifica con il servizio competente quando e come gestire eventuali rinnovi. Non ripresentare una prima richiesta.',
                 'You reported a valid Italian permit. Check validity and conditions against your studies and ask the competent service about any renewal timing and process. Do not submit a first application again.'),catalog['permit']['guide_url'],
                [('Ho verificato validità e riferimento per il rinnovo','I checked validity and the renewal contact')],('Questura / Università','Police / University'))]
            note('permit','Hai già un permesso valido: controlli sulla validità, non sul primo rilascio.','You have a valid permit: validity checks, not a first application.')
        elif p.get('permit')=='unknown':
            keep_steps('permit',{'route'})
            update('permit','route',checklist=[say('Ho chiarito stato della richiesta e prossima azione con l’ufficio','I clarified application status and next action with the office')])

    if p.get('taxcode')=='yes':
        if 'taxcode' in ids and p.get('taxcode_document')=='missing':
            catalog['taxcode']['steps']=[new_step('certificate',('Recupera il certificato del codice già assegnato','Get the certificate for your existing tax code'),
                ('Hai già un codice fiscale ma ti manca il documento ufficiale. Chiedi all’università o all’Agenzia delle Entrate come recuperare il certificato di attribuzione del codice esistente, senza richiedere un nuovo codice. Verifica con il locatore quale documento accetta.',
                 'You already have a tax code but lack the official document. Ask your university or the Revenue Agency how to obtain the certificate of assignment for the existing code, without applying for a new code. Check which document the landlord accepts.'),catalog['taxcode']['guide_url'],
                [('Ho verificato come ottenere il certificato del codice esistente','I checked how to obtain the certificate for my existing code'),('Ho chiarito il documento richiesto dal locatore','I clarified the document requested by the landlord')],('Agenzia delle Entrate / Università','Revenue Agency / University'))]
            note('taxcode','Il codice esiste: serve il certificato, non una nuova attribuzione.','The code exists: get the certificate, not a new assignment.')
        else:
            remove('taxcode','Hai già il codice fiscale: evitiamo una nuova richiesta.','You already have a tax code: avoid applying again.')
    elif {'bank','phone','temporary','residence'} & set(ids) and p.get('taxcode')=='no':
        add('taxcode','Hai indicato che manca il codice fiscale: verifica il documento richiesto dagli altri servizi.','You lack a tax code: check the document requested by other services.')
    if 'taxcode' in ids and p.get('taxcode')=='unknown':
        keep_steps('taxcode',{'existing'})
        update('taxcode','existing',body=say('Non è certo se il codice sia già assegnato. Verifica con università o Agenzia delle Entrate: se esiste, chiedi come ottenere il certificato ufficiale; se non esiste, verifica il canale per la prima richiesta e aggiorna il profilo. Non avviare un’attribuzione duplicata.',
            'It is unclear whether a code was assigned. Check with your university or the Revenue Agency: if it exists, ask how to obtain the official certificate; otherwise check the first-application channel and update your profile. Do not request a duplicate assignment.'),
            checklist=[say('Ho chiarito se il codice è già assegnato e quale documento mi serve','I clarified whether a code was assigned and which document I need')])
    if 'housing' in ids and p.get('housing')=='found':
        keep_steps('housing',{'contract','deposit','handover'})
        note('housing','Casa già trovata: saltati ricerca e visita, restano contratto e adempimenti.','Accommodation found: skip search and viewing, keep contract and formalities.')
    if 'housing' in ids:
        suffix=say(' Confronta la durata del contratto con il soggiorno indicato nel profilo.',' Compare contract length with your stated stay.')
        update('housing','contract',body=next(s['body'] for s in catalog['housing']['steps'] if s['id']=='contract')+suffix,
               checklist=[say('Ho confrontato durata del contratto e durata del soggiorno','I compared contract length with stay duration'),say('Ho chiarito le clausole con il referente della casa','I clarified clauses with the housing contact')])
    if 'health' in ids and italian:
        update('health','access',body=say('Per gli studi fuori sede, individua ATS/ASST o il servizio sanitario competente e verifica come accedere alle cure a Milano. Non applicare a te i passaggi della guida per studenti non UE.', 'For study away from home, identify ATS/ASST or the competent health service and check how to access care in Milan. Do not apply non-EU student procedures to yourself.'), owner=say('ATS / ASST · assistenza fuori sede','ATS / ASST · care away from home'), checklist=[say('Ho verificato con il servizio sanitario l’accesso alle cure come studente fuorisede','I checked healthcare access as a student away from home with the health service')])
    if 'health' in ids and p.get('health_coverage')=='yes':
        keep_steps('health',{'access','next'});note('health','Copertura già verificata: il percorso riguarda l’accesso alle cure.','Coverage checked: focus on accessing care.')
    if 'temporary' in ids:
        if not (italian or eu): remove('temporary','La guida temporanea UE non è una procedura per il profilo indicato.','EU temporary guidance is not a procedure for your profile.')
        elif eu and long:
            catalog['temporary']['steps']=[new_step('duration-check',('Verifica la registrazione per un anno o più','Check registration for one year or longer'),
                ('La guida temporanea UE si rivolge a soggiorni inferiori a un anno. Hai indicato una durata più lunga: chiarisci con l’Anagrafe quale registrazione si applica prima di usare quel modulo.',
                 'The EU temporary guide addresses stays under one year. You stated a longer stay: clarify the appropriate registration with the Registry before using that form.'),catalog['temporary']['guide_url'],
                [('Ho chiarito con l’Anagrafe il canale per la durata indicata','I clarified the route for my stated duration with the Registry')],('Comune · Anagrafe','City · Registry'))]
        elif italian:
            update('temporary','route',body=say('Hai scelto il domicilio temporaneo mantenendo la residenza d’origine. Verifica la FAQ del Comune per studenti fuorisede: la richiesta è diversa dal trasferimento della residenza.',
                'You chose temporary student domicile while retaining existing residence. Check the City FAQ for students away from home: this differs from transferring residence.'),checklist=[say('Ho verificato il domicilio temporaneo nella FAQ del Comune','I checked temporary domicile in the City FAQ')])
            update('temporary','prepare',body=say('Prepara fuori dall’app la dichiarazione firmata indicata dalla FAQ e il documento di identità. Puoi chiedere una bozza con segnaposti; completa i dati solo fuori da StudiaMI.',
                'Prepare the signed declaration and ID described by the FAQ outside the app. You can request a placeholder draft; fill details outside StudiaMI.'),
                checklist=[say('Ho preparato e controllato la dichiarazione da firmare fuori dall’app','I prepared and checked the declaration to sign outside the app'),say('Ho verificato il documento da allegare','I checked the ID attachment')],draft=True)
            update('temporary','send',checklist=[say('Ho firmato e inviato la richiesta sul contatto ufficiale','I signed and sent through the official contact'),say('Ho conservato risposta o protocollo e verificato la durata','I kept the reply or reference and checked duration')])
    if 'residence' in ids:
        if non_eu:
            source=VALID_PERMIT if p.get('permit')=='valid' else catalog['residence']['guide_url']
            update('residence','documents',source=source,body=say('Per il titolo di soggiorno indicato, verifica con l’Anagrafe la procedura. Con permesso valido controlla passaporto, permesso e codice fiscale; con la sola ricevuta chiarisci il canale prima di presentare la richiesta. Gli atti familiari non sono automaticamente necessari per l’iscrizione in sé.',
                'Check the Registry procedure for your stated stay document. With a valid permit check passport, permit and tax code; with a receipt clarify the channel before applying. Family records are not automatically required for registration itself.'),
                checklist=[say('Ho verificato il canale per il mio titolo di soggiorno','I checked the route for my stay document'),say('Ho verificato documenti di identità, soggiorno e casa pertinenti','I checked relevant identity, stay and housing documents')],extra_sources=[{'url':LEASE,'title':say('Documentazione abitativa per affitto','Rental housing evidence')}])
        if p.get('digital_id')=='yes' and italian:
            update('residence','access',source=ITALIAN_RESIDENCE,body=say('Hai indicato SPID o CIE utilizzabile online. Per il trasferimento della residenza verifica e usa il servizio ANPR collegato dalla fonte del Comune.',
                'You reported SPID or an ID card usable online. Check and use the ANPR residence-transfer service linked by the City source.'),checklist=[say('Ho verificato accesso al servizio ANPR con le mie credenziali','I checked ANPR access with my credentials')])
        elif p.get('digital_id') in {'no','unknown'}:
            update('residence','access',body=say('Non risulta un’identità digitale utilizzabile. Chiedi all’Anagrafe o allo Student Desk il canale o l’assistenza per il tuo caso prima di procedere; non devi ottenere SPID solo per spuntare questo piano.',
                'No usable digital identity is confirmed. Ask the Registry or Student Desk about the route or support for your case before proceeding; you do not need SPID just to tick this plan.'),checklist=[say('Ho contattato il servizio per verificare un canale accessibile','I contacted the service to check an accessible route')])
    for id in ['bank','phone']:
        if id in ids and p.get('taxcode')=='yes':
            update(id,'documents',body=say('Hai già il codice fiscale. Verifica gli altri documenti e il canale direttamente con il servizio; il piano non include una nuova richiesta del codice.',
                'You already have a tax code. Check other documents and the channel with the provider; this plan does not include another tax-code application.'),checklist=[say('Ho verificato gli altri documenti con il servizio, usando il codice già disponibile','I checked other documents with the provider, using my existing tax code')])
    if 'bank' in ids and non_eu:
        document=say('la ricevuta della richiesta già presentata','the receipt of your submitted application') if p.get('permit')=='pending' else say('il permesso italiano valido','your valid Italian permit') if p.get('permit')=='valid' else say('i documenti di soggiorno pertinenti al tuo caso','the stay documents relevant to your case')
        update('bank','documents',body=say('La guida bancaria elenca documento di identità, codice fiscale e permesso o ricevuta, se pertinenti. Hai indicato: ','The banking guide lists ID, tax code and a permit or receipt when applicable. Your stated situation calls for checking: ')+document+say('. Verifica direttamente con la banca i documenti accettati e il canale: la checklist non garantisce l’apertura del conto.','. Check accepted documents and access directly with the bank: this checklist does not guarantee account opening.'),
               checklist=[say('Ho verificato documento di identità e codice fiscale con la banca','I checked ID and tax code with the bank'),say('Ho verificato con la banca ','I checked with the bank ')+document])
        note('bank','La checklist usa lo stato dei tuoi documenti di soggiorno e richiede la verifica con la banca.','The checklist uses your stay-document status and requires checking with the bank.')
    for id in suppressed:
        remove(id,'Blocco rimosso da te: verifica comunque obblighi e scadenze con il servizio competente.','Block removed by you: still check obligations and deadlines with the competent service.')
    ids=[id for id in dict.fromkeys(ids) if catalog[id]['steps']]
    # Keep municipal decision and urgent stay checks ahead of dependent services.
    rank=lambda id: 0 if id=='arrival' else 1 if id=='visa' and p['stage']=='arriving' else 2 if id=='permit' else 3 if id=='taxcode' else 4 if id in {'temporary','residence'} and p.get('housing')=='found' else 5
    ids=sorted(ids,key=rank)
    for id in ids:
        catalog[id]['order_locked']=rank(id)<5
        catalog[id]['personalization_reason']=explanations.get(id,say('Incluso per l’obiettivo che hai scelto, con controlli adattati al profilo.','Included for your chosen goal, with checks adapted to your profile.'))
        for s in catalog[id]['steps']:
            s.setdefault('owner',say('Servizio indicato nella guida','Service listed in the guide'))
    return [catalog[id] for id in ids], excluded, route_choice, choice
