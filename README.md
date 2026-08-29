# Asta Live – Guida all’utilizzo
this time it is not 3 pigs, but giana

## Introduzione

**Asta Live** è uno strumento web per seguire un’asta di fantacalcio in tempo reale e mantenere aggiornati, durante l’asta, i dati necessari a monitorare la propria rosa, i partecipanti avversari e il comportamento del mercato.

L’applicazione combina inserimento manuale dei dati e calcoli automatici. L’utente deve soprattutto registrare gli eventi che osserva durante l’asta: acquisti, costi reali, assegnazioni agli avversari, eventuali Extra, preferiti e note. A partire da queste informazioni il tool aggiorna automaticamente dashboard, residui, slot, indicatori e stime come **MAX_D**.

> **Importante:** questa guida descrive il funzionamento del tool senza riportare soglie, coefficienti, budget predefiniti, valori numerici di esempio o indicazioni strategiche rigide. I dettagli quantitativi del motore rimangono intenzionalmente generici.

---

## A cosa serve il tool

Il tool è pensato per essere utilizzato mentre l’asta è in corso, con l’obiettivo di avere sempre sotto controllo:

- il budget e la sua distribuzione tra i ruoli;
- gli slot disponibili e quelli già occupati;
- la spesa effettiva della propria squadra;
- la composizione della propria rosa;
- gli acquisti degli altri partecipanti;
- il budget residuo degli avversari;
- la pressione competitiva ancora presente sui diversi ruoli;
- la disponibilità residua dei giocatori per categoria;
- la stima **MAX_D** per i giocatori ancora liberi;
- il livello di supporto dei dati osservati alla stima dinamica;
- eventuali intervalli indicativi quando il mercato osservato è molto eterogeneo.

Il tool non sostituisce il giudizio dell’utente: raccoglie dati e li usa per produrre indicatori coerenti con lo stato corrente dell’asta.

---

## Come funziona, in pratica

Durante l’utilizzo, il flusso tipico è:

1. aprire l’applicazione e superare l’eventuale schermata di accesso;
2. controllare le **Impostazioni Lega**;
3. verificare che budget, slot, distribuzione del budget e partecipanti siano corretti;
4. durante l’asta, aggiornare il giocatore interessato cambiandone lo stato;
5. inserire il **Costo Reale** quando viene conosciuto;
6. assegnare gli acquisti degli altri al relativo partecipante;
7. registrare gli eventuali **Extra**;
8. usare il **Control Panel** per monitorare la situazione complessiva;
9. usare **Mia Squadra**, **Salvati**, **Altre Squadre** e **Dati su Altri Giocatori** per consultare il dettaglio;
10. creare periodicamente un **Backup** per poter ripristinare il lavoro in caso di necessità.

L’applicazione salva automaticamente le modifiche nel browser, quindi nella normale operatività non è necessario premere un pulsante di salvataggio dopo ogni modifica.

---

# Accesso e protezione della schermata

## Accesso iniziale

L’app può mostrare una schermata **Accesso Riservato** prima di consentire l’utilizzo dell’interfaccia.

È necessario inserire la parola chiave prevista dall’applicazione e confermare l’accesso.

Una volta effettuato correttamente, l’accesso viene ricordato da quel browser e non viene normalmente richiesto di nuovo nello stesso contesto.

### Nota di sicurezza

La schermata di accesso è un filtro applicativo e non deve essere considerata una misura di sicurezza forte; pertanto il meccanismo serve soprattutto a impedire l’uso occasionale o accidentale dell’app, non a proteggere dati da chi abbia pieno accesso al codice sorgente o agli strumenti del browser.

---

## Blocco dello schermo

Il pulsante **Lock** consente di bloccare l’interfaccia mentre l’app resta aperta.

Al primo utilizzo del blocco viene richiesta una password da scegliere. La password non viene memorizzata in chiaro: il browser conserva il relativo hash.

Dopo aver impostato la password, lo schermo può essere bloccato e successivamente sbloccato inserendo la stessa password.

Il blocco viene inoltre mantenuto durante il refresh della pagina nella sessione della scheda in cui è stato attivato.

### Cambiare la password

Quando esiste già una password di blocco, compare il pulsante **Cambia Password**.

L’operazione reimposta la password memorizzata: al successivo blocco sarà possibile sceglierne una nuova.

### Limite importante

Anche il lock dello schermo è una protezione visiva, non una protezione crittografica completa. I dati dell’applicazione rimangono nel browser e una persona con accesso tecnico agli strumenti di sviluppo del browser potrebbe aggirare il blocco.

---

# Navigazione dell’interfaccia

La barra principale contiene le sezioni operative dell’app.

## Control Panel

È la schermata di monitoraggio generale. Mostra in un unico punto i principali indicatori della situazione corrente, tra cui:

- crediti spesi;
- crediti residui;
- percentuale di budget già utilizzata;
- stato degli slot complessivi;
- stato dell’asta;
- costo atteso per completare la rosa;
- margine rispetto al costo atteso;
- numero di giocatori acquistati;
- prezzo medio reale della propria squadra;
- confronto tra spesa media propria e degli altri;
- eventuale riserva residua dedicata agli acquisti della categoria prevista dalla configurazione.

Il Control Panel contiene anche un quadro dettagliato per ruolo e una rappresentazione della composizione residua dei giocatori liberi.

