"""
dualtask_labeling_configuration.py

This module configures the environment for a dual-task labeling experiment using PsychoPy. It includes functionalities
for resource path management, window creation, stimuli initialization, participant information collection, and
progress tracking. It supports essential operations such as accessing stimuli files, saving experiment results, and
managing the participant's progress through the experiment phases.
"""
from psychopy import monitors, visual, gui, core
import random
import os
import datetime
import sys
import csv


def resource_path(relative_path):
    """
    Constructs an absolute path to a resource, taking into account whether the application is running from a compiled
    executable or a standard Python script.

    Parameters:
    - relative_path (str): The relative path to the resource.

    Returns:
    - str: The absolute path to the resource.
    """
    if getattr(sys, 'frozen', False):
        # If we're running as a bundled exe, set the base path as one level above the executable
        base_path = os.path.join(os.path.dirname(sys.executable), "..")
    else:
        # If we're running in a normal Python environment
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)


# Define paths for accessing various experiment resources.
test_stimuli_path = resource_path('stimuli/test/')
practice_stimuli_path = resource_path('stimuli/practice/')
results_path = resource_path('results/')
pics_path = resource_path('pics/')
random_path = resource_path('randomization_lists/')


def create_window():
    """
    Creates and returns a PsychoPy window object with predefined settings for the experiment.

    Returns:
    - psychoPy.visual.Window: A window object for displaying the experiment's visual stimuli.
    """
    current_monitor = monitors.Monitor(name='testMonitor')

    # Create and return a window for the experiment
    return visual.Window(monitors.Monitor.getSizePix(current_monitor),
                         monitor="testMonitor",
                         allowGUI=True,
                         fullscr=True,
                         color=(255, 255, 255)
                         )


