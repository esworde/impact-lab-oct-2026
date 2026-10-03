"use strict";
const BUILDER_COPY = {
  it: {
    createPath: "Crea il mio percorso ↗",
    guideMe: "Guidami con le domande",
    storyExample: "UNA STORIA DA CUI PARTIRE",
    giuliaStory:
      "Giulia arriva a Milano. Casa, borsa di studio, domicilio: come si incastrano?",
    tryGiulia: "Componi il percorso di Giulia →",
    sourcePromise:
      "Guide ufficiali, un piano che scegli tu. Nessun account richiesto.",
    title: "La tua storia. Il tuo percorso.",
    intro:
      "Le tue risposte cambiano servizi, passaggi e checklist. Chiediamo ciò che manca e puoi rivedere le scelte prima e durante il percorso.",
    story: "Racconta liberamente",
    questions: "Rispondi alle domande",
    storyLabel: "Cosa vuoi organizzare a Milano?",
    placeholder:
      "Sono una studentessa italiana, ho una borsa di studio e sto arrivando a Milano. Cerco casa e non so se cambiare residenza…",
    storyNote:
      "Descrivi obiettivi e dubbi, senza nomi, indirizzi o documenti. Il testo viene inviato a Claude per proporre le card; non viene salvato nel piano.",
    propose: "Componi il mio percorso",
    thinking: "Metto insieme le card…",
    error:
      "Non riesco a proporre le card adesso. Riprova o usa le domande: puoi comporre il piano anche da lì.",
    qProfile: "Da quale situazione parti?",
    qProfileNote:
      "Serve ad adattare le guide sui documenti. Puoi lasciare il profilo da verificare.",
    qStage: "A che punto sei?",
    qGoals: "Cosa vuoi affrontare?",
    qGoalsNote:
      "Scegli uno o più blocchi. Nell’anteprima potrai aggiungerne altri e cambiarne l’ordine.",
    next: "Continua →",
    previous: "← Indietro",
    preview: "Il piano prende forma.",
    previewNote:
      "Controlla il profilo e scegli i blocchi: puoi aggiungerli, toglierli e cambiare l’ordine prima di iniziare.",
    profile: "Profilo da confermare",
    stage: "Momento",
    blocks: "blocchi",
    steps: "passi",
    remove: "Rimuovi",
    up: "Sposta prima",
    down: "Sposta dopo",
    add: "Aggiungi un blocco",
    empty: "Aggiungi almeno una card per iniziare.",
    start: "Conferma il piano e inizia →",
    editBlocks: "Modifica i blocchi",
    resume: "Riprendi il mio percorso →",
    saved: "Il tuo piano rimane in questo browser.",
    sequence:
      "Ogni passo si sblocca dopo i controlli e la tua conferma. Le scadenze e le attività urgenti vanno verificate anche in parallelo.",
    giulia:
      "Come Giulia: hai già codice fiscale, CIE e SPID. Vuoi chiarire borsa e ISEE prima di decidere tra domicilio e residenza, poi organizzare casa, trasporti e salute.",
    reviewChange:
      "Se cambi i blocchi o il profilo, il piano composto richiede nuove conferme. Ritrovando la stessa composizione puoi riprendere i suoi progressi.",
    questionCounter: "DOMANDA",
    of: "DI",
    restart: "Ricominciamo",
    manual: "Puoi selezionare anche una sola card.",
  },
  en: {
    createPath: "Create my journey ↗",
    guideMe: "Guide me with questions",
    storyExample: "A STORY TO START FROM",
    giuliaStory:
      "Giulia arrives in Milan. Housing, a study grant, domicile: how do they fit together?",
    tryGiulia: "Build Giulia’s journey →",
    sourcePromise: "Official guides. A plan you choose. No account needed.",
    title: "Your story. Your journey.",
    intro:
      "Your answers shape services, steps and checklists. We ask what is missing, and you can review choices before and during the journey.",
    story: "Tell your story",
    questions: "Answer a few questions",
    storyLabel: "What do you want to organise in Milan?",
    placeholder:
      "I’m an Italian student with a study grant, moving to Milan. I need housing and I’m unsure whether to transfer my residence…",
    storyNote:
      "Describe goals and questions, without names, addresses or documents. Your text is sent to Claude to suggest cards; it is not saved in the plan.",
    propose: "Build my journey",
    thinking: "Bringing your cards together…",
    error:
      "I cannot suggest cards right now. Retry or use the questions: you can build a plan there too.",
    qProfile: "What is your starting situation?",
    qProfileNote:
      "This adapts document guidance. You can leave your profile to be checked.",
    qStage: "Where are you in your move?",
    qGoals: "What would you like to tackle?",
    qGoalsNote:
      "Choose one or more blocks. In the preview you can add others and change their order.",
    next: "Continue →",
    previous: "← Back",
    preview: "Your plan takes shape.",
    previewNote:
      "Check the profile and choose the blocks: add, remove and reorder them before starting.",
    profile: "Profile to confirm",
    stage: "Stage",
    blocks: "blocks",
    steps: "steps",
    remove: "Remove",
    up: "Move earlier",
    down: "Move later",
    add: "Add a block",
    empty: "Add at least one card to begin.",
    start: "Confirm the plan and start →",
    editBlocks: "Edit blocks",
    resume: "Continue my journey →",
    saved: "Your plan stays in this browser.",
    sequence:
      "Each step unlocks after your checks and explicit confirmation. Check deadlines and urgent tasks in parallel too.",
    giulia:
      "Like Giulia: you already have a tax code, ID card and SPID. Clarify grants and ISEE before deciding between domicile and residence, then organise housing, transport and health.",
    reviewChange:
      "Changing blocks or profile requires fresh confirmations for the composed plan. Returning to the same composition lets you resume its progress.",
    questionCounter: "QUESTION",
    of: "OF",
    restart: "Start again",
    manual: "You can also choose just one card.",
  },
};
Object.assign(BUILDER_COPY.it, {
  completeProfile: "UNA DOMANDA PER ADATTARE IL PIANO",
  unknownAnswer:
    "Puoi scegliere “da verificare”: il piano ti guiderà a chiarire quel punto con l’ufficio, senza presumere una risposta.",
  facts: "Le risposte che cambiano il tuo piano",
  excluded: "Servizi esclusi dal piano",
  adaptError: "Non riesco ad aggiornare il piano. Riprova la scelta tra poco.",
  orderNote:
    "Decisioni e controlli sui documenti precedono i servizi che ne dipendono. Gli altri blocchi si possono riordinare.",
});
Object.assign(BUILDER_COPY.en, {
  completeProfile: "A QUESTION TO ADAPT YOUR PLAN",
  unknownAnswer:
    "You can choose “to check”: the plan will help clarify it with the office, without assuming an answer.",
  facts: "Answers shaping your plan",
  excluded: "Services excluded from this plan",
  adaptError: "I cannot update the plan right now. Retry your choice shortly.",
  orderNote:
    "Decisions and document checks precede dependent services. You can reorder the other blocks.",
});
const FACT_LABELS = {
  it: {
    stay_duration: "Durata a Milano",
    country: "Paese di cittadinanza",
    housing: "Sistemazione",
    taxcode: "Codice fiscale",
    digital_id: "SPID / CIE online",
    residence_status: "Residenza attuale",
    residence_intent: "Scelta da valutare",
    grant: "Borsa / ISEE",
    visa: "Visto già disponibile",
    permit: "Stato del permesso",
    health_coverage: "Copertura sanitaria verificata",
  },
  en: {
    stay_duration: "Stay in Milan",
    country: "Citizenship country",
    housing: "Accommodation",
    taxcode: "Tax code",
    digital_id: "SPID / online ID",
    residence_status: "Current residence",
    residence_intent: "Option to consider",
    grant: "Grant / ISEE",
    visa: "Visa available",
    permit: "Permit status",
    health_coverage: "Healthcare coverage checked",
  },
};
const FACT_OPTIONS = {
  stay_duration: [
    ["short", "Fino a 90 giorni", "Up to 90 days"],
    [
      "under-year",
      "Oltre 90 giorni, meno di un anno",
      "Over 90 days, under one year",
    ],
    ["year-plus", "Un anno o più", "One year or longer"],
    ["unknown", "Da verificare", "To check"],
  ],
  housing: [
    ["searching", "Sto cercando", "Still searching"],
    ["found", "Casa trovata", "Accommodation found"],
    ["unknown", "Da verificare", "To check"],
  ],
  residence_status: [
    ["elsewhere", "Altro Comune / estero", "Elsewhere / abroad"],
    ["milan", "Residente a Milano", "Registered in Milan"],
    ["unknown", "Da verificare", "To check"],
  ],
  residence_intent: [
    ["undecided", "Confrontare le opzioni", "Compare options"],
    ["keep", "Mantengo la residenza", "Keep residence"],
    [
      "temporary",
      "Domicilio / registrazione temporanea",
      "Temporary domicile / registration",
    ],
    ["transfer", "Trasferisco la residenza", "Transfer residence"],
  ],
  permit: [
    ["none", "Non presentata", "Not submitted"],
    ["pending", "Presentata, ho la ricevuta", "Submitted, I have the receipt"],
    ["valid", "Permesso italiano valido", "Valid Italian permit"],
    ["unknown", "Da verificare", "To check"],
  ],
};
const YES_OPTIONS = [
  ["yes", "Sì", "Yes"],
  ["no", "No", "No"],
  ["unknown", "Da verificare", "To check"],
];
function renderPlanFacts(plan, editable = false) {
  if (!plan) return "";
  const lang = state.profile.language,
    index = lang === "it" ? 1 : 2;
  const fields = Object.entries(plan.answers || {}).filter(([key]) =>
    ANSWER_FIELDS.includes(key),
  );
  const rows = fields
    .map(([key, value]) => {
      let opts = FACT_OPTIONS[key] || YES_OPTIONS;
      if (
        key === "residence_intent" &&
        (!["italian", "eu"].includes(builder.profile?.citizenship) ||
          (builder.profile?.citizenship === "eu" &&
            builder.profile?.stay_duration === "year-plus"))
      )
        opts = opts.filter((o) => o[0] !== "temporary");
      const display = opts.find((o) => o[0] === value)?.[index] || value;
      return `<div><dt>${esc(FACT_LABELS[lang][key])}</dt><dd>${editable ? (key === "country" ? `<input data-builder-profile="country" maxlength="50" minlength="2" value="${esc(value)}" aria-label="${esc(FACT_LABELS[lang][key])}">` : `<select data-builder-profile="${key}" aria-label="${esc(FACT_LABELS[lang][key])}">${opts.map((o) => `<option value="${o[0]}" ${o[0] === value ? "selected" : ""}>${esc(o[index])}</option>`).join("")}</select>`) : esc(display)}</dd></div>`;
    })
    .join("");
  const exclusions = (plan.excluded || [])
    .map((j) => `<li><strong>${esc(j.title)}</strong> ${esc(j.reason)}</li>`)
    .join("");
  return `<details class="plan-facts"><summary>${bt("facts")} · ${fields.length}</summary><dl>${rows}</dl></details>${exclusions ? `<div class="plan-excluded"><small>${bt("excluded")}</small><ul>${exclusions}</ul></div>` : ""}${!editable ? `<div class="plan-services">${(plan.block_summaries || []).map((j) => `<span title="${esc(j.personalization_reason)}">${esc(j.title)}</span>`).join("")}</div>` : ""}`;
}
async function updateCustomChoice(j, s, value) {
  if (state.adapting) return;
  state.adapting = true;
  const key = progressKey(j),
    previous = planFor(j).choices?.[s.id],
    previousRoute = state.custom.residence_choice;
  planFor(j).choices ??= {};
  planFor(j).choices[s.id] = value;
  StudyPlan.reopen(j, state.stepIndex, planFor(j));
  for (const step of j.steps.slice(state.stepIndex))
    step.checklist.forEach(
      (_, i) => delete state.progress[key]?.[`${step.id}:${i}`],
    );
  savePlans();
  store("studia-mi-checklists", state.progress);
  document
    .querySelectorAll("#journey-view button,#journey-view input")
    .forEach((el) => (el.disabled = true));
  try {
    const response = await fetch("/api/plan/compose", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        blocks: state.custom.blocks,
        profile: state.profile,
        residence_choice: value,
        suppressed_blocks: state.custom.suppressed_blocks || [],
      }),
    });
    if (!response.ok) throw new Error();
    const plan = await response.json();
    state.custom.residence_choice = value;
    store("studia-mi-custom", state.custom);
    const index = state.journeys.findIndex((item) => item.id === "custom");
    state.journeys[index] = plan;
  } catch {
    planFor(j).choices[s.id] = previous;
    state.custom.residence_choice = previousRoute;
    savePlans();
    toast(bt("adaptError"));
  } finally {
    state.adapting = false;
    renderRoute();
    renderSavedPath();
  }
}
for (const lang of ["it", "en"]) Object.assign(COPY[lang], BUILDER_COPY[lang]);
const bt = (key) => BUILDER_COPY[state.profile.language][key] || key;
const validBlocks = new Set([
  "arrival",
  "visa",
  "housing",
  "permit",
  "taxcode",
  "transport",
  "health",
  "residence",
  "temporary",
  "bank",
  "phone",
  "support",
  "identity",
  "work",
  "language",
]);
const storedCustom = readStored("studia-mi-custom", null);
state.custom =
  storedCustom &&
  Array.isArray(storedCustom.blocks) &&
  storedCustom.blocks.length &&
  storedCustom.blocks.every((b) => validBlocks.has(b)) &&
  new Set(storedCustom.blocks).size === storedCustom.blocks.length
    ? storedCustom
    : null;