---

## Schede P, D, C, A

Le schede dei ruoli contengono l’elenco dei giocatori appartenenti al ruolo selezionato.

Le quattro sigle rappresentano i reparti previsti dal modello dell’asta:

- **P** = portieri;
- **D** = difensori;
- **C** = centrocampisti;
- **A** = attaccanti.

All’interno di ogni scheda è possibile filtrare, ordinare e aggiornare i giocatori.

---

## Extra

La scheda **Extra** serve per registrare elementi che consumano slot o generano spesa senza essere rappresentati come normali giocatori della lista.

L’applicazione prevede Extra sia per la propria squadra sia, in modo separato, per gli avversari.

Esempi concettuali di Extra gestiti dal tool sono multe, scambi o compensazioni.

---

## Impostazioni Lega

Questa è la sezione da controllare prima di iniziare l’asta.

Qui vengono configurati:

- il budget iniziale della lega;
- gli slot previsti per ciascun ruolo;
- la quota di budget destinata a ciascun ruolo;
- l’eventuale riserva dedicata a una particolare categoria di acquisto;
- il numero dei partecipanti avversari;
- il nome di ciascun avversario.

Queste informazioni non sono solo descrittive: costituiscono la base dei calcoli del motore e determinano, tra le altre cose, i target di spesa, la disponibilità degli slot e la capacità economica residua attribuita ai singoli avversari.

---

## Utente

La sezione **Utente** contiene due sotto-schede.

### Mia Squadra

Mostra i giocatori assegnati alla propria squadra raggruppati per ruolo.

Per ogni giocatore viene visualizzato il costo reale. Gli eventuali Extra associati al ruolo vengono mostrati insieme agli altri elementi della rosa.

Questa sezione è principalmente di consultazione e verifica: la modifica dello stato e del costo dei singoli giocatori viene normalmente fatta nelle schede P/D/C/A.

### Salvati

Mostra i giocatori contrassegnati come **preferiti** tramite la stella.

I preferiti sono una funzione di organizzazione personale e non modificano le formule del motore.

Da qui è possibile:

- riconoscere rapidamente i giocatori d’interesse;
- vedere il relativo MAX_D;
- vedere lo stato del giocatore;
- vedere l’eventuale indicazione di giocatore molto conteso;
- aprire e modificare le note.

---

## Altri Giocatori

La sezione **Altri Giocatori** contiene due sotto-schede.

### Altre Squadre

Ogni avversario è mostrato separatamente.

Per ogni partecipante è possibile vedere:

- il residuo del budget;
- il numero di slot occupati e disponibili;
- i giocatori assegnati per ruolo;
- il costo reale dei singoli giocatori;
- la spesa complessiva per giocatori;
- gli Extra dell’avversario;
- la spesa totale risultante.

Questa vista è particolarmente utile per controllare che gli acquisti osservati siano assegnati al partecipante corretto.

### Dati su Altri Giocatori

Mostra, per ogni avversario:

- il budget residuo complessivo;
- per ciascun ruolo, gli slot occupati rispetto al totale previsto;
- i crediti spesi in quel ruolo.

Questa vista non introduce nuovi dati: riassume in forma più compatta informazioni già registrate nelle altre sezioni.

---

# Preparazione iniziale

## Verificare la configurazione della lega

Prima di registrare gli acquisti è importante passare da **Impostazioni Lega**.

### Budget iniziale

Inserire il budget previsto dalla propria lega.

Il budget è usato dal motore per costruire i target economici dei vari ruoli e per determinare quanto margine economico rimane disponibile.

### Slot per ruolo

Indicare la composizione prevista della rosa per ciascun ruolo.

Questi valori determinano la quantità di posti che devono essere riempiti dalla propria squadra e sono utilizzati anche per valutare quanti posti restano da riempire agli avversari.

### Distribuzione del budget

Per ogni ruolo viene indicata la percentuale del budget che si desidera associare a quel reparto.

Il tool controlla la somma delle percentuali e avvisa quando la configurazione non rappresenta l’intero budget.

Il motore continua comunque a usare i valori inseriti: l’avviso serve a rendere evidente che la configurazione non è perfettamente quadrata.

### Riserva per una categoria specifica

È possibile configurare una quota di budget destinata a eventuali acquisti della categoria prevista dalla riserva.

La riserva viene considerata dal motore come disponibilità pianificata e viene sottratta dal budget di pacing solo nella misura in cui è ancora non consumata.

### Partecipanti avversari

Configurare l’elenco degli avversari che partecipano alla lega e assegnare un nome a ciascuno.

Questi nomi compariranno nelle tendine di assegnazione degli acquisti e nelle viste delle altre squadre.

---

# Come registrare un acquisto

La registrazione corretta degli acquisti è la parte più importante dell’utilizzo quotidiano.

## Stato del giocatore

Nelle schede P/D/C/A ogni giocatore ha uno stato:

- **L – Libero**: il giocatore non è ancora assegnato;
- **M – Mio**: il giocatore è stato acquistato dalla propria squadra;
- **A – Altri**: il giocatore è stato acquistato da un avversario.

Lo stato viene modificato direttamente nella riga del giocatore.

### Impostare “Mio”

Se acquisti il giocatore tu:

