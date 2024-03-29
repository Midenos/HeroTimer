# HeroTimer

Tool zum errechnen der Gesamtzeit von Stunden in Hero-Excel Dateien
## Hero Excel Download

1. Auf "Mitarbeiterverwaltung" gehen
2. Dann auf "Zeiterfassung"
3. Nach gewünschen Einstellungen filtern
4. Button "Export" drücken und "Excel" auswählen 

## Installation

1. Downlaod Zip via http://midenos.de/Hero.zip / Oder aus dem Git "Install Zip" Ordner laden
2. Dateien entpacken 
3. Logo bei bedarf durch eigenes erstzen, Dateiname und Dateityp muss eingehalten werden "logo.png"
4. Hero.exe ausführen
5. Bei Windows Sicherheitsmeldungen trotzdem zulassen (Einmalig, weitere Infos in FAQ)
6. Auf "Weitere Informationen" klicken
7. Dann auf "Trotzdem Ausführen"
8. Software startet

## Anleitung

1. "Open File" auswählen
2. Excel Datei von Hero suchen und auswählen/öffnen
3. Arbeitszeit wird je nach ausgewählten Filtern errechnet und unten angezeigt 
4. "Optionen" Button zum einstellen der Firmenanschrift und des Logos wählen  
5. Projekt und Dateiname zum erstellen der PDF eintragen
6. PDF erstellen durch "PDF erstellen" Button 
7. Erstellte PDF befindet sich im Ordner der Hero.exe

![FAQ Pic 1](/ReadmePictures/tool_1.JPG)
![FAQ Pic 2](/ReadmePictures/tool_2.JPG)
![FAQ Pic 3](/ReadmePictures/tool_3.JPG)

## FAQ

- Windows Defender erkennt einen Trojaner

Leider erkennt der Windows Defender in Ausnahmefällen fehlerhaft die mit PyInstaller erstellte Dateien, dies liegt an der Decodierung und hier müsste eine base64 oder grundsätzlich die Umwandlung von Text in binäre Kodierung durchgeführt werden. Durch die Verwendung von UTF-8 die für das Tool notwendig ist, arbeite ich noch an der Umsetzung.

Das Programm enthält keine Schadsoftware! Gern selbst einmal über Virus Total laufen lassen.

![Virus Total](/ReadmePictures/VirusTotal.JPG)

- Fehler bei Starten (bitmap "data/hero.ico" not defined)

Achten Sie darauf, dass der "data" Ordner dort liegt wo die Hero.exe ausgeführt wird und die .ico Datei enthält

- Beim klicken auf "PDF erstellen" passiert nichts und ich erhalte keine Meldung

Bei Verwendung vom "" im Projekt/Dateiname wird keine PDF erstellt.
Bitte verwenden Sie anstelle von "" einfach '', aktuell können doppel "" nicht als Projekt oder Dateiname verwendet werden.

- Meine Logo sitzt nicht richtig

Sie können in der Software die Optionen für das Logo ändern, X-Position scheibt das Logo horizontal Y-Position vertikal.
Die Größe stellen Sie entsprechend Ihrer Wünsche ein, probieren Sie verschiedene Werte, größere Zahl bedeutet größeres Logo.
