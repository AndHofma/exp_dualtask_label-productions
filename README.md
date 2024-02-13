# Labeling-Aufgabe
Dieses Projektverzeichnis enthält das Setup für die Labeling-Aufgabe. Bitte lese dir in Ruhe alle Abschnitte durch und führe alle Schritte durch, die notwendig sind:

## Voraussetzungen
- Bitte stelle sicher, dass Python in der Version 3.10 auf deinem Rechner installiert ist
- Stelle sicher, dass auf deiner Festplatte 3.5 GB freier Speicherplatz für die Aufgabe zur Verfügung steht
- Bitte schreibe mir ein E-Mail mit deinem Namen und deiner Uni-Mailadresse, damit ich auf BoxUP die Ordner mit den Aufnahmen für dich freischalten kann
- Erstelle dir deine `labeler_ID` wie nachfolgend beschrieben, und notiere sie dir, damit du sie wiederverwenden kannst 
  - die ersten zwei Buchstaben deines Geburtsnamens
  - dein Geburtstag (der Tag zweistellig)
  - die zwei letzten Buchstaben deines Geburtsortes
  - die ersten zwei Buchstaben des Vornamens deiner Mutter
  - Trage die ID dann später in dieser Form ein: XX00XXXX - in Großbuchstaben - Umlaute sind kein Problem

### Check / Installation von Python 3.10

- So kannst du checken, ob Python 3.10 auf deinem System installiert ist:

  - **Auf Windows**
    - Öffne die Eingabeaufforderung:
      - Suche nach `cmd` im Startmenü und drücke Enter
      - Oder drücke `Win + R`

    - Python-Version überprüfen: 
      - Gib in der Eingabeaufforderung den folgenden Befehl ein und drücke Enter:
        > python --version
      - Alternativer Befehl (teste am besten beide):
        > python3 --version
      - Wenn Python installiert ist und der Pfad korrekt gesetzt wurde, zeigt dieser Befehl die Version von Python an, die derzeit als Standardversion zugänglich ist
        - Es sollte so etwas wie Python 3.10.x angezeigt werden, wenn Python 3.10 installiert ist
      - Wenn das System Python nicht finden kann, siehst du möglicherweise eine Fehlermeldung
        - In diesem Fall ist Python entweder nicht installiert oder nicht in der PATH-Variablen des Systems eingetragen

    - Überprüfung auf mehrere Versionen:
      - Wenn mehrere Versionen von Python installiert sind, musst du möglicherweise den spezifischen Pfad überprüfen, an dem Python 3.10 installiert ist
      - Das tust du mit dem `where` Befehl in der Eingabeaufforderung: 
        > where python
    - Der Befehl listet alle Pfade auf, an denen eine ausführbare Datei namens "python" gefunden wird
    - Du kannst dann den Pfad identifizieren, der zu Python 3.10 gehört
  
  - **Auf macOS**
    - Öffne das Terminal:
      - Du findest das Terminal im Ordner `Programme > Dienstprogramme`, oder du suchst es mit Spotlight, indem du `Cmd + Space` drückst und `Terminal` eingibst

    - Python-Version überprüfen: 
      - Gib im Terminal den folgenden Befehl ein, dann drücke Enter:
        > python --version
      - Alternativer Befehl (teste am besten beide):
        > python3 --version
      - Wenn Python installiert ist, zeigt dieser Befehl die Version von Python an, die derzeit als Standardversion zugänglich ist
        - Es sollte so etwas wie Python 3.10.x angezeigt werden, wenn Python 3.10 installiert ist
      - Wenn das System Python nicht finden kann, siehst du möglicherweise eine Fehlermeldung

      - Überprüfung auf mehrere Versionen:
        - Wenn mehrere Versionen von Python installiert sind, musst du möglicherweise den spezifischen Pfad überprüfen, an dem Python 3.10 installiert ist
        - Um alle Installationen von Python zu sehen, kannst du den `which` Befehl verwenden, um den Pfad des derzeit aktiven Python zu finden
        > which python
        > which python3
        - Oder du kannst Installationen im Homebrew Cellar auflisten (falls Homebrew verwendet wird):
        > ls /usr/local/Cellar/python@