1. seleziona **Mio**;
2. inserisci il **Costo Reale** appena il prezzo è definitivo;
3. controlla il Control Panel per verificare l’aggiornamento delle metriche.

Il giocatore entra automaticamente nella sezione **Mia Squadra** e contribuisce ai calcoli della spesa e degli slot occupati.

### Impostare “Altri”

Se il giocatore viene acquistato da un partecipante avversario:

1. seleziona il relativo avversario dal campo dedicato;
2. il giocatore viene marcato automaticamente come **Altri**;
3. inserisci il **Costo Reale** quando il prezzo è disponibile.

L’assegnazione a un avversario è importante perché consente al motore di distinguere la capacità economica dei singoli partecipanti e di usare il concorrente più competitivo come riferimento quando i dati disponibili lo consentono.

### Riportare un giocatore a “Libero”

Per annullare un’assegnazione, rimuovere lo stato attuale fino a tornare a **Libero**.

Quando un giocatore viene riportato a Libero, il tool azzera il costo reale associato a quella vendita e rimuove la relativa transazione dallo storico utilizzato dal motore.

---

# Inserire il costo reale

Il campo **Costo Reale** rappresenta il prezzo effettivamente osservato nell’asta.

Il campo è modificabile direttamente dalla tabella del ruolo.

Il costo reale viene usato per:

- aggiornare la spesa della propria squadra quando lo stato è Mio;
- aggiornare la spesa del relativo avversario quando lo stato è Altri;
- aggiornare le statistiche di spesa;
- alimentare lo storico delle transazioni;
- fornire dati osservati al motore MAX_D;
- contribuire alle informazioni dinamiche sul comportamento del mercato.

Il costo reale non è richiesto per i giocatori rimasti Liberi.

### Buona pratica operativa

Durante l’asta conviene registrare il costo reale appena l’assegnazione è certa. In questo modo le metriche e le stime si aggiornano con i dati più recenti disponibili.

---

# Assegnare correttamente gli avversari

Quando un acquisto è contrassegnato come **Altri**, è molto importante assegnarlo alla persona corretta.

Gli acquisti degli avversari non sono più trattati esclusivamente come una massa indistinta: il tool mantiene statistiche separate per partecipante.

L’assegnazione individuale permette di ricostruire:

- il budget residuo di ciascun avversario;
- gli slot ancora disponibili;
- gli acquisti per ruolo;
- gli Extra del singolo partecipante;
- la capacità massima sostenibile di offerta del singolo partecipante.

### Acquisto avversario con costo noto ma avversario non assegnato

Il tool gestisce anche il caso in cui sia stato registrato un acquisto di un avversario e il relativo costo, ma non sia ancora stato indicato chi lo ha comprato.

In questa situazione l’applicazione mostra un avviso e ricorre temporaneamente alla logica aggregata prevista dal motore, perché non può inventare quale partecipante abbia effettuato l’acquisto.

Per ottenere la stima più precisa possibile è quindi preferibile completare l’assegnazione all’avversario corretto.

---

# MAX_D: che cosa significa

## Definizione pratica

**MAX_D** è il valore massimo suggerito dal motore per un giocatore ancora libero.

Non deve essere interpretato come una previsione certa del prezzo finale o come il secondo prezzo di un’asta. È un tetto operativo costruito in base allo stato corrente dei dati disponibili.

Il suo obiettivo è tenere insieme:

- la struttura della propria rosa;
- il budget residuo;
- le esigenze future per ruolo;
- la disponibilità residua del mercato;
- la distribuzione delle categorie;
- i prezzi realmente osservati negli acquisti degli altri;
- il comportamento recente del mercato;
- la pressione esercitata dagli avversari;
- la posizione del giocatore rispetto agli altri superstiti della stessa categoria;
- il livello di riempimento del ruolo;
- la convenienza relativa a spostare budget verso altre categorie del ruolo.

---

## Quando cambia MAX_D

Il motore parte dal valore di base associato al giocatore e applica correzioni dinamiche solo quando il contesto dell’asta lo richiede.

Le correzioni comprendono, a livello concettuale:

### Inflazione osservata

Confronta ciò che si sta pagando realmente sul mercato con ciò che il modello si attendeva per quel contesto.

La correzione è sensibile alla categoria del giocatore, in modo da evitare che acquisti molto economici appartenenti a categorie diverse alterino inutilmente la valutazione della categoria corrente.

### Pressione degli avversari

Tiene conto di quanti slot devono ancora essere coperti dagli altri partecipanti nel ruolo e della loro capacità economica residua osservata.

La pressione non viene quindi interpretata solo come quantità di posti mancanti: viene anche confrontata con la capacità di spesa ancora disponibile.

### Momentum del mercato

Osserva il comportamento recente delle transazioni e verifica se, nel ruolo considerato, il mercato sta mostrando un’accelerazione o un rallentamento rispetto al proprio andamento storico.

Le transazioni più recenti hanno maggiore influenza rispetto a quelle più lontane, con un decadimento graduale.

### Posizione del giocatore nella propria categoria

Il giocatore viene confrontato con gli altri giocatori ancora liberi della stessa categoria e dello stesso ruolo.

Quando una categoria diventa più scarsa, la posizione relativa dei migliori superstiti acquista maggiore rilevanza.

### Sazietà

Il motore tiene conto del fatto che alcune esigenze di composizione della rosa possano essere già state coperte.

