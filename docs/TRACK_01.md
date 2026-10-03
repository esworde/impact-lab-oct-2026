# Track 01: personas e casi d'uso costruiti sui dati del Comune

**Stato:** traccia in fase di scelta per il progetto hackathon. La proposta è partire da Giulia come utente principale e valutare Reza come secondo caso, dopo aver completato il percorso principale.

Questa nota raccoglie l'analisi e le raccomandazioni fornite al team. L'analisi riporta l'incrocio di 12 dataset del portale del Comune: i 6 indicati in [DATA.md](../DATA.md) per la Track 01 e altri 6 trovati nel portale. Prima i numeri, poi le personas. Il brief di riferimento è in [CHALLENGE.md](../CHALLENGE.md).

## Cosa dicono i dati

| Dato | Numero | Fonte |
|---|---|---|
| Iscritti alle università milanesi (2024/25) | *212.214*, in crescita ogni anno dal 2019 | ds753 |
| Nuovi iscritti all'anagrafe nel 2024 | 46.953 persone: 42% dall'estero, 35% da altre regioni (quasi metà da Sud e Isole), 23% dalla Lombardia | ds1959 |
| Età dei nuovi iscritti (2024) | 25–34 anni: **39%**; 20–24 anni: solo **10%** | ds1957 |
| Chi usa il cambio di residenza online (2022, 10.194 risposte) | 25–34 anni: 35%; 18–24 anni: *6%*. Tutte le risposte sono in italiano | ds1702 |
| Chi risponde "il servizio non mi ha aiutato" | 25% degli italiani da altro Comune; *46%* degli stranieri dall'estero | ds1702 |
| Residenza per stranieri dall'estero (fine 2024) | NPS *28* (la TARI ha 54). Ostacoli: procedura complessa 38%, login 19%, trovare le informazioni 19% | ds2692, ds2693 |
| Prenotare un appuntamento (fine 2024) | Ostacoli: tempi di attesa 28%, trovare dove prenotare 17% | ds2690 |
| Sportelli dell'anagrafe | 12 sedi su 13 ricevono solo su appuntamento online, lun–ven 8:30–15:30, cioè in orario di lezione o di lavoro | ds549 |
| Residenti da Iran, India, Turchia, Pakistan | Raddoppiati o triplicati in 10 anni (Iran: da 1.303 a 3.960). È compatibile con l'arrivo di studenti internazionali, ma il dato non lo dice | ds74 |

*Il dato più importante: il "buco della residenza".* A Milano studiano 212mila universitari, ma i 20–24enni sono solo il 10% dei nuovi iscritti all'anagrafe e il 6% di chi usa il cambio di residenza.

- I fuorisede vivono a Milano senza spostare la residenza. Per l'anagrafe non esistono, quindi non ricevono l'email di benvenuto che il Comune manda ai nuovi residenti.
- Diventano visibili anni dopo, verso i 25–34 anni, quando iniziano a lavorare.
- È esattamente la domanda che il Comune ha lasciato aperta: "come sappiamo che qualcuno è appena arrivato?"

È una deduzione, perché nessun dataset conta i fuorisede. Il vostro team può confermarla per esperienza diretta.

## Le personas

### 1. Giulia, 19 anni, da Lecce, Politecnico, stanza a Città Studi: la fuorisede invisibile

È la prima volta che gestisce la burocrazia da sola. Tiene la residenza a Lecce (ISEE di famiglia per la borsa di studio, medico di base).

- *Casi d'uso:*
  - "Devo spostare la residenza a Milano?" Cosa cambia per borsa di studio, medico, TARI.
  - "Sono appena arrivata: cosa faccio, e in che ordine?" Medico temporaneo da non residente; TARI da occupante non residente (esiste una dichiarazione apposita, ds2693); abbonamento ATM under 27; quale sportello e in che orari.
  - "Il contratto dice 'TARI a carico del conduttore'." Claude legge la clausola di un contratto inventato e spiega cosa deve fare.
- *Cosa fa Claude mentre lei lo usa:* le fa 4–5 domande sulla sua situazione e costruisce una checklist personale ordinata, con le fonti. Sulla residenza le presenta pro e contro, e decide lei.
- *Ad AI spenta resta:* una pagina di link "Studiare a Milano".
- *Attenzione:* molte regole non sono del Comune (ATS per il medico, ente per il diritto allo studio, ATM). L'agente deve dire di chi è ogni regola e citarne la fonte.

### 2. Reza, 24 anni, da Teheran, magistrale al Politecnico: lo studente internazionale

Parla farsi e inglese, poco italiano. Ha 8 giorni per chiedere il permesso di soggiorno.

- *Casi d'uso:*
  - "I arrived yesterday: what first?" La sequenza in ordine: kit del permesso in uno dei 19 uffici postali abilitati (ds554), codice fiscale, contratto d'affitto, residenza, iscrizione al servizio sanitario.
  - "What documents do I need for residence?" È il servizio comunale con il giudizio peggiore (46% "non mi ha aiutato"): Claude lo spiega in parole semplici e indica lo sportello più vicino (ds549).
  - "Explain this letter from the Comune." Traduzione in farsi e versione semplificata.
