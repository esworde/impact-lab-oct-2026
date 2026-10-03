"use strict";
const COPY = {
  it: {
    skip: "Vai ai contenuti",
    skipFooter: "Vai al footer",
    lab: "Claude Impact Lab · Milano",
    city: "Esplora il sito del Comune ↗",
    journeys: "Percorsi",
    how: "Come funziona",
    sources: "Le fonti",
    openChat: "Apri la chat",
    kicker: "STUDENT LIFE, MADE SIMPLE",
    hero1: "La tua nuova vita,",
    hero2: "comincia a Milano.",
    heroDescription:
      "Raccontaci la tua situazione o rispondi a poche domande. Adattiamo servizi, passaggi e checklist al tuo caso.",
    askPlaceholder: "Sto per trasferirmi a Milano. Da dove inizio?",
    suggestHousing: "Cerco una stanza",
    suggestDocuments: "Mi servono i documenti",
    suggestArrival: "Sto per arrivare",
    yourJourney: "IL TUO PERCORSO",
    startWhere: "Da dove vuoi partire?",
    journeysIntro:
      "Scegli un obiettivo. Al resto pensiamo un passo alla volta.",
    personalize: "Personalizza per te",
    italian: "Studente italiano",
    international: "Studente internazionale",
    arriving: "Sto arrivando",
    alreadyHere: "Sono già qui",
    citizenshipNote: "Per i documenti, quale percorso ti riguarda?",
    eu: "Cittadinanza UE",
    nonEu: "Cittadinanza non UE",
    unsure: "Da verificare",
    lessSearching: "MENO RICERCHE. PIÙ CHIAREZZA.",
    oneStep: "Una cosa alla volta.\nUn posto solo.",
    how1Title: "Crea il tuo percorso",
    how1Body:
      "Racconta la tua situazione o rispondi a poche domande. Rivedi le card proposte e scegli l’ordine.",
    how2Title: "Segui i passaggi",
    how2Body:
      "Checklist, indicazioni e link ai servizi. Sai sempre cosa viene dopo.",
    how3Title: "Chiedi, quando vuoi",
    how3Body: "L’assistente conosce il passo in cui sei e ti aiuta a capirlo.",
    footerDescription: "La tua vita da studente, un passo alla volta.",
    prototype: "Prototipo indipendente · Claude Impact Lab Milano 2026",
    privacy: "Privacy",
    floatingPlaceholder: "Chiedi a StudiaMI…",
    personalData: "Non inserire dati personali.",
    chatSubtitle: "Un aiuto per la tua vita a Milano.",
    chatWelcome: "Ciao, da dove cominciamo?",
    chatWelcomeBody:
      "Puoi chiedermi dei primi passi a Milano o approfondire il percorso che stai seguendo.",
    yourQuestion: "La tua domanda",
    chatPlaceholder: "Scrivi la tua domanda…",
    chatNote:
      "Le informazioni vanno verificate alla fonte. Non inserire dati personali.",
    clearChat: "Nuova chat",
    steps: "passi",
    stepSingular: "passo",
    startPath: "Esplora il percorso",
    resumePath: "Riprendi il percorso",
    home: "Home",
    breadcrumb: "Percorso di navigazione",
    editProfile: "Modifica profilo",
    progress: "Passaggi validati da te",
    step: "PASSO",
    of: "DI",
    officialSource: "LA FONTE PER QUESTO PASSAGGIO",
    readGuide: "Apri la guida",
    checklist: "La tua checklist",
    checklistNote:
      "Spunta ciò che hai verificato. Non equivale all’invio di una pratica.",
    needHelp: "Un dubbio su questo passaggio?",
    helpStep: "Chiedi a StudiaMI",
    previous: "Indietro",
    next: "Passo successivo",
    summary: "Vedi riepilogo",
    summaryTitle: "Il tuo percorso, a colpo d’occhio.",
    summaryBody:
      "Tieni traccia di quello che hai verificato e torna sui passaggi ancora aperti. Le pratiche si completano sui servizi ufficiali.",
    verified: "Validato da te",
    toVerify: "Da verificare",
    download: "Scarica la checklist",
    backHome: "Esplora altri percorsi",
    thinking: "Consulto le guide…",
    usedSources: "FONTI CONSULTATE",
    fetched: "Recuperata il",
    updated: "Aggiornamento dichiarato",
    openSuggested: "Apri il percorso",
    profileTitle: "Un percorso che parte da te.",
    profileBody:
      "Scegli il profilo per adattare i passaggi. Puoi cambiarlo in qualsiasi momento.",
    intlTitle: "Quale percorso internazionale?",
    intlBody:
      "Questa scelta serve ad adattare i passaggi sui documenti. Non determina la tua idoneità a un servizio.",
    privacyTitle: "Solo quello che serve.",
    privacyBody:
      "Non chiediamo un account. Profilo generico, blocchi del percorso, scelte, checklist e conferme rimangono nel tuo browser. Il racconto per comporre un percorso viene inviato a Claude e non viene salvato nel piano. La conversazione resta in memoria nella pagina e scompare ricaricandola; non viene salvata nel nostro database. Per rispondere, domanda e contesto vengono inviati a Claude (Anthropic), secondo le sue condizioni di trattamento. Non scrivere nomi, indirizzi, documenti o informazioni mediche.",
    sourceIntro:
      "YesMilano è la fonte principale. Le guide del Comune di Milano e del Ministero degli Affari Esteri completano le istruzioni dei servizi competenti. La data di recupero non indica necessariamente l’ultimo aggiornamento del contenuto.",
    loadError: "Non riesco a caricare i percorsi. Riprova tra poco.",
    chatUnavailable:
      "La chat è in attivazione. Intanto puoi seguire i percorsi e aprire tutte le fonti ufficiali.",
    chatError:
      "L’assistente non riesce a rispondere adesso. Riprova oppure consulta la fonte del passaggio.",
    chatLimit:
      "La chat ha raggiunto il limite di questa demo. I percorsi e le fonti restano disponibili.",
    retry: "Riprova",
    tryPersona: "PROVA UNA STORIA",
    catalogIntro: "15 casistiche, dalle guide How to di YesMilano.",
    catalogLink: "Esplora il catalogo originale ↗",
    groupBefore: "Prima di arrivare",
    groupBeforeBody:
      "Prepara il viaggio, i documenti e il tuo primo punto di appoggio.",
    groupFirst: "I primi passi a Milano",
    groupFirstBody: "Documenti, casa e servizi per iniziare la tua vita qui.",
    groupSettled: "Ora fai spazio alla tua vita qui",
    groupSettledBody: "Supporto, identità, lavoro e una nuova lingua.",
    guideLink: "Guida YesMilano",
    cases: "casistiche",
    giuliaDemo: "· studentessa fuorisede",
    rezaDemo: "· studente non UE",
    plan: "IL TUO PIANO",
    inspiredBy: "Un caso come",
    locked: "Bloccato",
    current: "Da validare",
    validatedStep: "Validato da te",
    validationTitle: "Prima di andare avanti",
    validationNote:
      "Spunta tutti i controlli, poi conferma questo passaggio. La conferma riguarda il tuo piano: non approva una pratica e non invia documenti.",
    validationReady: "Controlli completati. Ora puoi validare il passaggio.",
    validationMissing:
      "Completa tutti i controlli per sbloccare la validazione.",
    validateNext: "Conferma e sblocca il prossimo passo",
    validateFinish: "Conferma e apri il riepilogo",
    lockedNotice:
      "Prima valida il passaggio corrente per sbloccare quello successivo.",
    choiceTitle: "La scelta per il tuo piano",
    choiceRequired: "Scegli un’opzione e completa i controlli.",
    yourChoice: "La tua scelta confermata",
    owner: "CHI TI AIUTA",
    draft: "Prepara una bozza con StudiaMI",
    draftPrompt:
      "Prepara una bozza non ufficiale per la richiesta di domicilio temporaneo di una studentessa fuorisede come Giulia, basata sulla fonte del Comune KA-00595. Usa solo segnaposti, nessun dato personale. Indica cosa deve controllare e firmare lo studente, senza inviare nulla.",
    helpPrompt: "Aiutami con questo passaggio: ",
    saved: "Checklist salvata nel tuo browser.",
    close: "Chiudi",
    send: "Invia domanda",
    sourceError: "Le fonti non sono disponibili in questo momento.",
    context: "Stai seguendo",
    completed: "validati da te",
    questionHousing:
      "Sto cercando una stanza a Milano. Cosa devo controllare prima di firmare?",
    questionDocuments:
      "Sono uno studente a Milano. Quali documenti devo verificare per iniziare?",
    questionArrival:
      "Sto per arrivare a Milano per studiare. Da dove comincio?",
  },
  en: {
    skip: "Skip to content",
    skipFooter: "Skip to footer",
    lab: "Claude Impact Lab · Milan",
    city: "Explore the City website ↗",
    journeys: "Journeys",
    how: "How it works",
    sources: "Our sources",
    openChat: "Open chat",
    kicker: "STUDENT LIFE, MADE SIMPLE",
    hero1: "Your new chapter,",
    hero2: "starts in Milan.",
    heroDescription:
      "Tell us your situation or answer a few questions. We’ll adapt services, steps and checklists to your situation.",
    askPlaceholder: "I’m moving to Milan. Where do I start?",
    suggestHousing: "I need a room",
    suggestDocuments: "Help with paperwork",
    suggestArrival: "I’m arriving soon",
    yourJourney: "YOUR JOURNEY",
    startWhere: "Where would you like to start?",
    journeysIntro: "Choose a goal. We’ll take it one step at a time.",
    personalize: "Make it yours",
    italian: "Italian student",
    international: "International student",
    arriving: "Arriving soon",
    alreadyHere: "Already here",
    citizenshipNote: "Which document route is relevant to you?",
    eu: "EU citizenship",
    nonEu: "Non-EU citizenship",
    unsure: "Not sure yet",
    lessSearching: "LESS SEARCHING. MORE CLARITY.",
    oneStep: "One step at a time.\nAll in one place.",
    how1Title: "Create your journey",
    how1Body:
      "Tell your story or answer a few questions. Review the suggested cards and choose their order.",
    how2Title: "Follow the steps",
    how2Body:
      "Checklists, guidance and service links. Always know what comes next.",
    how3Title: "Ask whenever you need",
    how3Body:
      "Your assistant knows which step you’re on and helps you understand it.",
    footerDescription: "Your student life, one step at a time.",
    prototype: "Independent prototype · Claude Impact Lab Milano 2026",
    privacy: "Privacy",
    floatingPlaceholder: "Ask StudiaMI…",
    personalData: "Do not enter personal information.",
    chatSubtitle: "A hand with your new life in Milan.",
    chatWelcome: "Hello, where shall we start?",
    chatWelcomeBody:
      "Ask about your first steps in Milan, or get help with the journey you’re following.",
    yourQuestion: "Your question",
    chatPlaceholder: "Write your question…",
    chatNote:
      "Check information at the source. Do not enter personal information.",
    clearChat: "New chat",
    steps: "steps",
    stepSingular: "step",
    startPath: "Explore this journey",
    resumePath: "Continue your journey",
    home: "Home",
    breadcrumb: "Breadcrumb",
    editProfile: "Edit profile",
    progress: "Steps you confirmed",
    step: "STEP",
    of: "OF",
    officialSource: "THE SOURCE FOR THIS STEP",
    readGuide: "Open the guide",
    checklist: "Your checklist",
    checklistNote:
      "Tick what you have checked. This does not submit an application.",
    needHelp: "A question about this step?",
    helpStep: "Ask StudiaMI",
    previous: "Back",
    next: "Next step",
    summary: "View summary",
    summaryTitle: "Your journey, at a glance.",
    summaryBody:
      "Keep track of what you have checked and return to any open steps. Official applications are completed through the relevant services.",
    verified: "Confirmed by you",
    toVerify: "To check",
    download: "Download checklist",
    backHome: "Explore other journeys",
    thinking: "Checking the guides…",
    usedSources: "SOURCES CONSULTED",
    fetched: "Retrieved on",
    updated: "Stated update",
    openSuggested: "Open this journey",
    profileTitle: "A journey that starts with you.",
    profileBody:
      "Choose a profile to adapt the steps. You can change it at any time.",
    intlTitle: "Which international route?",
    intlBody:
      "This choice adapts the document steps. It does not determine eligibility for a service.",
    privacyTitle: "Just what you need.",
    privacyBody:
      "No account needed. Your generic profile, journey blocks, choices, checklists and confirmations stay in your browser. Your story is sent to Claude to suggest blocks and is not saved in the plan. The conversation stays in page memory and disappears when you reload; it is not saved in our database. To answer, your question and context are sent to Claude (Anthropic), subject to its data-processing terms. Do not enter names, addresses, documents or medical information.",
    sourceIntro:
      "YesMilano is the primary source. City of Milan and Ministry of Foreign Affairs guides complement instructions from the relevant services. Retrieval dates do not necessarily reflect the last content update.",
    loadError: "The journeys could not be loaded. Please try again shortly.",
    chatUnavailable:
      "Chat is being activated. You can still follow all the journeys and open official sources.",
    chatError:
      "The assistant cannot answer right now. Try again or open the source for this step.",
    chatLimit:
      "This demo’s chat limit has been reached. Journeys and sources remain available.",
    retry: "Try again",
    tryPersona: "TRY A STORY",
    catalogIntro: "15 cases, from YesMilano’s How to guides.",
    catalogLink: "Explore the original catalogue ↗",
    groupBefore: "Not yet in Milan",
    groupBeforeBody: "Prepare your trip, paperwork and first place to stay.",
    groupFirst: "First steps in Milan",
    groupFirstBody: "Documents, housing and services to begin your life here.",
    groupSettled: "Getting settled",
    groupSettledBody: "Support, identity, work and a new language.",
    guideLink: "YesMilano guide",
    cases: "cases",
    giuliaDemo: "· Italian student away from home",
    rezaDemo: "· non-EU student",
    plan: "YOUR PLAN",
    inspiredBy: "A case like",
    locked: "Locked",
    current: "Awaiting your confirmation",
    validatedStep: "Confirmed by you",
    validationTitle: "Before you move on",
    validationNote:
      "Tick every check, then confirm this step. Confirmation applies to your plan: it does not approve applications or send documents.",
    validationReady: "Checks complete. You can now confirm this step.",
    validationMissing: "Complete every check to enable confirmation.",
    validateNext: "Confirm and unlock the next step",
    validateFinish: "Confirm and view the summary",
    lockedNotice: "Confirm the current step before unlocking the next one.",
    choiceTitle: "Your plan choice",
    choiceRequired: "Choose an option and complete the checks.",
    yourChoice: "Your confirmed choice",
    owner: "WHO CAN HELP",
    draft: "Prepare a draft with StudiaMI",
    draftPrompt:
      "Prepare an unofficial draft for temporary student domicile for an Italian student like Giulia, based on City source KA-00595. Use placeholders only, no personal data. Explain what the student must check and sign; do not send anything.",
    helpPrompt: "Help me with this step: ",
    saved: "Checklist saved in your browser.",
    close: "Close",
    send: "Send question",
    sourceError: "Sources are unavailable right now.",
    context: "Your current journey",
    completed: "confirmed by you",
    questionHousing:
      "I’m looking for a room in Milan. What should I check before signing?",
    questionDocuments:
      "I am a student in Milan. Which documents should I check to get started?",
    questionArrival: "I’m moving to Milan to study. Where do I start?",
  },
};
const ART = {
  passport:
    '<ellipse cx="120" cy="143" rx="65" ry="4" fill="#000" opacity=".06"/><g transform="rotate(-8 120 80)"><rect x="80" y="23" width="83" height="111" rx="8" fill="currentColor"/><path d="M90 24v109" stroke="#fff" opacity=".2" stroke-width="2"/><circle cx="123" cy="68" r="24" fill="none" stroke="#fff7e9" stroke-width="2"/><ellipse cx="123" cy="68" rx="11" ry="24" fill="none" stroke="#fff7e9" stroke-width="1.5"/><path d="M99 68h48M104 56h38M105 80h36M107 109h33M112 116h23" stroke="#fff7e9" stroke-width="2"/></g>',
  bank: '<ellipse cx="120" cy="143" rx="80" ry="4" fill="#000" opacity=".06"/><path d="m45 61 75-36 75 36z" fill="currentColor"/><rect x="42" y="127" width="156" height="10" rx="3" fill="currentColor"/><path d="M65 69v49M100 69v49M140 69v49M175 69v49" stroke="currentColor" stroke-width="12"/><circle cx="188" cy="111" r="22" fill="#fffaf0" stroke="currentColor" stroke-width="2"/><path d="M194 100c-12-7-20 13-7 20m-12-12h16m-17 6h16" stroke="currentColor" fill="none" stroke-width="2"/>',
  phone:
    '<ellipse cx="120" cy="143" rx="59" ry="4" fill="#000" opacity=".06"/><rect x="85" y="20" width="70" height="115" rx="13" fill="currentColor"/><rect x="91" y="32" width="58" height="84" rx="4" fill="#fffaf5"/><path d="M108 26h24" stroke="#fff" stroke-width="2" stroke-linecap="round"/><circle cx="120" cy="125" r="4" fill="#fff"/><path d="M110 52h14l9 9v34h-23z" fill="currentColor" opacity=".55"/><path d="M112 75h17M117 69v13M125 69v13M112 82h17" stroke="#fff" stroke-width="1.5"/>',
  work: '<ellipse cx="120" cy="143" rx="76" ry="4" fill="#000" opacity=".06"/><rect x="48" y="58" width="144" height="76" rx="12" fill="currentColor"/><path d="M94 58V40h52v18" fill="none" stroke="currentColor" stroke-width="7"/><path d="M49 83c46 18 94 18 142 0" fill="none" stroke="#fff" opacity=".5" stroke-width="2"/><rect x="112" y="86" width="16" height="20" rx="3" fill="#fffaf5"/>',
  language:
    '<ellipse cx="120" cy="143" rx="83" ry="4" fill="#000" opacity=".06"/><path d="M43 33h108a12 12 0 0 1 12 12v58a12 12 0 0 1-12 12H78l-28 20v-20h-7a12 12 0 0 1-12-12V45a12 12 0 0 1 12-12z" fill="currentColor"/><path d="M164 65h33a11 11 0 0 1 11 11v40a11 11 0 0 1-11 11h-4v14l-20-14h-25a11 11 0 0 1-11-11" fill="#fffaf4" stroke="currentColor" stroke-width="2"/><text x="66" y="84" fill="#fffaf4" font-family="Georgia,serif" font-size="36">Ciao</text>',

  arrival:
    '<ellipse cx="120" cy="143" rx="84" ry="5" fill="#000" opacity=".06"/><path d="M28 116C9 76 47 47 78 42" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 5"/><path d="m69 38 14 3-9 11" fill="none" stroke="currentColor" stroke-width="1.5"/><g transform="rotate(-8 112 83)"><rect x="71" y="33" width="83" height="103" rx="11" fill="currentColor"/><rect x="94" y="23" width="37" height="20" rx="6" fill="none" stroke="currentColor" stroke-width="5"/><path d="M91 37v94M135 37v94" stroke="#fff" opacity=".25" stroke-width="3"/><rect x="95" y="61" width="31" height="23" rx="3" fill="#fff9f0"/><path d="m100 72 6-6 5 4 8-4v12h-19z" fill="currentColor" opacity=".5"/><circle cx="87" cy="139" r="4" fill="currentColor"/><circle cx="139" cy="139" r="4" fill="currentColor"/></g><g transform="rotate(10 174 101)"><rect x="146" y="62" width="46" height="68" rx="5" fill="#fffaf1"/><circle cx="169" cy="84" r="11" fill="none" stroke="currentColor" stroke-width="1.3"/><ellipse cx="169" cy="84" rx="5" ry="11" fill="none" stroke="currentColor"/><path d="M158 84h22M158 112h22M160 117h18" stroke="currentColor" stroke-width="1.5"/></g><circle cx="199" cy="44" r="15" fill="#fff" opacity=".6"/><path d="m192 44 5 5 9-10" fill="none" stroke="currentColor" stroke-width="2"/>',
  housing:
    '<ellipse cx="120" cy="143" rx="88" ry="5" fill="#000" opacity=".06"/><path d="M29 78 82 37l52 41" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round"/><path d="M39 78v61h86V78L82 45z" fill="#fffaf4"/><rect x="76" y="98" width="23" height="41" rx="11" fill="currentColor"/><rect x="50" y="88" width="16" height="20" rx="3" fill="currentColor" opacity=".3"/><rect x="96" y="60" width="12" height="29" rx="2" fill="currentColor" opacity=".4"/><g transform="rotate(-27 168 84)"><circle cx="165" cy="70" r="21" fill="none" stroke="currentColor" stroke-width="9"/><path d="M165 91v43h14v-12h-14m0-11h14" fill="none" stroke="currentColor" stroke-width="8" stroke-linejoin="round"/></g><path d="M29 138h180" stroke="currentColor" stroke-width="1.2" opacity=".5"/><path d="M209 134v-18m0 4c-13 0-14-13-14-13s14 0 14 13m0 7c11 0 12-11 12-11s-12 0-12 11" fill="none" stroke="currentColor" stroke-width="2"/>',
  documents:
    '<ellipse cx="120" cy="143" rx="66" ry="4" fill="#000" opacity=".06"/><g transform="rotate(-7 110 78)"><path d="M73 27h62l25 25v84H73z" fill="#fff"/><path d="M135 27v25h25" fill="currentColor" opacity=".2"/><path d="M88 66h48M88 78h40M88 90h43M88 102h25" stroke="currentColor" stroke-width="4" stroke-linecap="round" opacity=".35"/></g><circle cx="158" cy="114" r="21" fill="currentColor"/><path d="m149 114 6 6 12-13" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="m152 133-5 17 11-4 7 4 2-18" fill="currentColor" opacity=".55"/>',
  transport:
    '<ellipse cx="120" cy="143" rx="74" ry="4" fill="#000" opacity=".06"/><rect x="75" y="25" width="90" height="108" rx="18" fill="currentColor"/><rect x="83" y="43" width="74" height="48" rx="6" fill="#fffcf6"/><path d="M120 43v48" stroke="currentColor" stroke-width="3"/><rect x="100" y="32" width="40" height="5" rx="2" fill="#fff" opacity=".6"/><circle cx="94" cy="107" r="6" fill="#fff"/><circle cx="146" cy="107" r="6" fill="#fff"/><path d="M95 128 83 145m62-17 12 17M94 137h52" stroke="currentColor" stroke-width="3"/><path d="M45 56h17M38 72h24M46 88h16M176 52h20M176 68h28" stroke="currentColor" stroke-width="2" stroke-linecap="round" opacity=".3"/>',
  health:
    '<ellipse cx="120" cy="143" rx="66" ry="4" fill="#000" opacity=".06"/><rect x="65" y="55" width="110" height="78" rx="10" fill="#fffaf5"/><path d="M99 55V40h42v15" fill="none" stroke="currentColor" stroke-width="5"/><path d="M112 74h16v14h14v16h-14v14h-16v-14H98V88h14z" fill="currentColor"/><path d="M164 45c-10-14-33 0-20 15l20 17 20-17c13-15-10-29-20-15z" fill="currentColor" opacity=".5"/><path d="M48 119v-19m0 5c-13 0-15-13-15-13s15 0 15 13m0 7c12 0 14-11 14-11s-14 0-14 11" fill="none" stroke="currentColor" stroke-width="2"/>',
  citylife:
    '<ellipse cx="120" cy="143" rx="82" ry="4" fill="#000" opacity=".06"/><rect x="42" y="106" width="95" height="20" rx="3" fill="currentColor"/><rect x="50" y="89" width="91" height="18" rx="3" fill="#fffcf6"/><rect x="57" y="73" width="80" height="16" rx="3" fill="currentColor" opacity=".45"/><path d="M155 78h42v40a15 15 0 0 1-15 15h-12a15 15 0 0 1-15-15z" fill="#fffcf6"/><path d="M197 84h7a11 11 0 0 1 0 22h-7" fill="none" stroke="currentColor" stroke-width="3"/><path d="M166 65c-10-9 10-13 0-22m17 22c-10-9 10-13 0-22" fill="none" stroke="currentColor" stroke-width="2" opacity=".6"/><path d="m91 29 6 13 15 2-11 10 3 15-13-7-13 7 3-15-11-10 15-2z" fill="currentColor" opacity=".35"/>',
};
const $ = (s) => document.querySelector(s);
const esc = (s) =>
  String(s ?? "").replace(
    /[&<>"']/g,
    (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[
        c
      ],
  );
const readStored = (key, fallback) => {
  try {
    return JSON.parse(localStorage.getItem(key)) || fallback;
  } catch {
    return fallback;
  }
};
const saved = readStored("studia-mi-profile", {});
const ANSWER_FIELDS = [
  "stay_duration",
  "country",
  "housing",
  "taxcode",
  "digital_id",
  "residence_status",
  "residence_intent",
  "grant",
  "visa",
  "permit",
  "health_coverage",
];
const state = {
  profile: {
    citizenship_confirmed: saved.citizenship_confirmed === true,
    ...Object.fromEntries(
      ANSWER_FIELDS.map((key) => [
        key,
        typeof saved[key] === "string" ? saved[key] : null,
      ]),
    ),
    language: ["it", "en"].includes(saved.language) ? saved.language : "it",
    citizenship: ["italian", "international", "eu", "non-eu"].includes(
      saved.citizenship,
    )
      ? saved.citizenship
      : null,
    stage: saved.stage === "here" ? "here" : "arriving",
  },
  journeys: [],
  sources: [],
  progress: readStored("studia-mi-checklists", {}),
  plans: readStored("studia-mi-plans", {}),
  journeyId: null,
  stepIndex: 0,
  messages: [],
  pending: false,
  ready: false,
};
const t = (key) => COPY[state.profile.language][key] || key;
const store = (key, value) => {
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch {
    /* Private browser mode: progress remains in page memory. */
  }
};
const art = (id) =>
  `<svg viewBox="0 0 240 160" aria-hidden="true" focusable="false">${ART[id] || ART.arrival}</svg>`;
const crumbs = (title) =>
  `<nav class="breadcrumb" aria-label="${t("breadcrumb")}"><ol><li><a href="#" data-home>${t("home")}</a></li><li><a href="#journeys" data-nav="journeys">${t("journeys")}</a></li><li aria-current="page">${esc(title)}</li></ol></nav>`;
const currentJourney = () =>
  state.journeys.find((j) => j.id === state.journeyId);
const progressKey = (journey) =>
  `${journey.plan_revision}:${state.profile.citizenship || "international"}:${journey.id}`;
const planFor = (journey) =>
  (state.plans[progressKey(journey)] ??= {
    choices: { ...journey.initial_choices },
  });
const checksFor = (journey) => {
  const key = progressKey(journey);
  if (!state.progress[key] && journey.plan_revision === "guided-1") {
    const old =
      state.progress[
        `${state.profile.citizenship || "international"}:${journey.id}`
      ];
    if (old) state.progress[key] = { ...old };
  }
  return state.progress[key] || {};
};
const checked = (journey, step, index) =>
  checksFor(journey)[`${step.id}:${index}`] === true;
const ready = (journey, step) =>
  StudyPlan.ready(step, checksFor(journey), planFor(journey));
const done = (journey, step) =>
  StudyPlan.validated(step, checksFor(journey), planFor(journey));
const frontier = (journey) =>
  StudyPlan.frontier(journey, checksFor(journey), planFor(journey));
const doneCount = (journey) => frontier(journey);
const savePlans = () => store("studia-mi-plans", state.plans);
const safeURL = (url) => {
  try {
    const u = new URL(url);
    return ["https:", "http:"].includes(u.protocol) ? u.href : "#";
  } catch {
    return "#";
  }
};
const sourceHost = (url) => {
  try {
    return new URL(url).hostname.replace(/^www\./, "");
  } catch {
    return "";
  }
};
const date = (value) => {
  try {
    return new Intl.DateTimeFormat(
      state.profile.language === "it" ? "it-IT" : "en-GB",
      {
        day: "numeric",
        month: "short",
        year: "numeric",
        timeZone: "Europe/Rome",
      },
    ).format(new Date(value));
  } catch {
    return "";
  }
};

function translate() {
  document.documentElement.lang = state.profile.language;
  document.title =
    state.profile.language === "it"
      ? "StudiaMI · La tua vita da studente a Milano"
      : "StudiaMI · Your student life in Milan";
  document.querySelectorAll("[data-t]").forEach((el) => {
    // Break lines in the copy before icons are added: a <br> inside an SVG ends it early.
    el.innerHTML =
      t(el.dataset.t).split("\n").map(iconLabel).join("<br>") +
      (el.dataset.tIcon ? ` ${icon(el.dataset.tIcon)}` : "");
  });
  document.querySelectorAll("[data-placeholder]").forEach((el) => {
    el.placeholder = t(el.dataset.placeholder);
  });
  document
    .querySelectorAll("[data-lang]")
    .forEach((el) =>
      el.setAttribute(
        "aria-pressed",
        String(el.dataset.lang === state.profile.language),
      ),
    );
  document
    .querySelectorAll(".close-dialog")
    .forEach((el) => el.setAttribute("aria-label", t("close")));
  document
    .querySelectorAll("button[type=submit]")
    .forEach((el) => el.setAttribute("aria-label", t("send")));
  document
    .querySelectorAll("[data-chat-form] input")
    .forEach((el) => el.setAttribute("aria-label", t("yourQuestion")));
  $(".header-chat").setAttribute("aria-label", t("openChat"));
  updateProfileControls();
}

function updateProfileControls() {
  const intl =
    state.profile.citizenship && state.profile.citizenship !== "italian";
  document
    .querySelectorAll("[data-audience]")
    .forEach((el) =>
      el.setAttribute(
        "aria-pressed",
        String(
          el.dataset.audience === "italian"
            ? state.profile.citizenship === "italian"
            : !!intl,
        ),
      ),
    );
  document
    .querySelectorAll("[data-stage]")
    .forEach((el) =>
      el.setAttribute(
        "aria-pressed",
        String(el.dataset.stage === state.profile.stage),
      ),
    );
  $("#international-options").hidden = !intl;
  document
    .querySelectorAll("[data-citizenship]")
    .forEach((el) =>
      el.setAttribute(
        "aria-pressed",
        String(el.dataset.citizenship === state.profile.citizenship),
      ),
    );
}

let journeysLoadVersion = 0;
async function loadJourneys() {
  const version = ++journeysLoadVersion;
  const params = new URLSearchParams({
    language: state.profile.language,
    citizenship: state.profile.citizenship || "international",
  });
  const r = await fetch("/api/journeys?" + params);
  if (!r.ok) throw new Error("journeys");
  const journeys = await r.json();
  if (version !== journeysLoadVersion) return;
  if (state.custom?.blocks?.length) {
    const response = await fetch("/api/plan/compose", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        blocks: state.custom.blocks,
        suppressed_blocks: state.custom.suppressed_blocks || [],
        residence_choice: state.custom.residence_choice || null,
        profile: {
          ...state.profile,
          citizenship: state.profile.citizenship || "international",
        },
      }),
    });
    if (!response.ok) throw new Error("custom plan");
    const custom = await response.json();
    if (version !== journeysLoadVersion) return;
    const generated = state.custom.generated_plan;
    if (
      generated?.base_revision === custom.plan_revision &&
      generated.language === state.profile.language &&
      generated.residence_choice === custom.residence_choice
    )
      journeys.push(generated);
    else if (
      generated?.base_revision === custom.plan_revision &&
      generated.language === state.profile.language &&
      !state.custom.residence_choice
    )
      journeys.push(generated);
    else journeys.push({ ...custom, needs_ai: true });
  }
  state.journeys = journeys;
  state.ready = true;
  renderJourneys();
  if (typeof renderSavedPath === "function") renderSavedPath();
  renderRoute();
}