const builder = {
  mode: "story",
  question: 0,
  plan: null,
  suppressed: [],
  profile: null,
  blocks: [],
  available: [],
  preview: false,
  pending: false,
  error: false,
  story: "",
  example: false,
};
let builderVersion = 0;
const builderProfile = () => ({
  ...builder.profile,
  language: state.profile.language,
});
const options = () => [
  ["italian", t("italian")],
  ["eu", t("eu")],
  ["non-eu", t("nonEu")],
  ["international", t("unsure")],
];
function renderSavedPath() {
  const el = $("#saved-path");
  el.hidden = !state.custom;
  el.innerHTML = state.custom
    ? `<button data-resume-custom ${!state.ready ? "disabled" : ""}>${iconLabel(bt("resume"))}</button><small>${bt("saved")}</small>`
    : "";
}
async function openBuilder(mode) {
  ++builderVersion;
  builder.mode = mode === "questions" ? "questions" : "story";
  builder.question = 0;
  builder.pending = false;
  builder.error = false;
  builder.preview = false;
  builder.example = false;
  builder.profile = {
    ...state.profile,
    citizenship: state.profile.citizenship || "international",
  };
  builder.blocks = [];
  builder.plan = null;
  builder.suppressed = [];
  builder.available = state.journeys.filter((j) => j.id !== "custom");
  if (mode === "edit" && state.custom) {
    builder.blocks = [...state.custom.blocks];
    builder.suppressed = [...(state.custom.suppressed_blocks || [])];
    builder.profile.residence_intent =
      currentJourney()?.residence_choice ||
      state.custom.residence_choice ||
      builder.profile.residence_intent;
    builder.preview = true;
  }
  if (mode === "giulia") {
    builder.profile.citizenship = "italian";
    Object.assign(builder.profile, {
      stage: "here",
      citizenship_confirmed: true,
      stay_duration: "year-plus",
      housing: "found",
      taxcode: "yes",
      digital_id: "yes",
      residence_status: "elsewhere",
      residence_intent: "undecided",
      grant: "yes",
      health_coverage: "unknown",
    });
    builder.blocks = ["arrival", "housing", "transport", "health"];
    builder.preview = true;
    builder.example = true;
  }
  location.hash = "#builder";
  renderRoute();
  window.scrollTo({ top: 0, behavior: "smooth" });
  if (builder.preview) await refreshBuilderCards();
}
async function refreshBuilderCards() {
  const version = ++builderVersion;
  builder.pending = true;
  builder.error = false;
  renderBuilder();
  try {
    const r = await fetch(
      "/api/journeys?" +
        new URLSearchParams({
          language: state.profile.language,
          citizenship: builder.profile.citizenship,
        }),
    );
    if (!r.ok) throw new Error();
    const cards = await r.json();
    if (version !== builderVersion) return;
    builder.available = cards;
    if (builder.blocks.length) {
      const response = await fetch("/api/plan/compose", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          blocks: builder.blocks,
          profile: builderProfile(),
          suppressed_blocks: builder.suppressed,
        }),
      });
      if (!response.ok) throw new Error();
      const plan = await response.json();
      if (version !== builderVersion) return;
      builder.plan = plan;
    } else builder.plan = null;
  } catch {
    if (version === builderVersion) builder.error = true;
  } finally {
    if (version === builderVersion) {
      builder.pending = false;
      if (location.hash === "#builder") renderBuilder();
    }
  }
}
function renderBuilder() {
  builder.profile ??= {
    ...state.profile,
    citizenship: state.profile.citizenship || "international",
  };
  const tabs = `<div class="builder-tabs" aria-label="${esc(bt("createPath").replace(/[↗→←]/g, "").trim())}"><button data-builder-mode="story" aria-pressed="${builder.mode === "story"}">${bt("story")}</button><button data-builder-mode="questions" aria-pressed="${builder.mode === "questions"}">${bt("questions")}</button></div>`;
  let content = "";
  if (builder.preview) {
    const selected = (builder.plan?.block_summaries || []).map((j) => ({
      ...j,
      steps: (j.step_titles || []).map((title) => ({ title })),
    }));
    content = `<p class="eyebrow">${bt("preview")}</p>${builder.example ? `<p class="builder-example">${bt("giulia")}</p>` : ""}<p>${bt("previewNote")}</p><div class="builder-profile"><label>${bt("profile")}<select data-builder-profile="citizenship">${options()
      .map(
        ([v, label]) =>
          `<option value="${v}" ${v === builder.profile.citizenship ? "selected" : ""}>${esc(label)}</option>`,
      )
      .join(
        "",
      )}</select></label><label>${bt("stage")}<select data-builder-profile="stage">${[
      ["arriving", t("arriving")],
      ["here", t("alreadyHere")],
    ]
      .map(
        ([v, label]) =>
          `<option value="${v}" ${v === builder.profile.stage ? "selected" : ""}>${esc(label)}</option>`,
      )
      .join(
        "",
      )}</select></label></div>${renderPlanFacts(builder.plan, true)}<p class="builder-count">${selected.length} ${bt("blocks")} · ${selected.reduce((sum, j) => sum + j.steps.length, 0)} ${bt("steps")}</p><ol class="builder-blocks">${selected.map((j, i) => `<li class="builder-block ${esc(j.tone)}"><div class="builder-block-art">${art(j.icon)}</div><div class="builder-block-body"><small>0${i + 1} · ${j.steps.length} ${t(j.steps.length === 1 ? "stepSingular" : "steps")}</small><h3>${esc(j.title)}</h3><p>${esc(j.subtitle)}</p>${j.personalization_reason ? `<p class="block-reason">${esc(j.personalization_reason)}</p>` : ""}<details><summary>${t("steps")}</summary><ol>${j.steps.map((s) => `<li>${esc(s.title)}</li>`).join("")}</ol></details></div><div class="block-tools"><button data-block-up="${j.id}" aria-label="${bt("up")}: ${esc(j.title)}" ${i === 0 || j.order_locked || selected[i - 1]?.order_locked ? "disabled" : ""}>${icon("arrow-up")}</button><button data-block-down="${j.id}" aria-label="${bt("down")}: ${esc(j.title)}" ${i === selected.length - 1 || j.order_locked || selected[i + 1]?.order_locked ? "disabled" : ""}>${icon("arrow-down")}</button><button data-block-remove="${j.id}" aria-label="${bt("remove")}: ${esc(j.title)}">${icon("x")}</button></div></li>`).join("")}</ol>${!selected.length ? `<p>${bt("empty")}</p>` : ""}<details class="builder-add"><summary>${bt("add")} ${icon("plus")}</summary><div class="builder-goals">${builder.available
      .filter((j) => !selected.some((s) => s.id === j.id))
      .map(
        (j) =>
          `<button data-block-add="${j.id}">${esc(j.title)} ${icon("plus")}</button>`,
      )
      .join(
        "",
      )}</div></details><p class="builder-note">${bt("sequence")} ${bt("orderNote")}</p><small>${bt("reviewChange")}</small><div class="builder-footer"><button class="button secondary" data-builder-restart>${bt("restart")}</button><button class="button primary" data-builder-start ${!selected.length || builder.pending || builder.error || !builder.plan?.ready ? "disabled" : ""}>${iconLabel(bt("start"))}</button></div>`;
  } else if (builder.mode === "story") {
    content = `<form id="builder-story-form"><label class="builder-label" for="builder-story">${bt("storyLabel")}</label><textarea id="builder-story" minlength="10" maxlength="2000" required placeholder="${esc(bt("placeholder"))}">${esc(builder.story)}</textarea><small>${bt("storyNote")}</small><div class="builder-footer"><button class="button primary" type="submit" ${builder.pending ? "disabled" : ""}>${builder.pending ? bt("thinking") : bt("propose")} ${icon("arrow-up-right")}</button></div></form>`;
  } else {
    const q = builder.question;
    content = `<p class="eyebrow">${bt("questionCounter")} ${q + 1} ${bt("of")} 3</p><h2>${bt(["qProfile", "qStage", "qGoals"][q])}</h2>`;
    if (q === 0)
      content += `<p>${bt("qProfileNote")}</p><div class="builder-goals">${options()
        .map(
          ([v, label]) =>
            `<button data-builder-pick-profile="${v}" aria-pressed="${v === builder.profile.citizenship}">${esc(label)}</button>`,
        )
        .join("")}</div>`;
    if (q === 1)
      content += `<div class="builder-goals">${[
        ["arriving", t("arriving")],
        ["here", t("alreadyHere")],
      ]
        .map(
          ([v, label]) =>
            `<button data-builder-pick-stage="${v}" aria-pressed="${v === builder.profile.stage}">${esc(label)}</button>`,
        )
        .join("")}</div>`;
    if (q === 2)
      content += `<p>${bt("qGoalsNote")}</p><div class="builder-goals">${builder.available.map((j) => `<button data-builder-goal="${j.id}" aria-pressed="${builder.blocks.includes(j.id)}">${esc(j.title)} ${builder.blocks.includes(j.id) ? icon("check") : icon("plus")}</button>`).join("")}</div>`;
    content += `<div class="builder-footer"><button class="button secondary" data-builder-prev ${q === 0 ? "disabled" : ""}>${iconLabel(bt("previous"))}</button><button class="button primary" data-builder-next ${builder.pending || (q === 2 && !builder.blocks.length) ? "disabled" : ""}>${iconLabel(q === 2 ? bt("propose") : bt("next"))}</button></div>`;
  }
  if (builder.preview && builder.plan?.questions?.length && !builder.pending) {
    const q = builder.plan.questions[0];
    content = `<p class="eyebrow">${bt("completeProfile")}</p><h2>${esc(q.title)}</h2><p>${esc(q.why)}</p>${q.kind === "country" ? `<form id="builder-answer-form"><label for="builder-country">${esc(q.title)}</label><input id="builder-country" name="country" minlength="2" maxlength="50" required autocomplete="off"><button class="button primary" type="submit">${iconLabel(bt("next"))}</button></form>` : `<div class="builder-goals">${q.options.map((o) => `<button data-answer-key="${q.key}" data-answer-value="${o.id}">${esc(o.title)}</button>`).join("")}</div>`}<p class="builder-note">${bt("unknownAnswer")}</p><button class="back-link" data-builder-restart>${bt("restart")}</button>`;
  }
  const nextQuestion = builder.plan?.questions?.[0]?.key;
  if (builder.preview && nextQuestion && nextQuestion !== builder.lastQuestion)
    window.scrollTo({ top: 0, behavior: "smooth" });
  builder.lastQuestion = nextQuestion;
  $("#builder-view").innerHTML =
    `<button class="back-link" data-home>${icon("arrow-left")} ${t("back")}</button><div class="builder-heading"><p class="eyebrow">STUDIAMI · ${t("yourJourney")}</p><h1>${bt("title")}</h1><p>${bt("intro")}</p></div><div class="builder-panel">${!builder.preview ? tabs : ""}${content}${builder.error ? `<p class="error-message" role="alert">${bt("error")}</p>` : ""}</div>`;
}
async function suggestBlocks() {
  const version = ++builderVersion;
  builder.pending = true;
  builder.error = false;
  renderBuilder();
  try {
    const r = await fetch("/api/plan/suggest", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ story: builder.story, profile: builderProfile() }),
    });
    if (!r.ok) throw new Error();
    const proposal = await r.json();
    if (version !== builderVersion || location.hash !== "#builder") return;
    builder.blocks = proposal.blocks;
    builder.profile = proposal.profile;
    builder.preview = true;
    await refreshBuilderCards();
  } catch {
    if (version === builderVersion) {
      builder.error = true;
      builder.pending = false;
      renderBuilder();
    }
  }
}
async function startCustom() {
  if (
    builder.pending ||
    builder.error ||
    !builder.blocks.length ||
    !builder.plan?.ready
  )
    return;
  const previousCustom = state.custom,
    previousProfile = { ...state.profile };
  state.custom = {
    blocks: [...builder.blocks],
    suppressed_blocks: [...builder.suppressed],
  };
  builder.pending = true;
  renderBuilder();
  const loaded = await changeProfile(builderProfile());
  builder.pending = false;
  if (!loaded) {
    state.custom = previousCustom;
    Object.assign(state.profile, previousProfile);
    store("studia-mi-profile", state.profile);
    builder.error = true;
    translate();
    renderBuilder();
    return;
  }
  store("studia-mi-custom", state.custom);
  builder.story = "";
  if (state.journeys.some((j) => j.id === "custom"))
    navigate(
      "custom",
      Math.min(
        frontier(state.journeys.find((j) => j.id === "custom")),
        state.journeys.find((j) => j.id === "custom").steps.length - 1,
      ),
    );
}
document.addEventListener("click", async (e) => {
  const el = e.target.closest("button");
  if (!el) return;
  if (el.dataset.answerKey) {
    builder.profile[el.dataset.answerKey] = el.dataset.answerValue;
    if (el.dataset.answerKey === "citizenship")
      builder.profile.citizenship_confirmed = true;
    await refreshBuilderCards();
    return;
  }
  if (el.dataset.builder) {
    await openBuilder(el.dataset.builder);
    return;
  }
  if (el.hasAttribute("data-resume-custom")) {
    navigate(
      "custom",
      Math.min(
        frontier(state.journeys.find((j) => j.id === "custom")),
        state.journeys.find((j) => j.id === "custom").steps.length - 1,
      ),
    );
    return;
  }
  if (el.dataset.builderMode) {
    builder.mode = el.dataset.builderMode;
    builder.preview = false;
    builder.error = false;
    ++builderVersion;
    builder.pending = false;
    renderBuilder();
    return;
  }
  if (el.dataset.builderPickProfile) {
    builder.profile.citizenship = el.dataset.builderPickProfile;
    builder.profile.citizenship_confirmed = true;
    renderBuilder();
    return;
  }
  if (el.dataset.builderPickStage) {
    builder.profile.stage = el.dataset.builderPickStage;
    renderBuilder();
    return;
  }
  if (el.dataset.builderGoal) {
    const id = el.dataset.builderGoal;
    builder.blocks = builder.blocks.includes(id)
      ? builder.blocks.filter((b) => b !== id)
      : [...builder.blocks, id];
    renderBuilder();
    return;
  }
  if (el.hasAttribute("data-builder-next")) {
    if (builder.question === 2) builder.preview = true;
    else builder.question++;
    await refreshBuilderCards();
    return;
  }
  if (el.hasAttribute("data-builder-prev")) {
    builder.question = Math.max(0, builder.question - 1);
    renderBuilder();
    return;
  }
  if (el.hasAttribute("data-builder-restart")) {
    await openBuilder(builder.mode);
    return;
  }
  if (el.hasAttribute("data-builder-start")) {
    await startCustom();
    return;
  }
  if (el.dataset.blockRemove) {
    builder.blocks = builder.blocks.filter((b) => b !== el.dataset.blockRemove);
    if (!builder.suppressed.includes(el.dataset.blockRemove))
      builder.suppressed.push(el.dataset.blockRemove);
    await refreshBuilderCards();
    return;
  }
  if (el.dataset.blockAdd) {
    if (!builder.blocks.includes(el.dataset.blockAdd))
      builder.blocks.push(el.dataset.blockAdd);
    builder.suppressed = builder.suppressed.filter(
      (id) => id !== el.dataset.blockAdd,
    );
    await refreshBuilderCards();
    return;
  }
  const id = el.dataset.blockUp || el.dataset.blockDown;
  if (id) {
    builder.blocks = builder.plan.block_summaries.map((j) => j.id);
    const i = builder.blocks.indexOf(id),
      next = i + (el.dataset.blockUp ? -1 : 1);
    if (next >= 0 && next < builder.blocks.length)
      [builder.blocks[i], builder.blocks[next]] = [
        builder.blocks[next],
        builder.blocks[i],
      ];
    await refreshBuilderCards();
  }
});
document.addEventListener("change", async (e) => {
  if (e.target.matches("[data-builder-profile]")) {
    const key = e.target.dataset.builderProfile;
    builder.profile[key] =
      key === "country" ? e.target.value.trim() || "unknown" : e.target.value;
    if (key === "citizenship") {
      builder.profile.citizenship_confirmed = true;
      builder.profile.country = null;
      builder.profile.visa = null;
      builder.profile.permit = null;
    }
    await refreshBuilderCards();
  }
});
document.addEventListener("input", (e) => {
  if (e.target.id === "builder-story") builder.story = e.target.value;
});
document.addEventListener("submit", async (e) => {
  if (e.target.id === "builder-answer-form") {
    e.preventDefault();
    builder.profile.country = $("#builder-country").value.trim();
    await refreshBuilderCards();
    return;
  }
  if (e.target.id === "builder-story-form") {
    e.preventDefault();
    if (!builder.pending) await suggestBlocks();
  }
});
translate();
renderSavedPath();

// Initialise after both scripts are ready, including saved composed plans.
loadJourneys().catch(() => {
  toast(t("loadError"));
  $("#journey-grid").innerHTML = `<p>${t("loadError")}</p>`;
});
