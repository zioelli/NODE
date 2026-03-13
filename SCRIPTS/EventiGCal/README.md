# Generatore di Link per Google Calendar
![Made by DigitalPro](https://img.shields.io/badge/Autore-Prof.%20G.Mirante-blue)
![Versione](https://img.shields.io/badge/Version-1.1.1-blue)

# Generatore di Link per Google Calendar

📅 **Automatizza la creazione di eventi su Google Calendar con un solo click!**

Questo script Python permette di generare un link personalizzato per aggiungere eventi a Google Calendar in modo rapido e senza errori. Ideale per insegnanti, studenti e famiglie che vogliono sincronizzare appuntamenti, riunioni o eventi scolastici direttamente dal sito della scuola.

---

## 🔧 **Come funziona?**
Lo script chiede all'utente di inserire:
- Data e ora di inizio/fine dell'evento
- Titolo, location e note/dettagli
- Genera un link che, una volta cliccato, apre Google Calendar con i dati precompilati.

---

## 🚀 **Istruzioni per l'uso**

### 1. **Prerequisiti**
- Python 3.x installato
- Nessuna libreria esterna richiesta (usa solo `urllib.parse`)

### 2. **Esecuzione**
1. Scarica lo script `genera_link_gcalendar.py`.
2. Esegui lo script con Python:
   ```bash
   python genera_link_gcalendar.py
   ```
3. Inserisci i dati richiesti (data, ora, titolo, location, note).
4. Copia il link generato e incollalo nella circolare o sul sito della scuola.
### 3. **Esempio di output**
Link generato:
``` bash
https://www.google.com/calendar/event?action=TEMPLATE&dates=20260315T090000%2F20260315T110000&text=Riunione%20Genitori&location=Aula%20Magna&details=Incontro%20con%20i%20docenti%20per%20il%20progetto%20scolastico
```
##

### 💡**Casi d'uso**

*Scuole*: Inserire eventi come riunioni, esami, o attività extracurriculari.
Famiglie: Sincronizzare appuntamenti scolastici con i propri calendari.
Lavoro: Pianificare riunioni o scadenze con colleghi.

### 📌 **Note**
Il link generato è compatibile con Google Calendar (web e app mobile).
Assicurati che i dati inseriti siano corretti (formato data/ora: gg/mm/aaaa e hh:mm).

### 🤝 Contributi
Se vuoi contribuire al progetto, apri una Pull Request o segnalaci un bug!