function renderJourneys() {
  const card = (j) => {
    const count = doneCount(j);
    return `<article class="journey-card ${esc(j.tone)}"><div class="card-art">${art(j.icon)}<span class="step-badge"><span class="badge-dot"></span>${j.steps.length} ${t(j.steps.length === 1 ? "stepSingular" : "steps")}</span></div><div class="card-body"><p class="card-tag">${t("guideLink")} · HOW TO</p><h3 class="card-title"><button data-journey="${esc(j.id)}">${esc(j.title)}</button></h3><p class="card-description">${esc(j.subtitle)}</p>${j.scope ? `<p class="card-scope">${esc(j.scope)}</p>` : ""}${count ? `<p class="resume-mark">${count}/${j.steps.length} ${t("completed")}</p>` : ""}<button class="card-action" data-journey="${esc(j.id)}"><span>${count ? t("resumePath") : t("startPath")}</span><span aria-hidden="true">${icon("arrow-up-right")}</span></button>${j.questions
      .slice(0, 1)
      .map(
        (q) =>
          `<button class="card-question" data-ask="${esc(q)}"><span>${esc(q)}</span><span aria-hidden="true">${icon("arrow-up-right")}</span></button>`,
      )
      .join(
        "",
      )}<a class="card-guide" href="${esc(safeURL(j.guide_url))}" target="_blank" rel="noopener noreferrer">${t("guideLink")} ${icon("arrow-up-right")}</a></div></article>`;
  };
  $("#journey-grid").innerHTML = [
    ["before", "groupBefore", "groupBeforeBody"],
    ["first", "groupFirst", "groupFirstBody"],
    ["settled", "groupSettled", "groupSettledBody"],
  ]
    .map(([group, title, body], index) => {
      const journeys = state.journeys.filter((j) => j.group === group);
      return `<section class="catalog-group" aria-labelledby="catalog-${group}"><div class="catalog-heading"><span class="catalog-number">0${index + 1}</span><div><h3 id="catalog-${group}">${t(title)}</h3><p>${t(body)}</p></div><span class="catalog-count">${journeys.length} ${t("cases")}</span></div><div class="journey-grid">${journeys.map(card).join("")}</div></section>`;
    })
    .join("");
}