Se una determinata categoria è già sufficientemente rappresentata nella propria squadra, la priorità di un ulteriore acquisto della stessa categoria viene ridotta.

È presente anche un effetto più generale legato al riempimento fisico del ruolo, indipendente dalla categoria specifica.

### Riallocazione tra categorie

Il motore può ridurre il cap quando i dati osservati indicano che completare una determinata area del ruolo sta diventando sproporzionatamente costoso rispetto all’alternativa ancora disponibile nello stesso ruolo.

Questa componente rappresenta un confronto economico interno al ruolo, non una previsione di prezzo assoluta.

### Contesa manuale

L’utente può contrassegnare manualmente un giocatore come **molto conteso**.

Il flag comunica al motore un’informazione qualitativa che potrebbe non emergere dai dati osservati.

È un’informazione manuale e non una prova che il giocatore verrà effettivamente pagato oltre le aspettative.

---

# Confidenza di MAX_D

Accanto al MAX_D può comparire un indicatore di **confidenza**.

La confidenza non misura se il MAX_D sia “giusto” o “sbagliato”. Indica quanto della componente dinamica della stima è sostenuta da dati reali osservati nell’asta.

In generale:

- una confidenza bassa indica che il motore si appoggia soprattutto alla componente strutturale di base;
- una confidenza più alta indica che sono disponibili più osservazioni utili per le correzioni dinamiche;
- la confidenza elevata non significa che il prezzo finale sia certo.

Questo indicatore deve quindi essere letto come **qualità/quantità dell’evidenza osservata dietro le correzioni**, non come probabilità di successo della stima.

---

# Intervallo indicativo accanto a MAX_D

In presenza di sufficiente eterogeneità nei prezzi osservati può comparire un intervallo indicativo accanto al MAX_D.

L’intervallo serve a rendere visibile l’incertezza introdotta dalla dispersione dei dati.

Non rappresenta:

- una previsione del prezzo finale;
- una ricostruzione del secondo prezzo;
- una garanzia di esito dell’asta.

Il range resta inoltre soggetto ai vincoli economici e competitivi già applicati dal motore.

---

# Control Panel: come leggere le metriche

## Crediti Spesi

È la somma della spesa reale della propria squadra, includendo i relativi Extra.

## Crediti Residui

È il budget ancora disponibile dopo aver sottratto la spesa registrata.

## Percentuale Budget Speso

Mostra quale parte del budget iniziale risulta già impegnata.

## Slot Totali / Occupati / Liberi

Riassume il livello di completamento della propria rosa.

## Stato Asta

Il tool distingue tra:

- **NON INIZIATA**, quando non risultano ancora acquisti o Extra che facciano partire il flusso dell’asta;
- **IN CORSO**, quando esiste già almeno un’operazione registrata.

Lo stato considera gli eventi di tutti i partecipanti, non soltanto quelli della propria squadra.

## Costo Atteso Futuro

È la stima della spesa necessaria per completare gli slot ancora aperti secondo il modello corrente.

## Margine vs Atteso

Confronta il budget residuo con il costo atteso necessario a completare la rosa.

È un indicatore di sostenibilità economica del percorso residuo, non una raccomandazione automatica su come spendere.

## Giocatori Comprati

Conta i giocatori assegnati alla propria squadra.

## Prezzo Medio Reale

È il costo medio degli acquisti registrati per la propria squadra.

## Media Spesa: Io vs Avversari

Confronta la spesa media propria con quella osservata per gli altri partecipanti.

Per gli avversari vengono utilizzati solo gli acquisti con costo noto, insieme agli Extra per i quali è stata registrata una spesa.

---

# Situazione Reparti

Per ogni ruolo il Control Panel mostra:

- slot totali;
- slot liberi;
- slot occupati;
- budget obiettivo del ruolo;
- spesa reale del ruolo;
- residuo del budget di ruolo;
- percentuale del budget di ruolo utilizzata;
- crediti medi per slot effettivamente occupato;
- stato di riempimento degli slot avversari;
- un segnale sintetico di attenzione.

Questa tabella è la vista più utile per capire rapidamente in quale reparto la situazione si sta discostando dai target impostati.

---

# Composizione residua per ruolo

Il Control Panel mostra anche la composizione dei giocatori ancora **Liberi** suddivisa per categoria.

Il grafico aiuta a capire come è distribuito il mercato residuo all’interno di ciascun ruolo.

La lettura è puramente descrittiva: mostra la composizione corrente dei giocatori ancora disponibili e non modifica da sola le formule del motore.

---

# Composizione della propria rosa

La tabella di composizione della rosa raggruppa i giocatori **Mio** per macro-categorie:

- area **Occ/Pun**;
- area **Tit**;
- area **Scm/Sca**.

Gli Extra, non avendo una categoria propria, vengono conteggiati nell’area residua prevista dal modello per mantenere coerente il conteggio degli slot della rosa.

---

# Filtri e ricerca

Nelle schede P/D/C/A è possibile filtrare i giocatori.

## Ricerca per nome

Il campo di ricerca permette di digitare il nome completo o una parte del nome.

La lista viene filtrata in tempo reale.

## Filtro per categoria

È possibile selezionare una o più categorie contemporaneamente.

I comandi rapidi permettono di selezionare tutte o nessuna delle categorie.

