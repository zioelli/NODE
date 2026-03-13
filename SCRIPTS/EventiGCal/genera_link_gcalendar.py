from urllib.parse import quote
from datetime import datetime

#Fuso orario e formato data usati in tutto il programma
FORMATO_DATA = "%d/%m/%Y"
TIMEZONE = "Europe/Rome"

def valida_data(messaggio):
    #Chiede una data all'utente e la ripete finché il formato è corretto
    while True:
        valore = input(messaggio)
        try:
            #strptime verifica che la data esista davvero (es. 31/02 viene rifiutato)
            return datetime.strptime(valore, FORMATO_DATA).date()
        except ValueError:
            print("Formato non valido. Riprova (es: 15/05/2024).")

def valida_ora(messaggio):
    #Chiede un orario all'utente e lo ripete finché il formato è corretto
    while True:
        valore = input(messaggio)
        try:
            h, m = map(int, valore.split(':'))
            #Controlla che ore e minuti siano in un intervallo sensato
            if 0 <= h <= 23 and 0 <= m <= 59:
                return valore.strip()
            raise ValueError
        except ValueError:
            print("Formato non valido. Riprova (es: 09:30).")

def combina_datetime(data, ora):
    #Unisce data e ora in una stringa nel formato richiesto da Google Calendar (YYYYMMDDTHHmmSS)
    dt = datetime.strptime(f"{data} {ora}", "%Y-%m-%d %H:%M")
    return dt.strftime("%Y%m%dT%H%M%S")

def valida_fine_evento(inizio):
    #Chiede data e ora di fine evento, ripetendo finché sono successive all'inizio
    while True:
        data_f = valida_data("Data fine (gg/mm/aaaa): ")
        ora_f  = valida_ora("Ora fine (hh:mm): ")
        fine   = combina_datetime(data_f, ora_f)

        #Confronta fine con inizio e segnala l'errore senza uscire dal programma
        if fine > inizio:
            return fine
        print("La data/ora di fine deve essere successiva a quella di inizio. Reimmetti la data di fine.")

def genera_link_gcalendar():
    print("--- Generatore Link Google Calendar ---")

    #Acquisizione e validazione delle date e degli orari di inizio evento
    data_i = valida_data("Data inizio (gg/mm/aaaa): ")
    ora_i  = valida_ora("Ora inizio (hh:mm): ")
    inizio = combina_datetime(data_i, ora_i)

    #Acquisizione fine evento: si ripete finché la fine è successiva all'inizio
    fine = valida_fine_evento(inizio)
    
    #Acquisizione testo libero: quote() codifica i caratteri speciali per l'URL
    #(es. spazi convertito in %20, & convertita in %26) così il link rimane valido qualunque cosa scriva l'utente
    titolo   = input("Titolo dell'evento: ")
    location = input("Location dell'evento: ")
    note     = input("Note/dettagli dell'evento: ")

    #Costruzione dell'URL secondo le specifiche di Google Calendar
    #ctz imposta il fuso orario così l'ora viene interpretata correttamente
    link = (
        f"https://www.google.com/calendar/event?action=TEMPLATE"
        f"&dates={inizio}%2F{fine}"   #%2F è la codifica URL di /
        f"&text={quote(titolo)}"
        f"&location={quote(location)}"
        f"&details={quote(note)}"
        f"&ctz={TIMEZONE}"
    )

    print("\nLink generato con successo:")
    print("-" * 30)
    print(link)
    print("-" * 30)

if __name__ == "__main__":
    genera_link_gcalendar()
    #Mantiene la finestra aperta dopo la generazione, utile se lanciato con doppio clic
    input("\nPremi Invio per uscire...")