function navigate(journeyId, index = 0) {
  $("#chat-dialog").close();
  if (!state.profile.citizenship) {
    showProfile(() => navigate(journeyId, index));
    return;
  }
  const hash = `#journey/${journeyId}/${index}`;
  if (location.hash === hash) renderRoute();
  else location.hash = hash;
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function renderRoute() {
  if (!state.ready) return;
  if (typeof renderBuilder === "function" && location.hash === "#builder") {
    state.journeyId = null;
    $("#home-view").hidden = true;
    $("#journey-view").hidden = true;
    $("#builder-view").hidden = false;
    $("#floating-ask").hidden = true;
    renderBuilder();
    return;
  }
  $("#builder-view").hidden = true;
  const match = location.hash.match(/^#journey\/([a-z]+)\/(\d+|summary)$/);
  const j = match && state.journeys.find((item) => item.id === match[1]);
  state.journeyId = j?.id || null;
  if (j?.adaptive && (!j.ready || j.needs_ai)) {
    openBuilder("edit");
    return;
  }
  $("#home-view").hidden = !!j;
  $("#journey-view").hidden = !j;
  $("#floating-ask").hidden = !j && state.heroVisible !== false;
  if (!j) {
    updateChatContext();
    return;
  }
  state.stepIndex =
    match[2] === "summary"
      ? "summary"
      : Math.min(Number(match[2]), j.steps.length - 1);
  const openUntil = frontier(j);
  if (
    (state.stepIndex === "summary" && openUntil < j.steps.length) ||
    (state.stepIndex !== "summary" && state.stepIndex > openUntil)
  ) {
    state.stepIndex = Math.min(openUntil, j.steps.length - 1);
    history.replaceState(null, "", `#journey/${j.id}/${state.stepIndex}`);
    toast(t("lockedNotice"));
  }
  const label =
    state.profile.citizenship === "italian"
      ? t("italian")
      : state.profile.citizenship === "eu"
        ? t("eu")
        : state.profile.citizenship === "non-eu"
          ? t("nonEu")
          : t("international");
  const summary = state.stepIndex === "summary";
  $("#journey-view").innerHTML =
    `${crumbs(j.title)}<div class="journey-heading"><div><p class="eyebrow">${esc(j.tag)}</p><h1>${esc(j.title)}</h1><p>${esc(j.subtitle)}</p></div><button class="profile-summary" data-edit-profile>${esc(label)} · ${t("editProfile")} ${icon("arrow-up-right")}</button></div>${j.id === "custom" ? `<div class="adaptive-facts">${renderAIPlan(j)}${renderPlanFacts(j)}</div><div class="custom-outline"><button class="button secondary" data-builder="edit">${bt("editBlocks")} ${icon("arrow-up-right")}</button><p>${esc(j.priority)}</p></div>` : ""}${j.plan_intro ? `<div class="persona-plan"><p class="eyebrow">${t("inspiredBy")} ${esc(j.persona)}</p><p>${esc(j.plan_intro)}</p><small>${esc(j.priority)}</small></div>` : ""}<div class="journey-layout"><aside class="journey-sidebar" aria-label="${t("steps")}"><div class="journey-progress"><div class="progress-label"><span>${t("progress")}</span><span id="progress-count">${doneCount(j)}/${j.steps.length}</span></div><div class="progress-track"><div class="progress-fill" id="progress-fill"></div></div></div><ol class="step-nav" id="step-nav"></ol><p class="sidebar-note">${t("checklistNote")}</p></aside><section><div class="step-card ${esc(j.tone)}">${summary ? renderSummary(j) : renderStep(j, j.steps[state.stepIndex])}</div>${summary ? "" : renderPagination(j)}</section></div>`;
  updateProgress();
  updateChatContext();
}

function renderStep(j, s) {
  if (s.routes) {
    s = { ...s, ...s.routes[planFor(j).choices?.[s.follows_choice]] };
  }
  return `<div class="step-topline"><p>${t("step")} ${state.stepIndex + 1} ${t("of")} ${j.steps.length}</p><div class="step-illustration">${art(s.icon || j.icon)}</div></div>${s.block_title ? `<p class="eyebrow">${esc(s.block_title)}</p>` : ""}<h2>${esc(s.title)}</h2><p class="step-body">${esc(s.body)}</p>${s.why ? `<p class="step-why">${esc(s.why)}</p>` : ""}${s.owner ? `<p class="step-owner"><small>${t("owner")}</small> ${esc(s.owner)}</p>` : ""}${renderChoices(j, s)}<a class="official-link" href="${esc(safeURL(s.source))}" target="_blank" rel="noopener noreferrer"><span><small>${t("officialSource")}</small><strong>${t("readGuide")} · ${esc(sourceHost(s.source))}</strong></span><span aria-hidden="true">${icon("arrow-up-right")}</span></a>${(s.extra_sources || []).map((source) => `<a class="secondary-source" href="${esc(safeURL(source.url))}" target="_blank" rel="noopener noreferrer">${esc(source.title)} ${icon("arrow-up-right")}</a>`).join("")}<h3 class="checklist-title">${t("checklist")}</h3><div class="checklist">${s.checklist.map((item, i) => `<label class="check-item ${checked(j, s, i) ? "checked" : ""}"><input type="checkbox" data-check="${i}" ${checked(j, s, i) ? "checked" : ""}><span>${esc(item)}</span></label>`).join("")}</div>${s.draft || (s.follows_choice && planFor(j).choices?.[s.follows_choice] === "temporary") ? `<button class="draft-button" data-draft>${t("draft")} ${icon("arrow-up-right")}</button>` : ""}<div class="validation-panel"><h3>${t("validationTitle")}</h3><p>${esc(s.validation || t("validationReady"))}</p><small id="validation-status" role="status"></small><p class="validation-note">${t("validationNote")}</p></div><div class="step-help"><p>${t("needHelp")}</p><button class="help-button" data-help-step><span aria-hidden="true">${icon("message-circle")}</span>${t("helpStep")} ${icon("arrow-up-right")}</button></div>`;
}

function renderSummary(j) {
  return `<p class="eyebrow">${t("summary")}</p><h2 class="completion-title">${t("summaryTitle")}</h2><p class="completion-description">${t("summaryBody")}</p><ul class="completion-list">${j.steps.map((s, i) => `<li><button data-step="${i}">${done(j, s) ? icon("circle-check") : icon("circle")} ${esc(s.title)}</button><span>${done(j, s) ? t("verified") : t("toVerify")}</span></li>`).join("")}</ul><div class="completion-actions"><button class="button primary" data-download>${t("download")} ${icon("arrow-down")}</button><button class="button secondary" data-home>${t("backHome")} ${icon("arrow-up-right")}</button></div>`;
}

function renderChoices(j, s) {
  if (s.follows_choice) {
    const previous = j.steps.find((item) => item.id === s.follows_choice);
    const choice = previous?.choices?.find(
      (c) => c.id === planFor(j).choices?.[previous.id],
    );
    return choice
      ? `<div class="confirmed-choice"><small>${t("yourChoice")}</small><strong>${esc(choice.title)}</strong></div>`
      : "";
  }
  if (!s.choices) return "";
  return `<fieldset class="plan-choices"><legend>${t("choiceTitle")}</legend>${s.choices.map((c) => `<label><input type="radio" name="plan-choice" data-plan-choice="${esc(c.id)}" ${planFor(j).choices?.[s.id] === c.id ? "checked" : ""}><span><strong>${esc(c.title)}</strong><small>${esc(c.body)}</small></span></label>`).join("")}</fieldset>`;
}
function renderPagination(j) {
  const s = j.steps[state.stepIndex],
    validated = done(j, s);
  return `<div class="step-pagination"><button class="button secondary" data-step="${Math.max(0, state.stepIndex - 1)}" ${state.stepIndex === 0 ? "disabled" : ""}>${icon("arrow-left")} ${t("previous")}</button><button id="validate-step" class="button primary" data-validate ${!ready(j, s) ? "disabled" : ""}>${validated ? (state.stepIndex === j.steps.length - 1 ? t("summary") : t("next")) : state.stepIndex === j.steps.length - 1 ? t("validateFinish") : t("validateNext")} <span aria-hidden="true">${icon("arrow-right")}</span></button></div>`;
}
function updateProgress() {
  const j = currentJourney();
  if (!j) return;
  const openUntil = frontier(j);
  $("#progress-count").textContent = `${openUntil}/${j.steps.length}`;
  $("#progress-fill").style.width =
    `${Math.round((100 * openUntil) / j.steps.length)}%`;
  $("#step-nav").innerHTML = j.steps
    .map((s, i) => {
      const locked = i > openUntil,
        status =
          i < openUntil
            ? t("validatedStep")
            : locked
              ? t("locked")
              : t("current");
      return `${s.block_title && (i === 0 || j.steps[i - 1].block_id !== s.block_id) ? `<li class="block-nav-title">${esc(s.block_title)}</li>` : ""}<li><button data-step="${i}" aria-label="${i + 1}. ${esc(s.title)} · ${esc(status)}" class="${state.stepIndex === i ? "active" : ""} ${i < openUntil ? "done" : ""} ${locked ? "locked" : ""}" ${locked ? "disabled" : ""} ${state.stepIndex === i ? 'aria-current="step"' : ""}><span class="step-number">${i < openUntil ? icon("check") : locked ? icon("lock-keyhole") : i + 1}</span><span class="step-name">${esc(s.title)}<small>${esc(status)}</small></span></button></li>`;
    })
    .join("");
  if (state.stepIndex !== "summary") {
    const step = j.steps[state.stepIndex];
    $("#validate-step").disabled = !ready(j, step);
    $("#validation-status").textContent = done(j, step)
      ? t("validatedStep")
      : ready(j, step)
        ? t("validationReady")
        : step.choices && !planFor(j).choices?.[step.id]
          ? t("choiceRequired")
          : t("validationMissing");
    $("#validate-step").firstChild.textContent =
      (done(j, step)
        ? state.stepIndex === j.steps.length - 1
          ? t("summary")
          : t("next")
        : state.stepIndex === j.steps.length - 1
          ? t("validateFinish")
          : t("validateNext")) + " ";
  }
}

async function changeProfile(values) {
  Object.assign(state.profile, values);
  store("studia-mi-profile", state.profile);
  translate();
  try {
    await loadJourneys();
    return true;
  } catch {
    toast(t("loadError"));
    return false;
  }
}

function showProfile(onDone = () => {}) {
  const dialog = $("#info-dialog");
  $("#info-content").innerHTML =
    `<p class="eyebrow">STUDIAMI</p><h2 id="info-title">${t("profileTitle")}</h2><p>${t("profileBody")}</p><div class="profile-choices"><button data-pick-profile="italian">${t("italian")} ${icon("arrow-right")}</button><button data-pick-profile="international">${t("international")} ${icon("arrow-right")}</button></div>`;
  const handler = async (e) => {
    const btn = e.target.closest("[data-pick-profile]");
    if (!btn) return;
    if (btn.dataset.pickProfile === "international") {
      $("#info-content").innerHTML =
        `<h2 id="info-title">${t("intlTitle")}</h2><p>${t("intlBody")}</p><div class="profile-choices"><button data-pick-profile="eu">${t("eu")} ${icon("arrow-right")}</button><button data-pick-profile="non-eu">${t("nonEu")} ${icon("arrow-right")}</button><button data-pick-profile="unsure">${t("unsure")} ${icon("arrow-right")}</button></div>`;
      return;
    }
    dialog.removeEventListener("click", handler);
    dialog.close();
    await changeProfile({
      citizenship:
        btn.dataset.pickProfile === "unsure"
          ? "international"
          : btn.dataset.pickProfile,
    });
    onDone();
  };
  dialog.addEventListener("click", handler);
  dialog.addEventListener(
    "close",
    () => dialog.removeEventListener("click", handler),
    { once: true },
  );
  if (!dialog.open) dialog.showModal();
}

function sourceCards(sources) {
  return sources
    .map(
      (s) =>
        `<a class="source-item" href="${esc(safeURL(s.url))}" target="_blank" rel="noopener noreferrer"><strong>${esc(s.title)} ${icon("arrow-up-right")}</strong><small>${esc(sourceHost(s.url))}${s.fetched_at ? " · " + t("fetched") + " " + esc(date(s.fetched_at)) : ""}${s.stated_updated_date ? " · " + t("updated") + " " + esc(s.stated_updated_date) : ""}</small></a>`,
    )
    .join("");
}

async function showInfo(kind) {
  const d = $("#info-dialog");
  if (kind === "sources") {
    $("#info-content").innerHTML =
      `<p class="eyebrow">STUDIAMI</p><h2 id="info-title">${t("sources")}</h2><p>${t("sourceIntro")}</p><div id="all-sources">…</div>`;
    if (!d.open) d.showModal();
    try {
      const r = await fetch("/api/sources");
      if (!r.ok) throw new Error();
      state.sources = await r.json();
      $("#all-sources").innerHTML = sourceCards(state.sources);
    } catch {
      $("#all-sources").textContent = t("sourceError");
    }
  } else {
    $("#info-content").innerHTML =
      kind === "privacy"
        ? `<h2 id="info-title">${t("privacyTitle")}</h2><p>${t("privacyBody")}</p>`
        : `<p class="eyebrow">${t("lessSearching")}</p><h2 id="info-title">${esc(t("oneStep")).replace("\n", "<br>")}</h2>${[1, 2, 3].map((i) => `<p><strong>0${i} · ${t(`how${i}Title`)}</strong><br>${t(`how${i}Body`)}</p>`).join("")}`;
    if (!d.open) d.showModal();
  }
}

function updateChatContext() {
  const j = currentJourney(),
    s = j && state.stepIndex !== "summary" ? j.steps[state.stepIndex] : null;
  $("#chat-context").hidden = !j;
  $("#chat-context").textContent = j
    ? `${t("context")}: ${j.title}${s ? " → " + s.title : ""}`
    : "";
}

function openChat(question = "") {
  const d = $("#chat-dialog");
  updateChatContext();
  if (!d.open) d.showModal();
  if (question) $("#chat-input").value = question;
  $("#chat-input").focus();
}

function markdown(text) {
  // Escape all HTML first. Only create links for http(s); no raw HTML from the model.
  let html = esc(text);
  html = html.replace(
    /\[([^\]\n]+)\]\((https?:\/\/[^\s)]+)\)/g,
    (_, label, url) =>
      `<a href="${esc(safeURL(url.replace(/&amp;/g, "&")))}" target="_blank" rel="noopener noreferrer">${label}</a>`,
  );
  html = html.replace(/\*\*([^*\n]+)\*\*/g, "<strong>$1</strong>");
  return html
    .split("\n")
    .map((line) =>
      /^#{1,4} /.test(line)
        ? `<h4>${line.replace(/^#{1,4} /, "")}</h4>`
        : /^[-*] /.test(line)
          ? `<div class="list-line">${line.slice(2)}</div>`
          : line + "<br>",
    )
    .join("");
}

