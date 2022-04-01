# HeroTimer

Tool zum errechnen der Gesamtzeit von Stunden in Hero-Excel Dateien
## Hero Excel Download

1. Auf "Mitarbeiterverwaltung" gehen
2. Dann auf "Zeiterfassung"
3. Nach gewünschen Einstellungen filtern
4. Button "Export" drücken und "Excel" auswählen 

## Installation

1. Downlaod Zip via http://midenos.de/Hero.zip
2. Dateien entpacken 
3. "config.txt" Datei anpassen pro Zeile
    Ihre Firma
    Ihre Straße
    Ihre PLZ
4. Eigenes Logo verwenden, Dateiname und Dateityp muss erhalten eingehalten werden "logo.png"
5. Hero.exe ausführen
6. Bei Windows Sicherheitsmeldungen trotzdem zulassen (Einmalig, weitere Infos in FAQ)
7. Auf "Weitere Informationen" klicken
8. Dann auf "Trotzdem Ausführen"
9. Software startet

## Anleitung

1. "Open File" auswählen
2. Excel Datei von Hero suchen
3. Excel Datei öffen
4. Arbeitszeit nach ausgewählten Filtern errechnet und unten angezeigt 
5. PDF erstellen durch "PDF erstellen" Button 
6. Erstellte PDF befindet sich im Ordner der Hero.exe

![FAQ Pic 1](/ReadmePictures/tool_1.JPG)
![FAQ Pic 2](/ReadmePictures/tool_2.JPG)
![FAQ Pic 3](/ReadmePictures/tool_3.JPG)

## FAQ

- Windows Defender erkennt einen Trojaner

Leider erkennt der Windows Defender fehlerhaft die mit PyInstaller erstellte Dateien, dies liegt an der Decodierung und hier müsste eine base64 oder grundsätzlich die Umwandlung von Text in binäre Kodierung durchgeführt werden. Durch die Verwendung von UTF-8 die für das Tool notwendig ist, arbeite ich noch an der Umsetzung.
Das Programm enthält keine Schadsoftware! Gern selbst einmal über Virus Total laufen lassen.

![Virus Total](/ReadmePictures/VirusTotal.JPG)

- Fehler bei Starten (bitmap "data/hero.ico" not defined)

Achten Sie darauf, dass der "data" Ordner dort liegt wo die Hero.exe ausgeführt wird und die .ico Datei enthält

- Beim klicken auf "PDF erstellen" passiert nichts und ich erhalte keine Meldung

Achten Sie darauf, dass die "logo.png" vorhanden ist, ohne diese wird aktuell keine PDF erstellt(Wird noch überarbeitet)
