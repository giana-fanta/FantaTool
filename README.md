# Asta Fanta 26/27

App web personale che sostituisce `Fanta_2627.xlsx`: stessi dati (fogli P,
D, C, A), stesse formule di MAX_D e Dashboard, ma niente Excel/OneDrive di
mezzo. Vedi `docs/formule.md` per il dettaglio di ogni formula tradotta.

## 1. Installazione (una tantum)

Serve [Node.js](https://nodejs.org) installato sul computer (versione 18 o
successiva). Poi, da questa cartella:

```bash
npm install
npm run seed    # popola il database con i dati estratti dal tuo Excel
```

Il comando `seed` legge `data/seed.json` (già generato dal tuo file
originale) e crea `data/app.db`, il database SQLite che d'ora in poi è la
fonte dei dati — **non serve più aprire Excel**.

## 2. Avvio in locale

```bash
npm start
```

Apri il browser su **http://localhost:3000**. Da lì puoi vedere e
modificare i giocatori: ogni modifica ricalcola subito MAX_D e Dashboard.

## 3. Verificare che i calcoli siano corretti

```bash
npm test
```

Confronta i valori calcolati dall'app con quelli che Excel calcolava nel
file originale (due scenari salvati in `data/fixtures/`). Deve sempre dire
`OK: tutti i valori coincidono con Excel`. Se in futuro tocchi
`server/services/calculations.js`, rilancia questo comando prima di
fidarti del risultato.

## Struttura del progetto

```
data/
  schema.sql          ← struttura del database
  seed.json           ← dati iniziali (estratti dal tuo Excel)
  fixtures/           ← scenari di test per validate.js
docs/
  formule.md          ← ogni formula Excel spiegata e mappata al codice
server/
  index.js            ← avvio del server
  db.js                ← accesso al database
  seed.js              ← popola il database la prima volta
  services/
    calculations.js    ← IL CUORE: le formule tradotte in JS
    validate.js         ← verifica che i calcoli coincidano con Excel
  routes/
    giocatori.js         ← API per leggere/modificare i giocatori
    dashboard.js          ← API per la dashboard e le impostazioni
client/
  index.html, app.js, style.css  ← l'interfaccia che usi nel browser
```

## Prossimo passo: usarla anche da telefono, non solo da PC

Finché la usi solo su questo computer, va già bene così. Per usarla anche
da mobile fuori casa serve pubblicarla online — a quel punto **il database
SQLite di questo progetto non basta più** (i piani gratuiti di hosting
resettano i file locali ad ogni riavvio), va spostato su un database
gratuito ospitato (es. Supabase o Neon, entrambi hanno un piano gratuito
persistente). È un cambio piccolo (poche righe in `db.js`), da fare quando
sei pronto — dimmelo e ti guido passo passo anche per quello.

## Note sui dati

- I fogli **Tutti** e **Utils** del file originale non sono stati
  migrati, su richiesta esplicita: non contribuiscono a nessuna delle
  formule di MAX_D o Dashboard.
- Tutti i 301 giocatori (20 P + 108 D + 113 C + 60 A) sono stati
  verificati uno per uno contro i valori calcolati da Excel — vedi
  `npm test`.