## Filtro per stato

È possibile filtrare separatamente:

- Liberi;
- Mio;
- Altri.

Anche qui sono disponibili i comandi rapidi per selezionare tutti o nessuno degli stati.

## Reset Filtri

Il pulsante **Reset Filtri** riporta ricerca, categorie, stati e ordinamento alla vista predefinita.

---

# Ordinamento delle tabelle

È possibile fare clic sulle intestazioni ordinabili.

Il tool supporta l’ordinamento per:

- nome;
- MAX;
- MAX_D;
- costo reale.

Un secondo clic sulla stessa intestazione inverte la direzione dell’ordinamento.

Le frecce visualizzate nell’intestazione indicano la direzione corrente.

---

# Preferiti

La stella nella prima colonna consente di contrassegnare un giocatore come **preferito**.

Il preferito è un’informazione personale di organizzazione e non interviene nei calcoli.

I giocatori preferiti vengono raccolti nella sotto-scheda **Salvati** della sezione Utente.

Per rimuovere un preferito è sufficiente fare nuovamente clic sulla stella.

---

# Note

Ogni giocatore dispone di una funzione **Note**.

L’icona con il blocco note apre un pannello in cui è possibile scrivere o modificare annotazioni libere.

Le note vengono salvate automaticamente nel browser.

Le note non modificano il motore MAX_D né le metriche dell’asta: servono come memoria personale dell’utente.

---

# Giocatore molto conteso

La casella **CONT.** consente di segnalare manualmente che un giocatore è considerato molto conteso.

Il flag non deriva automaticamente dai dati: è una scelta dell’utente.

Quando attivo, contribuisce a una correzione del MAX_D coerente con l’informazione qualitativa inserita manualmente.

È quindi una funzione da usare come integrazione ai dati osservati, non come sostituzione delle informazioni reali sull’asta.

---

# Extra della propria squadra

## Cosa sono

Gli Extra rappresentano eventi che consumano slot o crediti senza essere trattati come normali giocatori della lista principale.

La scheda contiene, per ogni ruolo:

- numero di slot Extra;
- crediti spesi;
- dettagli consultabili nella sezione Mia Squadra.

### Inserimento manuale

È possibile modificare gli Extra direttamente tramite i campi numerici oppure usare i pulsanti di incremento e decremento.

Il valore non può scendere al di sotto di zero.

Quando cambia il numero di slot Extra, il tool allinea automaticamente l’elenco dei dettagli mostrati in **Mia Squadra**.

---

# Extra degli avversari

Gli Extra degli avversari sono tracciati separatamente per partecipante e per ruolo.

Per ogni coppia **avversario + ruolo** vengono memorizzati:

- slot Extra;
- crediti spesi.

Questi dati contribuiscono alle statistiche del singolo avversario e al calcolo della pressione economica del mercato.

---

# Aggiunta rapida di un Extra

Nelle schede P/D/C/A è disponibile una barra di **Aggiunta rapida Extra**.

L’utente sceglie:

- a chi attribuire l’Extra, cioè alla propria squadra oppure a un avversario;
- i crediti associati.

Il ruolo è già determinato dalla scheda in cui si sta lavorando.

La procedura aggiorna automaticamente la struttura dati degli Extra e salva la modifica.

---

# Mia Squadra e gestione degli Extra

Nella vista **Mia Squadra**, gli Extra del ruolo vengono trasformati in righe di dettaglio in cui è possibile indicare:

- un nome descrittivo;
- il costo associato.

Il numero di righe segue automaticamente il numero di slot Extra configurati per quel ruolo.

---

# Dati avversari e capacità competitiva

Uno degli aspetti centrali del tool è la possibilità di distinguere i singoli avversari.

Per ciascuno il sistema ricostruisce:

- budget iniziale;
- budget residuo;
- spesa per giocatori;
- spesa per Extra;
- slot occupati;
- slot ancora disponibili per ruolo;
- capacità massima sostenibile di offerta per un ruolo.

La stima competitiva usa questi dati per individuare l’avversario economicamente più forte ancora in grado di partecipare a quel ruolo.

Questo è diverso dal trattare tutti gli avversari come se fossero un unico portafoglio comune.

---

# Dati mancanti e precisione delle stime

Il tool è progettato per funzionare anche quando l’utente non conosce tutto.

Tuttavia, la qualità di alcune correzioni dinamiche dipende direttamente dalla qualità dei dati inseriti.

In particolare, sono importanti:

- la registrazione dei costi reali degli acquisti degli altri;
- l’assegnazione corretta degli acquisti al singolo avversario;
- l’inserimento degli Extra osservati;
- la continuità nella registrazione delle transazioni.

Quando mancano dati sufficienti, alcune correzioni restano più vicine alla componente di base del modello.

Il tool mostra questa situazione attraverso l’indicatore di confidenza e, quando appropriato, attraverso l’avviso relativo al cap aggregato.

---

# Avviso “cap agg.”

Accanto al MAX_D può comparire l’avviso **cap agg.**.

Questo significa che, per il ruolo del giocatore in esame, esistono acquisti degli altri con costo registrato ma senza partecipante assegnato.

Finché questi acquisti non vengono attribuiti correttamente, il motore non può usare il tetto competitivo basato sul singolo rivale più forte e utilizza una stima aggregata.

