# HeroTimer

Tool zum errechnen der Gesamtzeit von Stunden in Hero-Excel Dateien
## Hero Excel Download

1. Auf "Mitarbeiterverwaltung" gehen
2. Dann auf "Zeiterfassung"
3. Nach gewünschen Einstellungen filtern
4. Button "Export" drücken und "Excel" auswählen 

## Installation

1. Downlaod Zip via http://midenos.de/Hero.zip
2. Dateien entpacken und Hero.exe ausführen
3. Bei Windows Sicherheitsmeldungen trotzdem zulassen einmalig zulassen (Infos weiter unten in FAQ)
4. Auf "Weitere Informationen" klicken
5. Dann auf "Trotzdem Ausführen"
6. Software startet

## Anleitung

1. "Open File" auswählen
2. Excel Datei von Hero suchen
3. Excel Datei öffen
4. Arbeitszeit wird errechnet und unten angezeigt 

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
