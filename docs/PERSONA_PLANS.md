# Giulia e Reza: un piano da confermare, un passo alla volta

Questi percorsi traducono le problematiche del documento sulle tre personas condiviso dal team il 3 ottobre 2026. Giulia e Reza sono casi inventati: non vengono richiesti o memorizzati dati personali. Lucía resta fuori da questa estensione; il profilo UE mantiene le guide generali.

| Problema | Giulia | Reza |
| --- | --- | --- |
| Status e arrivo poco visibile | Confronto tra situazione temporanea, domicilio temporaneo e trasferimento di residenza | Distinzione tra visto, richiesta del permesso e iscrizione anagrafica |
| Dipendenze tra enti | Diritto allo studio prima della scelta; Anagrafe e Tributi per gli adempimenti | Kit del permesso senza attendere il codice fiscale; ricevuta, documenti abitativi e canale residenza |
| Casa e TARI | Chi è il titolare, cosa è già dichiarato, eventuale variazione occupanti non residenti | Nuova occupazione e verifica con Tributi anche in parallelo alla residenza |
| Accesso, lingua e salute | Riferimento sanitario fuori sede; nessuna determinazione della copertura | Accesso senza presumere SPID, supporto Student Desk, chat anche in farsi su richiesta |

## I due piani

**Giulia, 6 passaggi:** borsa/ISEE e ufficio competente → confronto e scelta dello status → azione coerente con la scelta → contratto e responsabilità TARI → dichiarazione pertinente → riferimento sanitario. La scelta cambia il contenuto e la fonte del terzo passaggio. Se sceglie il domicilio temporaneo, può chiedere a Claude una bozza con soli segnaposti da controllare e firmare fuori dall’app.

**Reza, 8 passaggi:** passaporto/visto e referente universitario → kit e termine del permesso → consegna/ricevuta/convocazione → codice fiscale → documenti abitativi → procedura residenza per il titolo attuale → TARI → riferimenti per salute, sportelli e lingua. Il termine urgente del permesso compare subito sopra il piano. L’ordine dell’interfaccia non sospende le scadenze o impone di attendere per le attività che possono essere gestite in parallelo.

## Come funziona la validazione

Tutti i titoli sono visibili, come la scaletta di un piano. Il contenuto è accessibile solo per i passaggi già confermati e il primo ancora aperto. Per avanzare servono tutti i controlli spuntati, una scelta quando prevista, e un clic esplicito su **Conferma e sblocca il prossimo passo**. Le spunte da sole non sbloccano nulla. Il riepilogo si apre solo dopo l’ultima conferma.

Anche un URL diretto a un passaggio futuro o al riepilogo torna al primo passaggio aperto. Modificare un controllo confermato o una scelta revoca le conferme successive e richiede di ricontrollare le loro checklist. Preferenze, scelte e conferme rimangono nel browser; si separano per profilo e versione del piano. Le vecchie spunte dei percorsi generali vengono conservate, senza essere trasformate automaticamente in conferme.

La conferma è dello studente e riguarda il piano. Non certifica documenti, idoneità o presentazione di pratiche. Claude riceve il passaggio aperto, la scelta e i passaggi che lo studente dichiara confermati: può spiegare, cercare le fonti e preparare una bozza, ma non sblocca il piano.

## Fonti municipali verificate e indicizzate

Acquisite con Firecrawl il **3 ottobre 2026**; testo, URL e aggiornamento dichiarato sono nel corpus SQLite e nello snapshot `webapp/data/seed.json`. Le FAQ vengono isolate da navigazione e suggerimenti di altri articoli; i redirect alla homepage vengono rifiutati.

- [Domicilio temporaneo per studenti, KA-00595](https://servizicrm.comune.milano.it/centro-supporto/KA-00595/Domicilio-temporaneo-per-studenti-e-lavoratori): dichiarazione firmata e documento, durata un anno, residenza d’origine conservata; non applicabile a chi è già residente a Milano.
- [Cambio residenza per italiani, KA-00371](https://servizicrm.comune.milano.it/centro-supporto/KA-00371/Cambio-residenza-per-italiani-gia-in-Italia): ANPR e termine indicato dal Comune.
- [Residenza con permesso valido, KA-00598](https://servizicrm.comune.milano.it/centro-supporto/KA-00598/Documenti-per-residenza-con-permesso-di-soggiorno-valido): gli atti di famiglia tradotti/legalizzati non sono obbligatori per l’iscrizione in sé, ma servono per registrare parentela e certificazioni.
- [Documenti abitativi in affitto, KA-00329](https://servizicrm.comune.milano.it/centro-supporto/KA-00329/Residenza-stranieri-in-affitto-documenti-immobile): contratto ed eventuale ricevuta di registrazione.
- [Variazione occupanti non residenti TARI, KA-01960](https://servizicrm.comune.milano.it/centro-supporto/KA-01960/): dichiarazione di variazione e riferimento per chi non può utilizzare il servizio online.

Rimangono le guide YesMilano già indicizzate, incluso il permesso di soggiorno. Non assumiamo come verificati i numeri dei dataset riportati nel documento, gli effetti su ISEE/borse o le condizioni sanitarie individuali. Questi ultimi vengono indirizzati agli enti competenti.