function appendMessage(role, text, data = {}) {
  const welcome = $(".chat-welcome");
  if (welcome) welcome.remove();
  const el = document.createElement("div");
  el.className = "message " + role;
  if (role === "user") el.textContent = text;
  else
    el.innerHTML = `<div class="message-label">${icon("message-circle")} STUDIAMI</div><div class="message-text">${markdown(text)}</div>${data.freshness_notice ? `<p class="freshness-notice">${esc(data.freshness_notice)}</p>` : ""}${data.sources?.length ? `<div class="source-list"><p class="source-label">${t("usedSources")}</p>${sourceCards(data.sources)}</div>` : ""}${data.suggested_journey ? `<button class="suggested-journey" data-journey="${esc(data.suggested_journey)}">${t("openSuggested")} ${icon("arrow-right")}</button>` : ""}`;
  $("#chat-messages").append(el);
  scrollChat();
}

function scrollChat() {
  const el = $("#chat-messages");
  el.scrollTop = el.scrollHeight;
}

async function sendQuestion(question, retry = false) {
  const text = question.trim();
  if (!text || state.pending) return;
  openChat();
  state.pending = true;
  $("#chat-input").value = "";
  document
    .querySelectorAll("form button[type=submit]")
    .forEach((b) => (b.disabled = true));
  document.querySelectorAll(".error-message").forEach((e) => e.remove());
  if (!retry) {
    state.messages.push({ role: "user", content: text });
    appendMessage("user", text);
  }
  const thinking = document.createElement("div");
  thinking.className = "thinking";
  thinking.innerHTML = `<span></span><span></span><span></span><small>${t("thinking")}</small>`;
  $("#chat-messages").append(thinking);
  scrollChat();
  const j = currentJourney(),
    s = j && state.stepIndex !== "summary" ? j.steps[state.stepIndex] : null;
  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        messages: state.messages
          .slice(-9)
          .filter((m, i, a) => i > 0 || m.role === "user"),
        profile: {
          ...state.profile,
          citizenship: state.profile.citizenship || "international",
        },
        suppressed_blocks:
          j?.id === "custom" ? state.custom.suppressed_blocks || [] : [],
        journey_id: j?.id || null,
        step_id: s?.id || null,
        plan_choice: j
          ? planFor(j).choices?.[
              j.id === "custom" ? "arrival--giulia-status" : "giulia-status"
            ] || null
          : null,
        custom_blocks: j?.id === "custom" ? j.blocks : [],
        generated_plan: j?.ai_generated ? j : null,
        validated_step_ids: j
          ? j.steps.slice(0, frontier(j)).map((step) => step.id)
          : [],
      }),
    });
    const result = await response.json();
    if (!response.ok) {
      const error = new Error(result.detail || "chat");
      error.status = response.status;
      throw error;
    }
    thinking.remove();
    state.messages.push({ role: "assistant", content: result.answer });
    appendMessage("assistant", result.answer, result);
  } catch (error) {
    thinking.remove();
    const el = document.createElement("div");
    el.className = "error-message";
    el.textContent =
      error.message === "CLAUDE_NOT_CONFIGURED"
        ? t("chatUnavailable")
        : error.status === 429
          ? t("chatLimit")
          : t("chatError");
    const retryButton = document.createElement("button");
    retryButton.textContent = t("retry");
    retryButton.addEventListener("click", () => sendQuestion(text, true));
    el.append(retryButton);
    $("#chat-messages").append(el);
    scrollChat();
  } finally {
    state.pending = false;
    document
      .querySelectorAll("form button[type=submit]")
      .forEach((b) => (b.disabled = false));
  }
}

