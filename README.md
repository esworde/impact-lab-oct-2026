# StudiaMI

> Claude Impact Lab Milano · 3 October 2026 · Track 01

**Your student life in Milan, one step at a time.** A bilingual web app for Italian and international students, with guided journeys and a Claude assistant grounded in public YesMilano and City of Milan sources.

## The problem

A student arriving in Milan must piece together housing, documents, transport and healthcare guidance across different websites, often in an unfamiliar language. StudiaMI provides a starting point, a checklist and help with the next action.

## What we built

- A home page with a question box and six illustrated journeys: arrival, housing, documents, transport, healthcare access and city life.
- Italian/international profiles, with EU/non-EU options where document routes differ. Language is a separate choice.
- Step-by-step cards, official source links, checklists saved locally, a summary and downloadable checklist.
- An assistant that receives the current journey/step and searches a SQLite FTS5 database before answering.
- Italian and English interfaces, responsive layouts, keyboard navigation and reduced-motion support.

Design references: [America.gov](https://america.gov/how-it-works), the supplied Italia Aperta screenshots and [Comune di Milano](https://www.comune.milano.it/) (municipal red and original logo). This is an independent hackathon prototype. The municipal logo identifies the design/source reference; the app does not claim to be an official municipal service.

## Where Claude works

**Model:** `claude-haiku-4-5-20251001`, chosen for speed and cost. Configurable through `CLAUDE_MODEL`.

At runtime Claude understands the question and the generic student profile, rewrites search queries into the corpus language, searches source sections, reads full guides when needed, explains the next actions in the selected language and can suggest a journey. Contextual help includes the step currently open.

- Prompts and tools: [`webapp/main.py`](webapp/main.py).
- Retrieval and versioned source storage: [`webapp/knowledge.py`](webapp/knowledge.py).
- Reviewed journey templates: [`webapp/journeys.py`](webapp/journeys.py).
- Every conversation turn first invokes `search_guides`. Results retain URLs, acquisition dates and declared content-update dates.
- Sources are displayed separately from generated prose. A notice is displayed when a consulted guide declares an update older than 180 days.
- Claude proposes guidance; students verify the original source and complete actions themselves on official services. Checkboxes never submit applications or approve eligibility.
- Responses are capped at 1,000 output tokens, tool loops at four model calls, concurrency at four conversations and the public demo at 200 chat requests/hour by default. Token usage and model-call counts are returned in the API response.
- Missing configuration and provider failures produce explicit errors; there are no fabricated AI responses.

## City data and sources

**30 public pages acquired with Firecrawl on 3 October 2026, indexed as 229 source sections.** The initial three-page Jina pilot has been replaced by Firecrawl content in the deployment snapshot.

| Source | Use |
| --- | --- |
| [YesMilano First Steps](https://studyandwork.yesmilano.it/en/study/how-to/first-steps) | Arrival and service navigation |
| [YesMilano student guides](https://studyandwork.yesmilano.it/en/study/how-to) | Tax code, visa/permit, residence, health, transport, SPID and student support |
| [YesMilano Rents](https://studyandwork.yesmilano.it/en/study/how-to/rents) and 10 linked detail pages | Contracts, deposit, payments, required documents and rental support |
| [Comune: cambio di residenza](https://www.comune.milano.it/servizi/anagrafe/cambio-di-residenza) | Municipal residence guidance |
| [Comune: dichiarazione TARI](https://www.comune.milano.it/servizi/tributi/tari-dichiarazione-di-occupazione-di-appartamenti-e-immobili) | Occupancy declaration guidance |
| [Comune: certificati anagrafici](https://www.comune.milano.it/servizi/anagrafe/certificati-anagrafici) | Certificates and official channels |

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
# Refresh up to 30 curated public pages with Firecrawl.
.venv/bin/python -m webapp.ingest --snapshot

# Refresh a smaller subset or a specific approved public source.
.venv/bin/python -m webapp.ingest --limit 3 --snapshot
.venv/bin/python -m webapp.ingest --url https://studyandwork.yesmilano.it/en/live_in_milano/rents-deposit --snapshot

# Verification
.venv/bin/python -m unittest discover -s webapp/tests -v
node --check webapp/static/app.js
```

## Railway deployment

The root [`Dockerfile`](Dockerfile) and [`railway.toml`](railway.toml) deploy a single FastAPI service. Mount a persistent Railway volume at `/data` and set `DATABASE_PATH=/data/knowledge.sqlite`. Use one replica: SQLite and a single attached volume are not a multi-replica design.

Set `ANTHROPIC_API_KEY`, `FIRECRAWL_API_KEY` and `CLAUDE_MODEL` on the service. Keys stay server-side. The container binds to Railway's `PORT`; `/health` is the healthcheck.

To refresh the deployed persistent database, run `python -m webapp.ingest` inside the service via `railway ssh`. Rebuilding the image alone does not overwrite existing pages on the persistent volume; startup only inserts missing seed pages. No refresh schedule has been configured yet.

## Verification

Seven automated tests cover atomic reindexing/version history, duplicate prevention, query escaping, real-corpus retrieval, profile-dependent journeys, API limits/errors and the Claude tool loop. A real Haiku call was tested against the indexed rental sources. Browser checks cover profile selection, step navigation and checklist persistence after reload.

## Privacy and limits

Only public source content is stored in SQLite. Generic preferences and checklist ticks are saved in browser storage; conversations remain in page memory and are not written to the app database. Questions and navigation context are sent to Anthropic for answering, subject to that provider's processing terms. The prototype asks users not to provide personal data. It does not upload documents, sign users into government services or submit applications. Application access logs are disabled; hosting/provider infrastructure has its own logging policies.

Before a broader release: review source freshness and journey wording with service owners, set an operating budget, configure authenticated operational refreshes and add multilingual retrieval evaluation.

## Hackathon materials

- [Selected Track 01](docs/TRACK_01.md)
- [Original hackathon hub README](docs/HACKATHON_HUB.md)
- [Challenge](CHALLENGE.md), [data catalogue](DATA.md), [rules](RULES.md), [submission](SUBMISSION.md)

## Licence

Code: MIT, see [LICENSE](LICENSE). Source guide content and the municipal logo remain attributed to their original publishers. Built at the Claude Impact Lab Milano for contribution to the Comune di Milano.
