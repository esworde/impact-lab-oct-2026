# Milano Fascicolo Demo

Proof of concept locale, un solo utente e un solo processo. Python **3.12**, FastAPI,
Playwright e HTML/CSS/JS vanilla. Nessun database.

## Avvio (macOS / Linux)

Da questa cartella, con `python3 --version` corrispondente a Python 3.12
(altrimenti usa `python3.12` nel primo comando):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
uvicorn app:app --reload
```

Apri **http://127.0.0.1:8000**. Per provare subito senza il Comune:

```bash
MOCK_MODE=true uvicorn app:app --reload
```

Ferma prima l'altro server con Ctrl+C. Nel mock non viene avviato alcun browser
Playwright: il pulsante mostra i due pagamenti fittizi richiesti. Su Linux serve
una sessione grafica per il browser reale; eventuali librerie di sistema mancanti
sono indicate da `playwright install-deps chromium`.

## Accesso reale

Clicca **Collega Fascicolo del Cittadino** e completa personalmente SPID/CIE
nella finestra Chromium visibile. Nessuna parte del login viene automatizzata.
La demo cerca un indicatore UI di accesso, apre Pagamenti e legge la vista corrente.
Il pulsante **Verifica accesso** (o **Riprendi** dopo un errore) ricarica le
correzioni in `fascicolo.py` mantenendo lo stesso browser e la stessa sessione.
Per adattare i selettori durante il login usa il server **senza `--reload`**:
`uvicorn app:app`. Il reload automatico del server chiuderebbe invece la sessione.
La diagnostica locale `POST /api/inspect`, protetta come le altre azioni, legge
solo segnali UI e struttura delle tabelle sul dominio del Fascicolo; non legge
righe di pagamento, valori form, cookie, token o DOM dei siti di autenticazione.
Dopo 10 minuti l'attesa si ferma, ma il browser resta aperto: usa **Riprendi**.
**Scollega e cancella dati** chiude la sessione e svuota i risultati in memoria.
Ctrl+C e il riavvio di Uvicorn chiudono il browser attraverso il lifespan.
Chiudere soltanto la scheda della webapp non termina il server: usa Scollega o Ctrl+C.

**Flusso reale verificato il 3 ottobre 2026:** dopo l'accesso manuale sono stati
recuperati 4 pagamenti dalla vista corrente e visualizzati nella tabella locale,
con data, descrizione, importo e stato. Nessun dettaglio personale è salvato nei file.
La sezione `PORTAL ADAPTER` all'inizio di `fascicolo.py` centralizza i selettori:
`LOGIN_MARKERS`, `PAYMENT_NAMES`, `CONTENT_SELECTOR`, `PAYMENTS_REGION_SELECTOR`,
`PAYMENT_CARD_SELECTOR`, `FIELD_LABELS` e `EMPTY_MESSAGES`.
Sono verificati il link e l'heading Pagamenti, il contenitore `.items-page .items-body`,
le schede `.item-card`, il titolo `.item-title` e lo stato `.item-stato .chip-text`.
I selettori alternativi restano candidati semantici.
Se necessario apri manualmente Pagamenti e premi Riprendi. Per cards configura
un selettore osservato nella UI; i valori sono riconosciuti solo da etichette esplicite.
Un formato sconosciuto produce un errore, non un falso elenco vuoto.
Campi incerti restano `None`; il testo visibile della riga è consultabile in tabella.
La demo non cambia filtri e non percorre pagine successive o liste virtualizzate:
mostra solo le righe attualmente renderizzate, non garantisce l'intero archivio.

## Verifica API pubbliche — 3 ottobre 2026

Non è stata trovata documentazione pubblica sufficiente per autenticare un cittadino
con OAuth/OIDC e ottenere i suoi pagamenti. Non equivale a dimostrare che non esistano
servizi riservati. Fonti controllate:

- [Fascicolo del Cittadino](https://www.comune.milano.it/servizi/fascicolo-del-cittadino): ingresso ufficiale e SPID/CIE; link verificato a `https://fascicolo.comune.milano.it/`.
- [Archivio pagamenti e rimborsi](https://www.comune.milano.it/servizi/tributi/archivio-pagamenti-e-rimborsi): consultazione attraverso la voce Pagamenti.
- [Portale del Dato / API](https://dati.comune.milano.it/web/portale-del-dato/governo-dei-dati/cdm-api): API CKAN di dati aperti, senza documentazione per i pagamenti personali.
- [EDU](https://dati.comune.milano.it/en/web/portale-del-dato/utilizza-i-dati/ecosistema-digitale-urbano): API Manager con adesione e accessi regolati.
- [Catalogo collegato da EDU](https://mde.comune.milano.it/devportal/apis): nella verifica pubblica non ha esposto un catalogo leggibile utilizzabile per questo flusso.

Perciò è implementata **Browser-assisted demo**, senza endpoint API del Comune,
client OAuth inventati o analisi del traffico di rete.

## Privacy e limiti

Contesto Chromium non persistente (`headless=False`); nessuna lettura/esportazione
di cookie, token, storage, password, OTP o PIN. Nessun salvataggio di HTML,
screenshot, tracce o dettagli dei pagamenti nei log. Nessuna richiesta HTTP diretta
al portale: soltanto navigazione e testo UI. Le risposte locali non sono memorizzabili
in cache; il frontend usa `textContent`. TLS e protezioni del portale restano attivi.

Mantieni il bind predefinito `127.0.0.1`, senza proxy, tunnel o più worker.
La demo rifiuta host/origini esterne e richieste di modifica estranee alla UI locale.
Il browser può creare file tecnici temporanei gestiti da Playwright; la chiusura
ordinaria li rimuove. Un arresto forzato del sistema/SIGKILL non consente garanzie
di pulizia: non è una soluzione di conservazione sicura o production-ready.

## Test

```bash
MOCK_MODE=true python -m unittest discover -s tests -v
python tests/check_browser.py
```

Il secondo comando apre un browser temporaneo con soli contenuti sintetici e
verifica che campi form e testo nascosto non siano estratti. Non accede al Comune.
Con il server mock già avviato, `python tests/check_http.py` verifica anche HTTP,
collegamento, richieste duplicate, cancellazione dati e restrizioni di origine.

Verificati: 10 test unitari, parser DOM sul formato delle schede, test HTTP
iniziali e visualizzazione dei 4 pagamenti reali nella UI.
