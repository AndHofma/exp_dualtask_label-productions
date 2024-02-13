"""
This module contains predefined instructional text strings used throughout a dual-task labeling experiment. These texts
guide participants through the experiment, explaining the task, providing instructions for each phase, and offering
feedback and reminders as needed. The instructional content is structured to progressively introduce the experiment's
context, tasks, and response mechanisms, ensuring participants understand their role and how to interact with the
experiment interface.

The module is structured around several key instruction variables, each serving a specific purpose within the
experiment flow:

- `begin`: Introduces the experiment, explaining the context and the nature of the stimuli the participants will
encounter.
- `begin_1`: Details the secondary tasks that speakers performed while recording the stimuli, setting expectations for
potential errors in the recordings.
- `begin_2`: Explains the symbols and response mechanisms that participants will use to label each recording, including
how to interpret and select pictograms based on their understanding of the audio stimuli.
- `begin_3`: Describes the process for proceeding through the experiment, including how to pause and save progress, and
how to navigate between recordings.
- `begin_4`: Offers a reminder of the key instructions and how to use the response options provided.
- `test`: Marks the transition from practice to the test phase of the experiment, indicating that feedback will no
longer be provided.
- `intermediate`: Provides a temporary closure message, allowing participants to take a break if needed.
- `intermediate_1`: Welcomes participants back to the experiment and reiterates key instructions to ensure continued
understanding and proper engagement with the task.
- `end`: Congratulates participants upon completing the experiment and provides instructions for formally ending the
session.

Usage:
These instructional texts are displayed at various stages of the experiment to provide guidance, clarify expectations,
and facilitate the labeling task. They are typically presented via the experiment's graphical user interface, requiring
participants to read and acknowledge the instructions by pressing the "Enter" key to proceed.

Example:
To display the initial welcome message and instructions, the experiment script would retrieve the `begin` variable from
this module and use the PsychoPy library to render the text on screen, waiting for participant input to continue.

Note:
The instructional texts are presented in German, reflecting the language used in the recordings and the intended
participant group for this specific experiment.
"""

# Instructions
begin = """
Willkommen zur Labeling-Aufgabe \n
Du hörst im Anschluss Aufnahmen verschiedener Sprecher,
die unterschiedliche Kombinationen von drei Namen laut vorlesen.
Die Namenskombinationen wurden den Sprechern am Bildschirm 
entweder ohne (a) oder mit Klammer (b) präsentiert:
a) Lotte und Laura und Lisa
b) (Lotte und Laura) und Lisa 
Die Klammern geben an, welche der Personen gemeinsam kommen. 
Gibt es keine Klammern wie in (a), kommen alle drei Personen gemeinsam. 
Gibt es Klammern wie in (b), kommen Lotte und Laura gemeinsam 
und Lisa kommt auch, aber nicht zusammen mit Lotte und Laura. 
Die Sprecher sollten die Namen so vorlesen, dass man möglichst 
gut verstehen kann, welche Personen gemeinsam kommen.  \n 
Bitte drück die Eingabetaste (Enter), um zur nächsten Seite zu kommen.
"""

begin_1 = """
Die Sprecher mussten im zweiten Teil der Aufgabe 
zusätzlich zum Vorlesen gleichzeitig weitere Aufgaben lösen.
Sie waren dadurch abgelenkt und haben hin und wieder Fehler produziert. \n
Deine Aufgabe ist es, die Aufnahmen anzuhören und dann zu entscheiden,
zu welcher Bedingung die Aufnahmen aus deiner Sicht gehören. \n
Du kannst jede Aufnahme mehrfach anhören, bevor du dich endgültig entscheidest.
Und du kannst das Labeln stoppen, den Zwischenstand speichern und ein ander Mal weitermachen, wo du aufgehört hast. \n
Bitte drück die Eingabetaste (Enter), um zur nächsten Seite zu kommen.
"""

