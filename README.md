# StudiaMI

> Claude Impact Lab Milano · 3 October 2026 · Track 01

**Live app:** https://studia-mi-production.up.railway.app

**Your student life in Milan, one step at a time.** A bilingual web app for Italian and international students, with guided journeys and a Claude assistant grounded in public YesMilano and City of Milan sources.

## The problem

A student arriving in Milan must piece together housing, documents, transport and healthcare guidance across different websites, often in an unfamiliar language. StudiaMI provides a starting point, a checklist and help with the next action.

## What we built

- A hero with **Create my journey**: a free-text story (one Haiku call) or guided questions (no model calls), with Giulia’s story as the main example. Targeted follow-ups collect missing facts before Claude generates the plan; explicit “to check” answers lead to verification with the relevant office.
- A Claude-authored plan: after the answers are collected, Haiku writes tailored step titles, actions, contextual checklist items and reasons, and chooses the order of optional services from indexed YesMilano and official-service evidence. The student reviews the proposal before starting. Changing residence choice regenerates subsequent actions with Claude, preserving the earlier prefix.
- An adaptive service graph: citizenship, study duration, accommodation, existing tax code/digital identity, residence, grant questions, healthcare coverage and visa/permit status change the services, steps and checklists. Submitted permit applications lead to follow-up rather than another kit; an existing tax code removes acquisition steps; accommodation already found removes search and viewing.
- Keeping residence, temporary registration and transferring residence assemble different municipal blocks. Changing this choice during the journey preserves confirmations before the decision and requires confirmation again from the decision onwards. The editable preview explains inclusions/exclusions and allows adding, removing and reordering optional blocks; prerequisite blocks stay first.
- **15 illustrated cases matching the YesMilano How To catalogue**, grouped into before arrival (3), first steps (8) and getting settled (4). Cases cover first steps, visa, rents, permit, tax code, transport, healthcare, residence, temporary registration, bank account, phone number, CAF/patronato, ID card, work and Italian courses.
- Italian/international profiles, with EU/non-EU options where document routes differ. Language is a separate choice.
- Sequential plans with a visible outline, locked future details, official sources, local checklists and explicit student confirmation before each next step. Direct links cannot skip confirmation; editing earlier decisions revokes dependent confirmations.
- Persona plans for **Giulia (6 steps)** and **Reza (8 steps)**, accessible through the home-page story buttons or the Italian/non-EU profile. Giulia’s status choice changes her next action; Reza’s permit deadline is highlighted from the start. [Plan design and verified sources](docs/PERSONA_PLANS.md).
- An assistant that receives the current journey/step and searches a SQLite FTS5 database before answering.
- Italian and English interfaces, responsive layouts, keyboard navigation and reduced-motion support.
- [Lucide](https://lucide.dev/) icons for interface controls, chat and status indicators; service cards keep their original illustrations. A pinned subset of Lucide Static 1.51.0 is served locally, with the [upstream licence](webapp/static/assets/LUCIDE-LICENSE.txt); no icon CDN or browser package dependency is required.

Design references: [America.gov](https://america.gov/how-it-works), the supplied Italia Aperta screenshots and [Comune di Milano](https://www.comune.milano.it/) (municipal red and original logo). This is an independent hackathon prototype. The municipal logo identifies the design/source reference; the app does not claim to be an official municipal service.

## Where Claude works

**Model:** `claude-haiku-4-5-20251001`, chosen for speed and cost. Configurable through `CLAUDE_MODEL`.

For free-text journey creation, Claude first selects card IDs and extracts explicit generic facts in one bounded call. Follow-ups collect missing answers. The new `/api/plan/generate` then calls Haiku to **write the action plan**, explain its priorities, generate contextual checklist items and order optional service blocks. The questionnaire also leads to AI generation. The student reviews the AI proposal before starting.

Generation reads indexed source excerpts and reviewed service constraints, with YesMilano as the primary source. The planner cannot omit required steps, reorder prerequisites, change decision options or replace canonical official links. Required confirmations stay attached alongside AI-authored contextual checks. Citations must refer to indexed sources. It does not invent services or determine eligibility. Generation failures show an explicit retry error; no fixed plan is presented as AI output.

Each planning call covers at most 15 steps and is capped at 4,000 output tokens. Typical focused plans use one call; larger plans use bounded batches. Each batch reads at most 20 relevant pages of 1,800 characters each, prioritising the sources for its required steps. Changing the residence branch asks Claude to rewrite subsequent steps while keeping the existing prefix. Saved plans resume without another model call. Plan generation shares the public daily model-request budget with story selection and chat. Implementation: [`webapp/planning.py`](webapp/planning.py).

Stories are not stored in the plan or SQLite; generic answers, selected blocks and the generated plan are saved locally. Composition progress is separate from individual-card progress and keyed by ordered blocks, excluded blocks, template/policy revisions and profile facts. Changing setup answers requires new confirmations; runtime residence choices preserve only the verified prefix. Older saved custom plans collect newly required missing answers before continuing.

At runtime Claude understands the question and the generic student profile, rewrites search queries into the corpus language, searches source sections, reads full guides when needed, explains the next actions in the selected language and can suggest a journey. Contextual help includes the step currently open, the student’s chosen route and self-reported confirmed steps. Claude explains the plan and can prepare an unofficial placeholder draft for temporary domicile; it cannot confirm or unlock a step.

- Prompts and tools: [`webapp/main.py`](webapp/main.py).
- Retrieval and versioned source storage: [`webapp/knowledge.py`](webapp/knowledge.py).
- Reviewed journey templates: [`webapp/journeys.py`](webapp/journeys.py).
- Every conversation turn first invokes `search_guides`. Results retain URLs, acquisition dates and declared content-update dates.
- Sources are displayed separately from generated prose. A notice is displayed when a consulted guide declares an update older than 180 days.
- Claude proposes guidance; students verify the original source and complete actions themselves on official services. Checkboxes never submit applications or approve eligibility.
- Responses are capped at 1,000 output tokens, tool loops at four model calls, concurrency at four conversations and the public demo at 200 model requests/day (chat, story selection and plan generation combined) by default. Token usage and model-call counts are returned in the API response.
- Missing configuration and provider failures produce explicit errors; there are no fabricated AI responses.

## City data and sources

**46 public pages acquired with Firecrawl on 3 October 2026, indexed as 311 source sections.** YesMilano is the primary source; competent public services provide supporting instructions. The initial three-page Jina pilot has been replaced by Firecrawl content in the deployment snapshot.

| Source | Use |
| --- | --- |
| [YesMilano First Steps](https://studyandwork.yesmilano.it/en/study/how-to/first-steps) | Arrival and service navigation |
| [YesMilano student guides](https://studyandwork.yesmilano.it/en/study/how-to) | Tax code, visa/permit, residence, health, transport, SPID and student support |
| [YesMilano Rents](https://studyandwork.yesmilano.it/en/study/how-to/rents) and 10 linked detail pages | Contracts, deposit, payments, required documents and rental support |
| [Comune: cambio di residenza](https://www.comune.milano.it/servizi/anagrafe/cambio-di-residenza) | Municipal residence guidance |
| [Comune: dichiarazione TARI](https://www.comune.milano.it/servizi/tributi/tari-dichiarazione-di-occupazione-di-appartamenti-e-immobili) | Occupancy declaration guidance |
| [Comune support FAQs](docs/PERSONA_PLANS.md) | Temporary student domicile, Italian residence transfer, valid-permit and housing documents, non-resident TARI occupants |
| [Comune: certificati anagrafici](https://www.comune.milano.it/servizi/anagrafe/certificati-anagrafici) | Certificates and official channels |
| [Additional YesMilano pages](https://studyandwork.yesmilano.it/en/study/universities-in-milano) | Universities, temporary-residence declaration, community services, emergency contacts and getting around |
| [Comune: library registration](https://servizicrm.comune.milano.it/centro-supporto/KA-02415/Iscrizione-ad-una-biblioteca-pubblica-lettura) and [Study in Milan](https://www.comune.milano.it/en/servizi/giovani/study-in-milan) | Supporting student and library services |
| [MAECI: Visas and permits](https://italiana.esteri.it/italiana/opportunity/studying-in-italy/visas-and-permits/) | Study stays up to 90 days, declaration-of-presence verification and official visa portal |

The catalogue mapping, original card titles, groups, guide URLs and Firecrawl consultation date are in [`webapp/data/how-to-catalog.json`](webapp/data/how-to-catalog.json). The list matches [YesMilano How To](https://www.yesmilano.it/en/study/how-to), including Bank account, Phone number and Work while studying. EU-only/non-EU routes show scope orientation for other or unspecified profiles; procedural steps are available when the appropriate generic profile is selected. This is navigation, not an eligibility determination.

The full acquisition snapshot and provenance are in [`webapp/data/seed.json`](webapp/data/seed.json). This is a curated student corpus, not a complete index of YesMilano. Linked PDFs have not been ingested. Fetch dates are not content-update dates: for example, the rental overview declares an update of 27 July 2023.

Refreshes atomically replace each page's search sections and preserve old text versions when the content hash changes. A failed scrape keeps the previous version. Sources without declared update dates have unknown content freshness. No live-web fetch is performed during chat; current fees, deadlines and requirements need checking at the linked competent service.

## Run it

Python 3.12, SQLite FTS5 and the dependencies below are sufficient; no Node build is required.

```bash
cp .env.example .env
# Add ANTHROPIC_API_KEY and FIRECRAWL_API_KEY; never commit .env.
uv venv .venv
uv pip install --python .venv/bin/python -r webapp/requirements.lock
.venv/bin/python -m uvicorn webapp.main:app --reload --port 8000 --no-access-log
```

Open `http://127.0.0.1:8000`. The public snapshot seeds the database on first startup. Without an Anthropic key, journeys and sources work; chat reports that it is unavailable.

```bash
# Refresh the 46 curated public pages with Firecrawl.
.venv/bin/python -m webapp.ingest --snapshot

# Refresh a smaller subset or a specific approved public source.
.venv/bin/python -m webapp.ingest --limit 3 --snapshot
.venv/bin/python -m webapp.ingest --url https://studyandwork.yesmilano.it/en/live_in_milano/rents-deposit --snapshot

# Verification
.venv/bin/python -m unittest discover -s webapp/tests -v
node webapp/tests/test_plan.cjs
node --check webapp/static/app.js
```

## Railway deployment

The root [`Dockerfile`](Dockerfile) deploys a single FastAPI service. Configure `/health` as its healthcheck in Railway. Mount a persistent Railway volume at `/data` and set `DATABASE_PATH=/data/knowledge.sqlite`. Use one replica: SQLite and a single attached volume are not a multi-replica design.

Set `ANTHROPIC_API_KEY`, `FIRECRAWL_API_KEY` and `CLAUDE_MODEL` on the service. Keys stay server-side. The container binds to Railway's `PORT`; this deployment sets `PORT=8000` and routes the public domain to port 8000. Railway's former `railway.toml` configuration has been deprecated; service settings are applied directly through Railway.

To refresh the deployed persistent database, run `python -m webapp.ingest` inside the service via `railway ssh`. Rebuilding the image alone does not overwrite existing pages on the persistent volume; startup only inserts missing seed pages. No refresh schedule has been configured yet.

## Verification

Twenty-six Python tests and the JavaScript plan-state checks cover retrieval/version history, API errors and limits, persona routes, catalogue coverage and the Claude tool loop. Adaptive tests compare actual services, sources and checklists for keep/temporary/transfer choices; short, pending and valid non-EU stays; EU duration; existing residence; relevant missing questions; and bank documents. All 15 cases across four citizenship profiles and four duration variants retain unique steps and indexed primary sources.

Browser checks cover explicit confirmation and locked direct URLs, adaptive follow-ups, Giulia’s three residence branches, preservation of earlier confirmations, revalidation of later steps, draft/chat context, saved progress after reload and mobile overflow. A non-EU student with a submitted permit follows the existing application, and a known tax code removes acquisition steps. Previous catalogue checks opened all 15 cases. AI-planning tests cover authored actions, mandatory confirmations, indexed citations, prerequisite order, failures, bounded batches and preservation of the prefix during replanning. Real Haiku calls exercise source retrieval, placeholder drafts, story extraction and personalized plan generation.

## Privacy and limits

Only public source content is stored in SQLite. Generic preferences, selected card IDs, plan choices, checklist ticks and self-confirmation timestamps are saved in browser storage; conversations remain in page memory and are not written to the app database. Stories, questions and navigation context are sent to Anthropic for selection or answering, subject to that provider's processing terms. The prototype asks users not to provide personal data. It does not upload documents, sign users into government services or submit applications. Application access logs are disabled; hosting/provider infrastructure has its own logging policies.

Before a broader release: review source freshness and journey wording with service owners, set an operating budget, configure authenticated operational refreshes and add multilingual retrieval evaluation.

## Hackathon materials

- [Selected Track 01](docs/TRACK_01.md)
- [Original hackathon hub README](docs/HACKATHON_HUB.md)
- [Challenge](CHALLENGE.md), [data catalogue](DATA.md), [rules](RULES.md), [submission](SUBMISSION.md)

## Licence

Code: MIT, see [LICENSE](LICENSE). Source guide content and the municipal logo remain attributed to their original publishers. Built at the Claude Impact Lab Milano for contribution to the Comune di Milano.
