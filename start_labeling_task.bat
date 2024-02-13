@echo off
:: Check for Python and verify version 3.10
python --version 2>&1 | findstr /R "Python 3\.10\."
if errorlevel 1 (
    echo Für diese Aufgabe brauchst du Python 3.10.
    echo Bitte installiere Python 3.10 oder update deine Python-Version: https://www.python.org/
    pause
    exit
) else (
    echo Python 3.10 erkannt.
)

:: Install requirements
echo Installiere erforderliche Python-Pakete...
python -m pip install -r requirements.txt

:: Start the experiment script
echo Starte die Aufgabe...
python dualtask_labeling_experiment.py

pause