function downloadChecklist() {
  const j = currentJourney();
  if (!j) return;
  const content =
    `StudiaMI — ${j.title}\n\n${t("checklistNote")}\n\n` +
    j.steps
      .map(
        (s) =>
          `${s.title} — ${done(j, s) ? t("validatedStep") : t("toVerify")}\n${s.checklist.map((item, i) => `[${checked(j, s, i) ? "x" : " "}] ${item}`).join("\n")}\n${s.source}\n`,
      )
      .join("\n");
  const url = URL.createObjectURL(
    new Blob([content], { type: "text/plain;charset=utf-8" }),
  );
  const a = document.createElement("a");
  a.href = url;
  a.download = `StudiaMI-${j.id}.txt`;
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 2000);
}

function toast(message) {
  $("#toast").textContent = message;
  $("#toast").hidden = false;
  setTimeout(() => ($("#toast").hidden = true), 3500);
}

document.addEventListener("click", async (e) => {
  const el = e.target.closest("button,a");
  if (!el) return;
  if (el.classList.contains("close-dialog")) {
    el.closest("dialog").close();
    return;
  }
  if (el.dataset.lang) {
    await changeProfile({ language: el.dataset.lang });
    return;
  }
  if (el.dataset.audience) {
    await changeProfile({ citizenship: el.dataset.audience });
    return;
  }
  if (el.dataset.citizenship) {
    await changeProfile({ citizenship: el.dataset.citizenship });
    return;
  }
  if (el.dataset.stage) {
    await changeProfile({ stage: el.dataset.stage });
    return;
  }
  if (el.dataset.open) {
    el.dataset.open === "chat" ? openChat() : showInfo(el.dataset.open);
    return;
  }
  if (el.dataset.persona) {
    await changeProfile({
      citizenship: el.dataset.persona === "giulia" ? "italian" : "non-eu",
      stage: "here",
    });
    navigate(
      "arrival",
      Math.min(frontier(state.journeys[0]), state.journeys[0].steps.length - 1),
    );
    return;
  }
  if (el.hasAttribute("data-validate")) {
    const j = currentJourney();
    if (StudyPlan.confirm(j, state.stepIndex, checksFor(j), planFor(j))) {
      savePlans();
      location.hash = `#journey/${j.id}/${state.stepIndex === j.steps.length - 1 ? "summary" : state.stepIndex + 1}`;
      renderJourneys();
    } else toast(t("lockedNotice"));
    return;
  }
  if (el.hasAttribute("data-draft")) {
    sendQuestion(t("draftPrompt"));
    return;
  }
  if (el.dataset.journey) {
    e.preventDefault();
    navigate(el.dataset.journey);
    return;
  }
  if (el.dataset.step !== undefined) {
    location.hash = `#journey/${state.journeyId}/${el.dataset.step}`;
    return;
  }
  if (el.hasAttribute("data-home")) {
    location.hash = "";
    window.scrollTo({ top: 0, behavior: "smooth" });
    return;
  }
  if (el.hasAttribute("data-edit-profile")) {
    showProfile();
    return;
  }
  if (el.hasAttribute("data-help-step")) {
    const s = currentJourney()?.steps[state.stepIndex];
    if (s) sendQuestion(t("helpPrompt") + s.title);
    return;
  }
  if (el.hasAttribute("data-download")) {
    downloadChecklist();
    return;
  }
  if (el.dataset.ask) {
    sendQuestion(el.dataset.ask);
    return;
  }
  if (el.dataset.question) {
    const key =
      "question" +
      el.dataset.question[0].toUpperCase() +
      el.dataset.question.slice(1);
    sendQuestion(t(key));
    return;
  }
  if (
    el.dataset.nav === "journeys" &&
    (state.journeyId || location.hash === "#builder")
  ) {
    e.preventDefault();
    location.hash = "#journeys";
    setTimeout(() => $("#journeys").scrollIntoView({ behavior: "smooth" }), 30);
  }
});
document.addEventListener("change", async (e) => {
  if (!e.target.matches("[data-check], [data-plan-choice]")) return;
  const j = currentJourney(),
    s = j.steps[state.stepIndex],
    key = progressKey(j);
  if (j.adaptive && e.target.matches("[data-plan-choice]")) {
    await updateCustomChoice(j, s, e.target.dataset.planChoice);
    return;
  }
  const requiresReview = done(j, s) || e.target.matches("[data-plan-choice]");
  if (e.target.matches("[data-plan-choice]")) {
    planFor(j).choices ??= {};
    planFor(j).choices[s.id] = e.target.dataset.planChoice;
  } else {
    state.progress[key] ??= {};
    state.progress[key][`${s.id}:${e.target.dataset.check}`] = e.target.checked;
    store("studia-mi-checklists", state.progress);
    e.target.closest("label").classList.toggle("checked", e.target.checked);
  }
  StudyPlan.reopen(j, state.stepIndex, planFor(j));
  if (requiresReview) {
    for (const later of j.steps.slice(state.stepIndex + 1)) {
      later.checklist.forEach(
        (_, i) => delete state.progress[key]?.[`${later.id}:${i}`],
      );
    }
    store("studia-mi-checklists", state.progress);
  }
  savePlans();
  updateProgress();
  renderJourneys();
});
document.querySelectorAll("[data-chat-form]").forEach((form) =>
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const input = form.elements.question;
    sendQuestion(input.value);
    input.value = "";
  }),
);
$("#chat-form").addEventListener("submit", (e) => {
  e.preventDefault();
  sendQuestion($("#chat-input").value);
});
$("#chat-input").addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendQuestion(e.target.value);
  }
});
$("#clear-chat").addEventListener("click", () => {
  if (state.pending) return;
  state.messages = [];
  $("#chat-messages").innerHTML =
    `<div class="chat-welcome"><span class="welcome-star" aria-hidden="true">${icon("message-circle")}</span><h3>${t("chatWelcome")}</h3><p>${t("chatWelcomeBody")}</p></div>`;
  $("#chat-input").value = "";
  $("#chat-input").focus();
});
for (const d of document.querySelectorAll("dialog"))
  d.addEventListener("click", (e) => {
    if (e.target === d) {
      const r = d.getBoundingClientRect();
      if (
        e.clientX < r.left ||
        e.clientX > r.right ||
        e.clientY < r.top ||
        e.clientY > r.bottom
      )
        d.close();
    }
  });
window.addEventListener("hashchange", renderRoute);
new IntersectionObserver(
  (entries) => {
    state.heroVisible = entries[0].isIntersecting;
    $("#floating-ask").hidden =
      location.hash === "#builder" || (!state.journeyId && state.heroVisible);
  },
  { threshold: 0.3 },
).observe($(".hero-ask"));