L’avviso non significa necessariamente che il MAX_D sia inutilizzabile: indica che una parte della precisione competitiva è limitata da dati incompleti.

---

# Pacing e inflazione globale

Il motore confronta il budget residuo con il costo atteso per completare la rosa.

Questo rapporto genera un indicatore di andamento globale della spesa, utilizzato come componente della stima dinamica.

La riserva configurata per la categoria prevista non pesa nel pacing finché non viene effettivamente consumata. In questo modo una quota di budget pianificata in anticipo non viene interpretata come una spesa inattesa.

---

# Storico delle transazioni

Quando un giocatore viene registrato come Mio o Altri e ha un costo noto, il tool memorizza una transazione nello storico.

Lo storico conserva, tra le altre cose:

- ruolo;
- categoria;
- rapporto tra costo reale e valore di riferimento;
- stato della transazione;
- ordine cronologico di inserimento/modifica.

Lo storico viene usato dal motore per analizzare il comportamento recente del mercato.

Se un giocatore torna a essere Libero, la relativa transazione viene rimossa.

---

# Stato dell’asta e aggiornamento automatico

L’applicazione determina automaticamente se l’asta è ancora **Non iniziata** o se è **In corso**.

L’asta passa allo stato In Corso quando esiste una prima operazione rilevante registrata, anche se questa riguarda un altro partecipante o un Extra avversario.

Una volta iniziata, il motore può attivare le componenti dinamiche che dipendono dai dati effettivamente osservati.

---

# Dati sensibili: Show / Hide

Nel toolbar è presente il pulsante che alterna la visualizzazione dei dati sensibili.

Quando i dati sensibili sono nascosti, gli importi e gli indicatori economici pertinenti vengono sfocati a schermo senza modificare i valori realmente memorizzati o utilizzati dai calcoli.

La funzione è quindi pensata per evitare che informazioni economiche siano leggibili a colpo d’occhio, ad esempio quando lo schermo è visibile ad altre persone.

---

# Salvataggio dei dati

## Persistenza nel browser

Lo stato dell’applicazione viene salvato automaticamente nel **localStorage** del browser.

Il salvataggio comprende i principali dati operativi, tra cui:

- giocatori e relativi stati;
- costi reali;
- preferiti;
- note;
- configurazione della lega;
- Extra della propria squadra;
- Extra degli avversari;
- storico delle transazioni.

Quando la pagina viene ricaricata, l’app prova prima a recuperare i dati salvati nel browser.

---

# File dati iniziale

Se nel browser non esiste ancora un database locale dell’app, il tool prova a caricare il file **dati.json**.

Il file deve essere raggiungibile dalla stessa applicazione. Se il caricamento fallisce, l’applicazione mostra un messaggio che invita a verificare la presenza del file oppure a eseguire il processo di estrazione previsto dal progetto.

Il contenuto del file dati viene poi normalizzato e salvato nel browser per l’utilizzo successivo.

---

# Backup

## Esporta Backup

Il pulsante **Esporta Backup** crea un file JSON con lo stato corrente dell’applicazione.

Il backup include i dati necessari per ripristinare il lavoro, compresi:

- giocatori;
- Extra;
- Extra degli avversari;
- configurazione della lega;
- storico delle transazioni.

Il file viene scaricato con il nome previsto dall’applicazione.

### Buona pratica

È consigliabile creare backup durante le fasi importanti dell’asta, soprattutto prima di modifiche estese o prima di cambiare dispositivo/browser.

---

# Ripristino di un Backup

## Importa Backup

Il pulsante **Importa Backup** apre la selezione del file JSON da caricare.

Il tool controlla che il file contenga almeno i dati essenziali richiesti dall’applicazione.

Prima della sostituzione viene chiesta conferma, perché l’importazione sovrascrive lo stato attuale.

I backup precedenti all’introduzione di alcune funzioni possono comunque essere letti grazie alle procedure di normalizzazione compatibili con i formati più vecchi.

---

# Reset Totale

Il pulsante **Reset Totale** elimina il database locale dell’app e ricarica i dati iniziali.

L’operazione è distruttiva per lo stato corrente del browser: vengono persi costi, assegnazioni e modifiche non presenti in un backup esterno.

Prima dell’esecuzione viene mostrata una richiesta di conferma.

> **Procedura consigliata:** prima di un reset, esportare sempre un backup del lavoro corrente.

---

# Compatibilità con dati precedenti

Il tool contiene funzioni di normalizzazione per rendere utilizzabili anche dati più vecchi.

Questo riguarda, tra gli altri aspetti:

- vecchie strutture degli Extra;
- assenza del campo preferito;
- assenza del flag di giocatore molto conteso;
- assenza dell’assegnazione a un avversario;
- assenza dello storico transazioni;
- configurazioni prive della distribuzione del budget per ruolo.

Quando un dato manca, il tool ricostruisce una struttura compatibile con il formato corrente.

---

# Procedura operativa consigliata durante l’asta

Per usare il tool senza esperienza pregressa, è utile adottare una procedura sempre uguale.

## Prima dell’asta

Verificare:

- configurazione del budget;
- slot dei ruoli;
- distribuzione del budget;
- partecipanti avversari;
- nomi degli avversari;
- eventuale riserva configurata;
- disponibilità del file dati iniziale, se richiesto dall’ambiente di esecuzione.

