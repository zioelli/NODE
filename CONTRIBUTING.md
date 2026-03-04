# 🛠️ Come contribuire a NODE

Benvenuto in NODE!
Qui trovi tutto ciò che ti serve per iniziare a contribuire: script, tutorial hardware e progetti open source per la scuola.

---

## 🔧 Prerequisiti

* Un account GitHub
* Git installato sul tuo computer
* Un editor di testo (es. VS Code)

---

## 🍴 Fork e Clone della Repository

### Forka la repo

1. Vai su **NODE** e clicca su **"Fork"** (in alto a destra).
2. Ora hai una copia personale della repo sotto il tuo account.

### Clona la tua copia locale

```bash
git clone https://github.com/tuo-username/node
cd NODE
```

---

## 🌿 Creare un Branch

Prima di modificare qualsiasi file, crea un branch dedicato:

```bash
git checkout -b nome-del-tuo-branch
```

Esempio:

```bash
git checkout -b aggiungi-script-orari
```

---

## ✏️ Modificare i File

Aggiungi o modifica i file nella cartella appropriata (es. `/scripts`, `/hardware`).

**Importante:** aggiungi un commento iniziale in ogni file con:

```python
# Nome del file: script_orari.py
# Autore: Tuo Nome (Istituto)
# Data: GG/MM/AAAA
# Descrizione: Breve descrizione dello script/progetto
```

---

## 💾 Commit e Push

Aggiungi i file modificati:

```bash
git add .
```

Fai il commit con un messaggio chiaro:

```bash
git commit -m "Aggiunto script per conversione orari da PDF a JSON"
```

Push sul tuo branch:

```bash
git push origin nome-del-tuo-branch
```

---

## 🔄 Aprire una Pull Request (PR)

1. Vai sulla tua repo su GitHub e seleziona il branch appena creato.
2. Clicca su **"Pull Request" → "New Pull Request"**.
3. Aggiungi una descrizione chiara delle modifiche.
4. Clicca su **"Create Pull Request"**.

Un maintainer revisionerà la PR e la unirà alla repo principale.

---

## 🐛 Segnalare Bug o Proporre Idee

Usa le **Issue** per:

* Segnalare bug
* Proporre nuovi script o progetti
* Chiedere aiuto

### Esempio di titolo per una Issue

❌ "Non funziona lo script"

✅ `[BUG] Script orari: errore in conversione PDF con file > 10MB`

---

## 🎯 Regole di Base

* **Nomi dei file:** usa nomi chiari e in minuscolo (es. `script_orari.py`, `guida_raspberry.md`).
* **Documentazione:** ogni script o progetto deve avere un file `README.md` nella sua cartella.
* **Rispetta la licenza:** tutto il materiale è sotto licenza GPLv3.

---

## 🤝 Codice di Condotta

* Sii rispettoso e costruttivo nei commenti.
* Dai credito agli autori originali.
* Divertiti e condividi la conoscenza!

---

## 📚 Risorse Utili

* Guida GitHub per principianti:
  [https://guides.github.com/activities/hello-world/](https://guides.github.com/activities/hello-world/)