begin_2 = """
Nach jeder Aufnahme erscheinen drei Piktogramme und ein Text:
Piktogramm: Drei Figuren stehen zusammen | Bedeutung: Alle drei Personen kommen gemeinsam 
Piktogramm: Eine Figur mit Fragezeichen | Bedeutung: Du weißt nicht welche Bedingung gemeint ist | Wichtig: Bitte nur wählen, wenn du auch nach wiederholtem Hören nicht sicher bist
Piktogramm: Zwei Figuren stehen zusammen, eine allein | Bedeutung: Zwei Personen kommen gemeinsam, die dritte allein
Unter jedem Piktogramm siehst einen Pfeil - nach links, nach unten, nach rechts.
Das ist die entsprechende Taste auf der Tastatur, die du drücken musst, um das Piktogramm auszuwählen. \n
Text: "Aufnahme wiederholen (Drücke Taste r)" | Bedeutung: Die Aufnahme wird noch einmal abgespielt \n
Bitte drück die Eingabetaste (Enter), um zur nächsten Seite zu kommen.
"""

begin_3 = """
Sobald du dich für ein Piktogramm entschieden hast, siehst du, wieviele Aufnahmen fertig gelabeled und wieviele noch offen sind.
Du musst dann auswählen, ob du weitermachst oder ob du stoppst und zwischenspeicherst. 
Mit der Eingabetaste "Enter" wird die nächste Aufnahme abgespielt.
Mit der "Esc"-Taste kannst du die Aufgabe beenden und den Zwischenstand speichern. 
Du kannst nach dem nächsten Anmelden weitermachen, wo du aufgehört hast. \n
Bitte drück die Eingabetaste (Enter), um zur nächsten Seite zu kommen.
"""

begin_4 = """
Noch einmal zur Erinnerung:
Du hörst eine Aufnahme, danach erscheinen drei Piktogramme und die Möglichkeit, die Aufnahme zu wiederholen.
Dein Tastendruck entscheided, welches Piktogramm zur Aufnahme passt.
Drei Figuren stehen zusammen - alle drei Personen kommen gemeinsam. 
(Pfeil nach links (←) oder rechts (→))
Eine Figur mit Fragezeichen - du weißt nicht welche Bedingung gemeint ist. (Pfeil nach unten (↓))
Zwei Figuren stehen zusammen, eine allein - zwei Personen kommen gemeinsam, die dritte allein. (Pfeil nach links (←) oder rechts (→)) \n
Danach drückst du "Enter", um weiterzumachen oder "Esc", um zu stoppen. \n
Bitte drück die Eingabetaste (Enter), dann starten zwei Übungsbeispiele.
"""

test = """
Das waren die Übungsbeispiele. \n
Nun kannst du soviele Aufnahmen labeln, wie du möchtest. 
Du erhältst kein Feedback mehr zur Intention des Sprechers, 
welche Bedingung vorgelesen wurde.  \n
Bitte drücke die Eingabetaste (Enter), um zu starten.
"""

intermediate = """
Danke! Bis in Kürze! \n
Drück die Eingabetaste (Enter), um die Aufgabe zu schließen.
"""

intermediate_1 = """
Schön, dass du zurück bist.
Noch einmal zur Erinnerung:
Du hörst eine Aufnahme, danach erscheinen drei Piktogramme und die Möglichkeit, die Aufnahme zu wiederholen.
Dein Tastendruck entscheided, welches Piktogramm zur Aufnahme passt.
Drücke den Pfeil nach links (←): Drei Figuren stehen zusammen - alle drei Personen kommen gemeinsam.
Drücke den Pfeil nach unten (↓): Eine Figur mit Fragezeichen - du weißt nicht welche Bedingung gemeint ist.
Drücke den Pfeil nach rechts (→): Zwei Figuren stehen zusammen, eine allein - zwei Personen kommen gemeinsam, die dritte allein. \n
Danach drückst du "Enter", um weiterzumachen oder "Esc", um zu stoppen. \n
Bitte drück die Eingabetaste (Enter), um zu starten.
"""

end = """
Geschafft!\n
Du hast alle Aufnahmen gelabelt.
Vielen Dank.
Drück die Eingabetaste (Enter), um die Aufgabe zu schließen.
"""
