import serial
import time
from datetime import datetime
import csv
import os
import sys

# Port-Konfiguration
PORT = "COM3"
BAUD = 9600

ser= None
object_timestamp = []

#Funktion zum speichern als csv:
def csv_export():

        if object_timestamp:
                # Wenn das Programm als EXE läuft:
                if getattr(sys, 'frozen', False):
                    script_dir = os.path.dirname(sys.executable)
                #Wenn das Programm als .py läuft:
                else:
                    try:
                         script_dir = os.path.dirname(os.path.abspath(__file__))
                    except NameError:
                         # Fallback, falls __file__ nicht definiert ist
                         script_dir = os.getcwd()
                    
                filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
                full_path = os.path.join(script_dir, filename)
                    
                try:
                        with open(full_path, mode='w', newline='') as file:
                            writer = csv.writer(file, delimiter=';') 
                            
                            writer.writerow(["Datum Beginn", "Uhrzeit Beginn", "Datum Ende", "Uhrzeit Ende", "Dauer (Sekunden)"])
                                    
                            for interval in object_timestamp:
                                start = interval[0]
                                end = interval[1]
                                #Für Excel angemessenes Format (ohne Millisekunden):
                                start_date_excel = start.strftime('%d.%m.%Y')
                                start_time_excel = start.strftime('%H:%M:%S')
                                end_date_excel = end.strftime('%d.%m.%Y')
                                end_time_excel = end.strftime('%H:%M:%S')
                                duration = (end - start).total_seconds() # Berechnen der Signaldauer in s; als
                                formatted_duration = f"{duration:.2f}".replace('.', ',')
                                writer.writerow([start_date_excel, start_time_excel, end_date_excel, end_time_excel,formatted_duration])
                                
                        
                        print(f"Daten erfolgreich gespeichert unter: {full_path}")
                except Exception as e:
                        print(f"Fehler beim CSV-Export: {e}")
        else:
                print("Keine neuen Daten für Auto-Save.")

try:
    # Verbindung öffnen
    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2)
    print(f"Verbunden mit {PORT}...")
    count = 0
    save = False
    tolerance = 10
    tolerance_counter = 0
    last_export = datetime.now()
    saving_period_in_s = 10

    # Hilfsvariable für den aktuellen Startzeitpunkt
    current_start = None

    while True:
        #Speichern nach Ablauf des Speicherintervalls
        if (datetime.now() - last_export).total_seconds() > saving_period_in_s:
             if csv_export():
                object_timestamp = []
             last_export = datetime.now()
        if ser.in_waiting > 0:  # Prüfen, ob Daten im Puffer sind, Zeile lesen
            state = ser.readline().decode('utf-8', errors='ignore').strip()
            
            # if state:
            #     print(state)

            if state=="OBJECT DETECTED!":  
                count+=1
                if save == True:
                    tolerance_counter = tolerance

                # Start Signal-Aufzeichnung
                if count == 1:
                    current_start = datetime.now()
            else:
                if save == True and current_start is not None:
                    # Ende erfassen, Aufzeichnung Liste hinzufügen
                    if tolerance_counter > 0:
                        tolerance_counter -= 1
                        continue
                    else:
                        current_end = datetime.now()
                        object_timestamp.append([current_start, current_end])
                        print(f"Aufzeichnung abgeschlossen: {current_start.strftime('%H:%M:%S')} bis {current_end.strftime('%H:%M:%S')}")
                     
                
                count = 0
                save = False
                current_start = None
                tolerance_counter = 0

            if count > 5 and save==False:
                save = True
                tolerance_counter = tolerance

except serial.SerialException as e:
    print(f"Fehler beim Öffnen des Ports: {e}")
except KeyboardInterrupt:
    print("\nProgramm beendet.")

# Bei Verbindungsabbruch: Speichern der Daten im Verzeichnis der Quelldatei
finally:

    if ser is not None and ser.is_open:
        ser.close()
        print("Serielle Verbindung geschlossen.")

    csv_export()

    # print(object_timestamp)

    input("\nProgramm beendet. Enter druecken zum Schließen...")