def save_pictogram_order(labeler_id, pictograms_order, positions, labels):
    """
    Saves the order of pictograms used in the experiment to a CSV file for a given labeler.

    Parameters:
    - labeler_id (str): Unique identifier for the participant.
    - pictograms_order (list): List of pictogram filenames.
    - positions (list): List of positions for each pictogram.
    - labels (list): List of labels associated with each pictogram.
    """

    filename = f"{labeler_id}_pictogram_order.csv"
    filepath = os.path.join(results_path, labeler_id, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Pictogram', 'PositionX', 'PositionY', 'Label'])
        for pictogram, (posX, posY), label in zip(pictograms_order, positions, labels):
            writer.writerow([pictogram, posX, posY, label])
    print(f"Saved pictogram order to {filepath}")


def load_pictogram_order(labeler_id):
    """
    Loads the order of pictograms from a CSV file for a given labeler, if available.

    Parameters:
    - labeler_id (str): Unique identifier for the participant.

    Returns:
    - tuple: (pictograms_order, positions, labels) if file found, otherwise (None, None, None).
    """

    filename = f"{labeler_id}_pictogram_order.csv"
    filepath = os.path.join(results_path, labeler_id, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            pictograms_order = []
            positions = []
            labels = []
            for row in reader:
                pictograms_order.append(row['Pictogram'])
                positions.append((float(row['PositionX']), float(row['PositionY'])))
                labels.append(row['Label'])
            print(f"Loaded pictogram order from {filepath}")
            return pictograms_order, positions, labels
    print("No pictogram order file found.")
    return None, None, None


def initialize_stimuli(window, labeler_id):
    """
    Initializes and returns the stimuli to be used in the experiment based on the labeler's pictogram order.

    Parameters:
    - window (psychoPy.visual.Window): The window where stimuli will be displayed.
    - labeler_id (str): Unique identifier for the participant.

    Returns:
    - tuple: Collection of PsychoPy visual stimuli objects.
    """

    pictograms_order, loaded_positions, loaded_labels = load_pictogram_order(labeler_id)

    if not pictograms_order:
        print("Initializing with default pictogram order.")
        # Define default order and positions if not loaded
        pictograms_order = [os.path.join(pics_path, 'no_bracket.png'), os.path.join(pics_path, 'bracket.png')]
        positions = [(-0.65, 0), (0.65, 0)]
        labels = ['left', 'right']
        random.shuffle(positions)  # Shuffle positions to randomize
        save_pictogram_order(labeler_id, pictograms_order, positions, labels)
    else:
        positions = loaded_positions
        labels = loaded_labels
        print("Using loaded pictogram order.")

    # Create fixation cross
    fixation_cross = visual.ShapeStim(window,
                                      vertices=((0, -0.13), (0, 0.13), (0, 0), (-0.09, 0), (0.09, 0)),
                                      lineWidth=15,
                                      closeShape=False,
                                      lineColor="black",
                                      name='fixation'
                                      )

    # Create pictograms
    bracket_pic = visual.ImageStim(window,
                                   image=pictograms_order[1],
                                   pos=positions[1]
                                   )

    nobracket_pic = visual.ImageStim(window,
                                     image=pictograms_order[0],
                                     pos=positions[0]
                                     )

    questionmark_pic = visual.ImageStim(window,
                                        image=os.path.join(pics_path, 'question.png'),
                                        pos=(0, 0)
                                        )

    audio_pic = visual.ImageStim(window,
                                 image=pics_path + 'audio.png',
                                 pos=(0, 0),
                                 name='audio_pic')

    # Labels for the positions
    bracket_pos_label = labels[1]
    nobracket_pos_label = labels[0]

    # arrow parameters
    arrowPositions = [[0.7, -0.7], [-0.7, -0.7], [0, -0.8]]  # position in the x-y-coordinate system
    arrowOrientations = [0, -180, -270]  # rotation in degrees
    arrowSize = 0.2  # size in pixels?
    arrows = []  # empty list to append to

    # generate all arrows in correct orientation
    for i in range(3):
        arrow = visual.ImageStim(window,
                                 image=os.path.join(pics_path, 'next.png'),
                                 pos=arrowPositions[i],
                                 size=arrowSize,
                                 ori=arrowOrientations[i]
                                 )
        arrows.append(arrow)

    return fixation_cross, bracket_pic, bracket_pos_label, nobracket_pic, nobracket_pos_label, pictograms_order, \
        audio_pic, questionmark_pic, arrows


def get_participant_info():
    """
    Displays a GUI dialog to collect participant information at the start of the experiment.

    Returns:
    - dict: Collected participant information if dialog is confirmed, otherwise quits the experiment.
    """
    exp_data = {
        'experiment': 'labeling_experiment',
        'cur_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        'labeler': 'labelerID'
    }
    # Dialogue box to get participant information
    info_dialog = gui.DlgFromDict(dictionary=exp_data,
                                  title='Labeling Production Data from Dualtask',
                                  fixed=['experiment', 'cur_date']
                                  )

    if info_dialog.OK:
        return exp_data
    else:
        core.quit()


# Function to append a single result to the CSV file
def append_result_to_csv(writer, result, output_file):
    """
    Appends the result of a trial to the appropriate CSV file.

    Parameters:
    writer (csv.writer): The CSV writer object to use for writing.
    result (list): A list containing the data for a single trial.
    output_file (File object): The CSV file object to use for writing.
    """
    writer.writerow(result)
    output_file.flush()
    os.fsync(output_file.fileno())


def get_progress_file_path(labeler_id, phase):
    """
    Generate the file path for a labeler's progress file for a given phase.

    Parameters:
    labeler_id (str): The ID of the labeler.
    phase (str): The phase of the experiment ('practice' or 'test').

    Returns:
    str: File path for the labeler's progress file for the given phase.
    """
    progress_directory = os.path.join(results_path, labeler_id)
    os.makedirs(progress_directory, exist_ok=True)  # Ensure the directory exists
    filename = f"{labeler_id}_{phase}_progress.csv"
    return os.path.join(progress_directory, filename)


def get_randomization_file_path(labeler_id, phase):
    """
    Generate the file path for a labeler's randomization file based on the phase (practice or test).

    Parameters:
    labeler_id (str): The ID of the labeler.
    phase (str): The phase of the experiment ('practice' or 'test').

    Returns:
    str: File path for the labeler's randomization file for the given phase.
    """
    randomization_directory = os.path.join(random_path, labeler_id)
    os.makedirs(randomization_directory, exist_ok=True)  # Ensure the directory exists
    filename = f"{labeler_id}_{phase}_randomized_stimuli.csv"
    return os.path.join(randomization_directory, filename)


def load_progress(progress_file_path):
    """
    Load the progress from a given CSV file.

    Parameters:
    progress_file_path (str): Path to the progress CSV file.

    Returns:
    list: List of stimuli filenames that have been processed.
    """
    if not os.path.exists(progress_file_path):
        return []  # Return empty list if file doesn't exist

    with open(progress_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader]
