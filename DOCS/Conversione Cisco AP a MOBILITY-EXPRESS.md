# Conversione Firmware AP Cisco AIR-AP1832I-F-K9  
## Da CAPWAP Mode a Mobility Express

Basato su:  
https://www.youtube.com/watch?v=VZpn9s8ipC4

In caso di aggiornamento della rete Wi-Fi della scuola con sostituzione degli Access Point, gli AP dismessi possono essere riconvertiti per l’utilizzo **senza controller**, operando in modalità **autonoma (Mobility Express)**. Gli AP convertiti possono essere utilizzati per estendere la copertura o replicare SSID in **aree con segnale debole o non coperte.**

---

# Procedura

## 1. Connessione console

Connettere l'AP al cavo console tramite **porta COM** ed utilizzare un terminale tipo **Putty**.

---

## 2. Reset dell'Access Point

Avviare l'AP tenendo premuto il **tasto reset** fino al **countdown di 25 secondi** visibile nella console.

---

## 3. Download firmware

Procurarsi il file firmware **Mobility Express** per il proprio modello.

Esempio (**AP1832I**):

```
AIR-AP1830-K9-8-10-162-0.tar
```

---

## 4. Credenziali di default

Dopo il reset dell'AP:

```
Username: Cisco
Password: Cisco
Enable: Cisco
```

---

## 5. Accesso alla modalità enable

In console eseguire:

```bash
enable
Password: Cisco
#
```

---

## 6. Disabilitare il logging

```bash
logging console disable
```

---

## 7. Verificare l'indirizzo IP

```bash
show ip interface brief
```

---

## 8. Verifica DHCP

Se l'AP è acceso con **power injector** e collegato alla **rete aziendale**, con il comando precedente potrete vedere l'IP assegnato dal **DHCP** all'interfaccia **BVI1**.

---

## 9. Impostare IP manuale (se necessario)

Se non viene assegnato un IP, impostarne uno manualmente nella subnet locale.

Formato comando:

```bash
capwap ap ip <IP> <SUBNET_MASK> <GATEWAY>
```

Esempio:

```bash
capwap ap ip 10.10.10.100 255.255.255.0 10.10.10.2
```

---

## 10. Avviare il server TFTP sul PC Windows

Scaricare ed eseguire **Tftpd64**:

https://pjo2.github.io/tftpd64/

Impostare:

- cartella contenente il firmware
- indirizzo IP compatibile con la subnet

Esempio:

```
C:\Users\User\Download
10.10.10.2
```

---

# 11. Upload e Upgrade Firmware

Eseguire il comando (puntare l'IP del server TFTP) ed attendere il completamento della procedura di upload:

```bash
ap-type mobility-express tftp://10.10.10.2/AIR-AP1830-K9-8-10-162-0.tar
```

---

# 12. Riavvio dell'Access Point

Al termine dell'installazione se non già eseguito in automatico, riavviare con il comando:

```bash
reload
```

---

# Prima configurazione

Una volta riavviato, seguire i passi indicati dall'AP in console.

---

## 1. Connessione alla rete di provisioning

Apparirà un hotspot chiamato:

```
CiscoAirProvision
```

Password:

```
password
```

---

## 2. Apertura pagina di configurazione

Una volta connessi, si aprirà automaticamente la **pagina di configurazione dell'AP**.

⚠️ Attenzione:

Se il PC Windows da cui eseguite la configurazione è **in dominio**, l'apertura automatica potrebbe **non funzionare**.

Per la prima configurazione è consigliato utilizzare **un PC non in dominio**.

---

## 3. Se il SSID non appare

Molto probabilmente al primo riavvio **non apparirà il SSID `CiscoAirProvision`**.

Procedere così:

1. scollegare la **rete aziendale**
2. riavviare l'AP
3. eseguire nuovamente il **reset da 25 secondi**

Dopo alcuni tentativi il SSID dovrebbe apparire nell'elenco delle reti disponibili.

---

## 4. Configurazione iniziale

La prima pagina permetterà di configurare:

- Username amministratore
- Password amministratore
- Parametri base del controller

---

# Riferimento video

Per la configurazione completa è consigliato seguire il video:

https://www.youtube.com/watch?v=VZpn9s8ipC4