## Durante ogni acquisto

Quando un giocatore viene assegnato:

1. individuarlo nella scheda del ruolo;
2. impostare **Mio** oppure assegnarlo a uno specifico **Avversario**;
3. inserire il costo reale appena disponibile;
4. verificare rapidamente che il dato sia finito nella squadra corretta;
5. proseguire con il successivo evento dell’asta.

## Quando si osserva un Extra

Registrare immediatamente:

- il destinatario;
- il ruolo interessato;
- gli slot consumati;
- la spesa, quando nota.

## Periodicamente

Controllare il **Control Panel** per individuare eventuali:

- residui incoerenti;
- slot mancanti o sovra-occupati;
- acquisti avversari non assegnati;
- avvisi sul cap aggregato;
- scostamenti importanti rispetto al piano iniziale.

## Prima di una chiusura o di un cambio dispositivo

Creare un **Backup**.

---

# Cosa aggiornare manualmente e cosa no

## L’utente deve aggiornare manualmente

- stato dei giocatori;
- assegnazione dell’avversario;
- costo reale;
- Extra;
- nomi degli avversari;
- configurazione della lega;
- preferiti;
- note;
- eventuale flag di giocatore molto conteso.

## Il tool calcola automaticamente

- budget residuo;
- spesa complessiva;
- spesa per ruolo;
- slot occupati e liberi;
- statistiche degli avversari;
- capacità economica dei singoli avversari;
- stato dell’asta;
- costo atteso residuo;
- margine rispetto all’atteso;
- composizione delle categorie;
- inflazione e pressione utilizzate dal motore;
- momentum del mercato;
- rank relativo nella categoria;
- indicatori di sazietà e riallocazione;
- MAX_D;
- confidenza del MAX_D;
- eventuale intervallo indicativo del MAX_D.

---

# Attenzione agli errori di inserimento

## Non lasciare acquisti avversari senza assegnazione

Quando possibile, associare ogni acquisto degli altri al partecipante corretto. I dati non assegnati riducono la precisione della componente competitiva per quel ruolo.

## Non inserire costi ipotetici come se fossero reali

Il campo Costo Reale deve rappresentare il prezzo effettivamente osservato, non una stima personale.

Le componenti dinamiche del motore dipendono proprio dalla distinzione tra dato osservato e supposizione.

## Non usare il flag “molto conteso” come stato automatico

Il flag è manuale e dovrebbe essere attivato solo quando l’utente dispone di un’informazione qualitativa che desidera comunicare al motore.

## Non confondere MAX con MAX_D

- **MAX** è il valore di riferimento di base associato al giocatore;
- **MAX_D** è il valore dinamico calcolato dal motore in funzione del contesto dell’asta.

## Non interpretare la confidenza come probabilità

Una confidenza alta significa che la componente dinamica è maggiormente sostenuta dai dati osservati. Non significa che la cifra sia garantita.

## Non usare il range come previsione esatta

Il range indicativo descrive l’incertezza derivante dalla dispersione dei prezzi osservati. Non è il prezzo finale previsto e non ricostruisce automaticamente il meccanismo di secondo prezzo.

---

# Limiti noti del modello

## Dati mancanti sugli avversari

Quando un acquisto degli altri ha costo noto ma non è associato a un partecipante, il tool non può ricostruire con certezza quale avversario disponga ancora della maggiore capacità economica.

Per questo utilizza una logica aggregata e visualizza un avviso.

## Dati economici facoltativi

La qualità di alcune correzioni dinamiche dipende dai costi reali che l’utente inserisce per gli acquisti degli altri. Se questi dati mancano, il motore dispone di meno evidenza osservata.

## Limite del confronto aggregato

Anche quando sono presenti dati su più avversari, alcune statistiche sono basate su informazioni aggregate. Un insieme di avversari con disponibilità economiche molto diverse può essere riassunto in modo più semplice rispetto alla situazione reale.

Il tool attenua questo problema usando il tracciamento per singolo partecipante dove possibile, ma non tutte le grandezze del motore sono costruite esclusivamente su dati individuali.

## MAX_D non è una garanzia

MAX_D è un indicatore operativo costruito con il modello e con i dati disponibili. Non garantisce il prezzo finale di un giocatore e non può conoscere informazioni che l’utente non ha registrato.

---

# Interpretazione corretta degli indicatori

Per utilizzare bene l’app è utile leggere i dati in questo modo:

- **MAX** = riferimento del giocatore;
- **MAX_D** = tetto dinamico aggiornato dal contesto;
- **Confidenza** = quantità/forza dell’evidenza osservata che alimenta le correzioni dinamiche;
- **Intervallo** = rappresentazione dell’incertezza dovuta alla dispersione osservata;
- **Margine vs Atteso** = distanza tra risorse residue e costo atteso del completamento;
- **Pressione avversari** = quanto spazio resta agli altri nel ruolo, combinato con la loro capacità economica osservata;
- **Sazietà** = riduzione della priorità quando parte della composizione desiderata è già stata coperta;
- **Riallocazione** = riduzione della spesa suggerita quando un’alternativa dello stesso ruolo appare relativamente più conveniente.

Questi indicatori vanno letti insieme e nel contesto dell’asta, non isolatamente.

---

# Domande frequenti

## Il tool salva automaticamente?