- *Cosa fa Claude:* risponde nella sua lingua, mette i passaggi nell'ordine giusto e cita le fonti.
- *Ad AI spenta resta:* le stesse pagine, in italiano.
- *Attenzione:*
  - Il percorso YesMilano per studenti internazionali esiste già: bisogna costruirci sopra, non accanto.
  - Gran parte dei passaggi dipende dallo Stato (Questura, Agenzia delle Entrate): l'agente non decide mai e rimanda sempre alla fonte.

### 3. Marco, 27 anni, da Napoli, primo lavoro, casa a NoLo: il neo-residente

È il gruppo più numeroso nei dati: circa 4 nuovi iscritti all'anagrafe su 10.

- *Casi d'uso:*
  - "Ho chiesto la residenza: e adesso?" Le pratiche che seguono: dichiarazione TARI di occupazione, cambio del medico, permesso di sosta per residenti (ds700/ds701).
  - "Come faccio la dichiarazione TARI?" I problemi segnalati più spesso sono procedura complessa, informazioni difficili da trovare e linguaggio.
  - "Non trovo un appuntamento." Prima controlla se il certificato si può ottenere online: 16 dei 22 certificati più richiesti lo sono già.
- *Cosa fa Claude:* riparte da dove si ferma l'email di benvenuto e gli costruisce la checklist delle cose da fare dopo la residenza.
- *Attenzione:* si sovrappone all'email di benvenuto e al pilota TARI che esistono già, e rischia di scivolare nella Track 02.

### 4. Famiglie e lavoratori dall'estero (Egitto, Cina, Filippine, Perù)

È la persona con l'impatto potenziale più alto: 16.793 arrivi dall'estero nel 2024 e la barriera linguistica più forte. *Ve la sconsiglio*: nessuno di voi ha questa esperienza, e servirebbero esperti come patronati e servizi sociali.

## Confronto

| | Giulia | Reza | Marco |
|---|---|---|---|
| Quanti sono | 212mila studenti, invisibili all'anagrafe | parte dei circa 17mila arrivi l'anno dall'estero | circa 18mila iscrizioni l'anno tra 25 e 34 anni |
| Disagio misurato nei dati | non misurabile: il Comune non li vede | *il più alto* (46% non aiutati, NPS 28) | medio (25% non aiutati) |
| Cosa fa già il Comune | niente | percorso YesMilano | email di benvenuto, pilota TARI |
| Quanto conoscete il problema | *benissimo*: l'avete vissuto | abbastanza, grazie a chi lavora in università | bene: i tre neolaureati |
| Chi la raggiunge dal primo giorno | le università, al momento dell'iscrizione | YesMilano e uffici internazionali delle università | l'email di benvenuto |

## La mia raccomandazione

*Giulia come utente principale, Reza come secondo caso nella stessa demo.*

- *Perché Giulia:* è la persona che conoscete meglio ed è il punto cieco del Comune. Alla domanda "come sappiamo che è arrivata?" la risposta è: lo sanno le università. I due di voi che ci lavorano sono il canale per arrivare a lei fin dal primo giorno.
- *Perché Reza:* copre "chi non parla italiano", che è nella domanda del brief, e il servizio comunale con il giudizio peggiore. Aggiungetelo solo se verso le 14:30 il percorso di Giulia funziona dall'inizio alla fine.
- *Marco nel pitch:* presentatelo come versione 2. Quando Giulia si laurea e prende la residenza, lo stesso agente la accompagna.
- *Rischio con la giuria:* gli studenti italiani possono sembrare poco "fragili" rispetto al brief. Lo coprono Reza e un'accessibilità intesa come accesso a informazioni e procedure, in linguaggio semplice e anche a voce.

## Prossimi passi

1. Ognuno di voi scrive i 3 momenti in cui si è bloccato nel primo mese a Milano. Servono a confermare e ordinare i casi d'uso di Giulia; secondo DATA.md sono la fonte più preziosa.
2. Chiedete allo staff del Comune in sala cosa contengono l'email di benvenuto e il percorso YesMilano, per non costruire un doppione.
3. Per la demo scegliete un solo percorso: la checklist di Giulia, con dentro la decisione sulla residenza.

## Limiti dei dati

- I questionari raccolgono solo chi ha già usato il servizio online, quindi probabilmente mancano proprio le persone che non parlano italiano.
- Periodi coperti: iscrizioni 2020–2024; questionario sulla residenza 2022; questionari su residenza stranieri e appuntamenti settembre–dicembre 2024; questionario TARI 2024.
- L’analisi originale cita gli script `.context/data/analyze.py` e `.context/data/surveys.py` per riprodurre i calcoli. Non sono ancora presenti in questa repository: vanno aggiunti insieme ai dati utilizzati per documentare la sezione "City data and sources" del README.
