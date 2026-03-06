from urllib.parse import quote

def genera_link_gcalendar():
    print("Inserisci i dettagli dell'evento:")

    # IT: Qui viene richiesto di inserire i dati di inizio evento
    data_inizio = input("Data inizio (formato: gg/mm/aaaa): ")
    ora_inizio = input("Ora inizio (formato: hh:mm): ")
    giorno, mese, anno = data_inizio.split('/')
    hh, mm = ora_inizio.split(':')
    inizio = f"{anno}{mese.zfill(2)}{giorno.zfill(2)}T{hh.zfill(2)}{mm.zfill(2)}00" # IT: zfill serve ad aggiungere zeri nel caso l'utente non rispetti il format data
    
    # IT: Qui viene richiesto di inserire i dati di fine evento
    data_fine = input("Data fine (formato: gg/mm/aaaa): ")
    ora_fine = input("Ora fine (formato: hh:mm): ")
    giorno, mese, anno = data_fine.split('/')
    hh, mm = ora_fine.split(':')
    fine = f"{anno}{mese.zfill(2)}{giorno.zfill(2)}T{hh.zfill(2)}{mm.zfill(2)}00"

    # IT: Inserimento di titolo, location, note
    titolo = input("Titolo dell'evento: ")
    location = input("Location dell'evento: ")
    note = input("Note/dettagli dell'evento: ")

    # IT: URL encode: serve ad adattare il testo al formato url (Esempio: elimina gli spazi)
    titolo_encoded = quote(titolo)
    location_encoded = quote(location)
    note_encoded = quote(note)

    # IT: Generazione link
    link = f"https://www.google.com/calendar/event?action=TEMPLATE&dates={inizio}%2F{fine}&text={titolo_encoded}&location={location_encoded}&details={note_encoded}"

    print("\nLink generato:")
    print(link)

if __name__ == "__main__":
    genera_link_gcalendar()
input("\nPremi un tasto per chiudere la finestra...")  # IT: Questa riga tiene aperta la finestra