Sì. Le modifiche operative vengono salvate nel browser tramite localStorage.

## Posso chiudere e riaprire la pagina?

Sì, purché si utilizzi lo stesso ambiente del browser e i dati locali non vengano cancellati. È comunque buona pratica conservare un backup esterno.

## Posso cambiare il budget iniziale dopo aver iniziato?

La configurazione è modificabile dall’interfaccia. Tuttavia, poiché il budget fa parte della base di calcolo del motore, cambiarlo durante un’asta già avviata modifica anche gli indicatori derivati. È quindi opportuno mantenere la configurazione coerente con la lega reale.

## Posso aggiungere o rimuovere avversari?

Sì, dalla sezione Impostazioni Lega. Quando il numero cambia, l’app aggiorna l’elenco degli avversari e riallinea gli Extra associati. Gli acquisti assegnati a partecipanti che non esistono più vengono privati dell’assegnazione.

## Cosa succede se tolgo un avversario a cui avevo assegnato degli acquisti?

Se l’avversario non è più presente nella configurazione, le assegnazioni non più valide vengono rimosse e gli acquisti restano senza avversario associato.

## Gli Extra contano nei calcoli?

Sì. Gli Extra della propria squadra concorrono al consumo di slot e alla spesa. Gli Extra avversari partecipano alle statistiche e ai calcoli previsti per il lato avversari.

## Le note modificano MAX_D?

No. Le note sono informative e non intervengono nei calcoli.

## I preferiti modificano MAX_D?

No. I preferiti servono solo per organizzare la lista personale.

## Il flag “molto conteso” modifica MAX_D?

Sì. È un’informazione manuale che viene usata dal motore come segnale aggiuntivo di domanda.

## Cosa significa “cap agg.”?

Significa che il motore non può applicare il tetto competitivo basato sul singolo avversario più forte per quel ruolo, perché esiste almeno un acquisto avversario con costo registrato ma non assegnato a un partecipante.

## Perché il MAX_D può cambiare anche quando non modifico il giocatore?

Perché MAX_D dipende dal contesto dell’intera asta. Nuovi acquisti, nuovi costi, nuove assegnazioni agli avversari, cambiamenti nella composizione dei ruoli e altre informazioni osservate possono modificare il valore dinamico di un giocatore ancora libero.

## Perché il MAX_D resta vicino al valore base?

Può accadere quando l’asta è ancora poco osservata oppure quando non ci sono abbastanza dati utili per sostenere le correzioni dinamiche. In quel caso il motore mantiene un comportamento più vicino alla componente strutturale di base.

## Il range accanto a MAX_D è un prezzo previsto?

No. È un intervallo indicativo ottenuto dalla dispersione dei rapporti di spesa osservati.

---

# Checklist rapida per un utente alle prime armi

## Prima di iniziare

- [ ] Accedere all’applicazione.
- [ ] Verificare le Impostazioni Lega.
- [ ] Controllare budget e distribuzione per ruolo.
- [ ] Controllare gli slot dei ruoli.
- [ ] Controllare il numero e i nomi degli avversari.
- [ ] Verificare che il dataset iniziale sia corretto.

## Per ogni acquisto

- [ ] Cercare il giocatore.
- [ ] Impostare Mio oppure assegnare l’avversario.
- [ ] Inserire il costo reale.
- [ ] Verificare il risultato nel Control Panel.

## Se è presente un Extra

- [ ] Scegliere il destinatario.
- [ ] Selezionare il ruolo corretto.
- [ ] Registrare slot e spesa.
- [ ] Verificare le metriche aggiornate.

## Durante l’asta

- [ ] Controllare periodicamente gli acquisti non assegnati.
- [ ] Aggiornare i costi reali appena disponibili.
- [ ] Usare preferiti e note per i giocatori importanti.
- [ ] Consultare MAX_D insieme a confidenza e contesto del ruolo.
- [ ] Creare backup periodici.

## Prima di chiudere il lavoro

- [ ] Esportare un backup.
- [ ] Verificare che il file JSON sia stato effettivamente scaricato.

---

# Riepilogo finale

Asta Live funziona come un **registro operativo dell’asta con motore di calcolo dinamico**.

Il principio fondamentale è semplice:

> **più i dati inseriti riflettono fedelmente ciò che sta accadendo nell’asta, più le componenti dinamiche possono adeguarsi al contesto osservato.**

Il lavoro dell’utente consiste soprattutto nel mantenere aggiornati gli eventi reali. Il tool si occupa poi di aggiornare automaticamente budget, slot, statistiche, dati degli avversari e indicatori di supporto alle decisioni.

Per un utilizzo corretto è essenziale distinguere sempre tra:

- dati realmente osservati;
- informazioni manuali aggiunte dall’utente;
- valori calcolati automaticamente;
- stime dinamiche che riflettono il contesto del momento.

Quando il dato non è noto, è preferibile lasciarlo come non disponibile piuttosto che inventarlo: il motore è progettato per esplicitare l’incertezza quando le informazioni osservate non sono sufficienti.

---

## Fonte della guida

Questa guida è stata redatta a partire dal comportamento effettivamente implementato nel file HTML dell’applicazione fornito, inclusi interfaccia, gestione dei dati, calcoli, backup/ripristino, sicurezza a schermo e logiche del motore MAX_D.