- Python 3.10 installieren, falls notwendig

  - **Auf Windows**
    - Python herunterladen:
      - Gehe auf https://www.python.org/ zum Bereich `Downloads` und darunter auf `Windows`
      - Du siehst nun alle `Python Releases for Windows`
      - Suche nach `Python 3.10.11 - April 5, 2023`
      - Dort befindet sich eine Liste mit Download-Files
      - Bitte klicke auf `Windows installer (64-bit)` und lade die Installationsdatei herunter

    - Installationsprogramm starten:
      - Öffne die heruntergeladene Datei, um die Installation zu starten
      - **Wichtig**: bevor du auf `Install Now` klickst - aktiviere die Option `Add python.exe to PATH`
      - Dann klicke auf `Install Now` oder `Customize Installation`, wenn du spezifische Features oder Installationspfade anpassen möchtest

    - Installation abschließen:
      - Folge den Anweisungen des Installationsprogramms
      - Nach Abschluss der Installation kannst du überprüfen, ob Python erfolgreich installiert wurde, indem Sie du die Eingabeaufforderung öffnest (siehe oben) und 
      > python --version
      - eingibst und Enter drückst

  - **Auf macOS**
    - Python herunterladen:
      - Gehe auf python.org zum Bereich `Downloads` und darunter auf `macOS`
      - Du siehst nun alle `Python Releases for macOS`
      - Suche nach `Python 3.10.11 - April 5, 2023`
      - Dort befindet sich eine Installationsdatei
      - Bitte klicke auf `macOS 64-bit universal2 installer` und lade die Installationsdatei herunter

    - Den Installationsanweisungen folgen:
      - Öffne die heruntergeladene `.pkg-Datei`, um die Installation zu starten - dies startet den Installationsassistenten für Python
      - Folge den Anweisungen des Installationsprogramms
      - Du wirst aufgefordert, die Installationsart zu wählen, und musst möglicherweise dein Administratorpasswort eingeben

    - Installation abschließen:
      - Nach Abschluss der Installation kannst du überprüfen, ob Python erfolgreich installiert wurde, indem Sie du das Terminal öffnest (siehe oben) und 
      > python3 --version
      - eingibst und Enter drückst

  - **Alternative Installation über Homebrew auf macOS**
    - Falls du Homebrew verwendest, kannst du Python auch über diesen Paketmanager installieren:
      - Öffne das Terminal
      - Installiere Python 3.10 mit Homebrew:
        - Gib den Befehl 
        > brew install python@3.10 
      - ein und drücke Enter
    - Stelle sicher, dass Python 3.10 korrekt verlinkt ist:
      - Führe 
      > brew link python@3.10 --force 
      - aus, falls notwendig

    - Überprüfe die Installation:
      - Überprüfe mit 
      > python3 --version
      - ob die richtige Version installiert wurde

### Download des Projektverzeichnisses
- Bitte lege auf deiner Festplatte einen Ordner namens `labeling_task` an
- Du brauchst ca. 3.5 GB freien Speicherplatz
- Klicke auf den grün unterlegten Button `<> Code` und dann auf "Download ZIP" und speichere das Ganze am besten erstmal in deinem `Downloads` Ordner (macOS: Go > Downloads (Option+Command+L))
  - Wenn der Download beendet ist - wähle die Datei aus `exp_dualtask_labeling-productions.zip`
  - Im Datei-Explorer müsste dies erscheinen: `Extrahieren - Tools für komprimierte Ordner` - bitte darauf klicken und dann rechts auf `Alle extrahieren`
    - Es erscheint `ZIP-komprimierte Ordner extrahieren` und es ist der Pfad voreingetragen, in dem sich die zip-Datei nach dem Download befindet
    - Das kannst du so lassen und auf `Extrahieren` klicken
    - Dann erscheint der entpackte Ordner mit demselben Namen, wie die zip-Datei
  - Bitte klicke auf den Ordner bis die einzelnen enthaltenen Dateien angezeigt werden
  - Wähle ALLE enthaltenen Dateien und Ordner auf einmal aus und verschiebe ALLE enthaltenen Dateien und Ordner in den von dir angelegten Ordner `labeling_task`
  - Bitte lege einen neuen Ordner im Unterordner `stimuli` an und nenne ihn `test`
    - Es müssten sich dann zwei Ordner in `stimuli` befinden - `practice` und `test`

## Verzeichnisstruktur
- In deinem Ordner `labeling_task` sollte nun Folgendes enthalten sein:
  - 6 Python Skripte (`*.py`)
  - Eine `requirements.txt` Datei
  - Eine batch Datei (`start_labeling_task.bat`)
  - Ein Ordner `pics` mit 5 Dateien (`*.png`)
  - Ein leerer Unterordner `stimuli/test` für die Aufnahmen (die du aus BoxUP holst)
  - Ein Unterordner `stimuli/practice` indem sich 10 Aufnahmen befinden
  - Ein Ordner `.idea` 

### Download der Aufnahmen zum Labeln
- Die Aufnahmen, die du labeln sollst, befinden sich in einem Ordner auf BoxUP
- Bitte lade den gesamten Inhalt des Ordners auf deinen Rechner und verschiebe dann alle Aufnahmen (wav-Dateien) in den Ordner `stimuli/test` in `labeling_task`
- Bitte nicht den ganzen BoxUP-Ordner in `stimuli/test` verschieben, sondern NUR die enthaltenen wav-Dateien, sonst findet das Skript die wav-Dateien später nicht
- Im Unterordner `stimuli/test` müssten sich dann 2.400 `wav-Dateien` befinden

## Starten der Labeling-Aufgabe
- Klicke doppelt auf `start_experiment.bat` - das Skript tut folgendes:
   - Es prüft, ob die korrekte Python Version installiert ist
   - Es installiert einmal zu Beginn alle notwendigen Python-Packages
   - Es startet das Experiment
   - Bitte klicke immer doppelt auf `start_experiment.bat`, wenn du die Aufgabe durchführen möchtest
- Folge den Instruktionen auf dem Bildschirm

## Ergebnisse
- Wenn du alle Aufnahmen durchgehört und gelabeled hast, gib mir bitte Bescheid
- Erstelle auf BoxUP bitte einen Ordner mit deiner `labeler_ID` und teile ihn mit mir
- In den Ordner lädst du bitte Folgendes hoch:
  - Den Ordner `results` und den Ordner `randomization_lists` aus `labeler_task`
  - Darin müssten jeweils Unterordner mit deiner `labeler_ID` und verschiedene Dateien sein
    - In `results/labeler_ID` müssten sich vier `csv-Dateien` und eine `txt-Datei` befinden
    - In `randomization_lists/labeler_ID` müsste sich eine `csv-Datei` befinden

## Hilfe
Bei Problemen oder Fragen kannst du dich jederzeit an mich wenden Andrea Hofmann <andhofma@uni-potsdam.de>
