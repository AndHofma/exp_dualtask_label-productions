"""
dualtask_labeling_functions.py

Module for defining functions used in the dual-task labeling experiment. It includes functions for presenting trials,
showing messages, displaying text and waiting for user input, and managing trial phases. This module utilizes PsychoPy
to handle audio-visual stimuli, user interactions, and data recording, supporting the experiment's core functionalities.
"""
# Import necessary libraries for audio-visual presentation, event handling, and file operations.
from psychopy import prefs
# Set the preferred audio library to ensure compatibility and performance.
prefs.hardware['audioLib'] = ['ptb', 'sounddevice', 'pygame', 'pyo']
# Now, import sound - the order is important
from psychopy import sound, core, event, visual
import os
import datetime
import time
from dualtask_labeling_configuration import load_progress
from dualtask_labeling_randomization import extract_filename_info
from psychopy.hardware import keyboard
import csv


def present_trial(window, fixation_cross, bracket_pic, nobracket_pic, recording, kb, audio_pic, questionmark_pic, arrows):
    """
    Present a single trial, including the fixation cross, audio stimulus, and response options.

    Parameters:
    - window: The PsychoPy window object where stimuli are displayed.
    - fixation_cross, bracket_pic, nobracket_pic, audio_pic, questionmark_pic: Visual stimuli objects.
    - recording: The audio stimulus to be played during the trial.
    - kb: A PsychoPy keyboard object for detecting user input.
    - arrows: Visual stimuli objects representing response options.

    Returns:
    - response_key: The key pressed by the participant as their response.
    - nr_repetitions: The number of times the audio stimulus was repeated.
    """
    # Initialize the text displayed for repeating the audio stimulus.
    repeat_text = visual.TextStim(window, text="Aufnahme wiederholen (r)", pos=(0, 0.6), color="black")
    # Initialize the counter for audio stimulus repetitions.
    nr_repetitions = 0

    # Allow for repetition of the stimulus until a response is made.
    while True:
        fixation_cross.draw()
        window.flip()
        # Display the fixation cross for 1 second.
        core.wait(1.0)
        # Clear the fixation cross.
        window.flip()

        audio_pic.draw()
        recording.play()
        window.flip()
        # Wait for the audio to finish plus 500ms pause.
        core.wait(recording.getDuration() + 0.5)

        # Display response options.
        bracket_pic.draw()
        questionmark_pic.draw()
        nobracket_pic.draw()
        repeat_text.draw()
        for arrow in arrows:
            arrow.draw()
        window.flip()

        # Clear any previous keyboard events.
        kb.clearEvents()
        # Extract the name of the key pressed.
        keys = kb.waitKeys(keyList=['left', 'down', 'right', 'r'])  # Wait until a key is pressed

        response_key = keys[0].name  # Get the name of the key that was pressed

        # If 'r' is pressed, increment the repetition counter.
        if response_key == 'r':
            nr_repetitions += 1
        else:
            # Any other key breaks the loop and proceeds.
            break
    # Clear the screen after the response.
    window.flip()
    # Brief pause before continuing to the next trial.
    core.wait(1)

    return response_key, nr_repetitions


def show_message(window, message, wait_for_keypress=True, duration=1, text_height=0.1):
    """
    Show a message on the screen.

    Parameters:
    message (str): The message to display.
    wait_for_keypress (bool, optional): Whether to wait for a keypress. Defaults to True.
    duration (float, optional): Time in seconds to wait if wait_for_keypress is False. Defaults to 1.
    text_height (float, optional): The height of the text. Defaults to 0.1.
    """
    text_stim = visual.TextStim(window, text=message, wrapWidth=2, height=text_height, color="black")
    text_stim.draw()
    window.flip()
    if wait_for_keypress:
        event.waitKeys(keyList=['return'])
    else:
        core.wait(duration)


def display_and_wait(element, window):
    """
    Displays a given screen element, flips the window, and then waits for any key press.

    Args:
        element: A psychopy visual element (TextStim, ImageStim, etc.) to be displayed on the screen.
        window: A psychopy.visual.Window object where the element will be displayed.

    Returns:
        keys: List of the keys that were pressed while waiting.
    """
    # Draw the provided element and flip window
    element.draw()
    window.flip()
    # Wait for any key to be pressed to display the next screen
    keys = event.waitKeys(keyList=['return'])

    return keys


def display_text_and_wait(text_string, window):
    """
    This function creates a TextStim object from a provided string, then draws it and waits for any key press.

    Args:
        text_string: The string to be displayed.
        window: The window to draw on.

    Returns:
        keys: A list of the keys that were pressed.
    """
    text_stim = visual.TextStim(window, text=text_string, color='black', wrapWidth=2)

    return display_and_wait(text_stim, window)


def get_output_file_path(labeler_id):
    """
    Generates and returns the file path for saving the experiment's results for a specific labeler.

    Parameters:
    - labeler_id (str): Unique identifier for the participant or labeler.

    Returns:
    - str: The file path where the labeler's results should be saved.
    """
    output_directory = os.path.join('results', labeler_id)  # Construct the directory path for results.
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)  # Create the directory if it doesn't exist.
    # Return the file path, assuming a consistent naming convention for result files.
    return os.path.join(output_directory, f"{labeler_id}_results.csv")


def run_trial_phase(stimuli_files, phase, participant_info, stimuli_path, fixation_cross, bracket_pic, nobracket_pic,
                    window, nobracket_pos_label, bracket_pos_label, audio_pic, questionmark_pic, arrows,
                    progress_file_path):
    """
    Executes a specific phase (practice or test) of the experiment, presenting each stimulus file to the participant
    and recording their responses.

    Parameters:
    - stimuli_files (list): Filenames of stimuli to be presented during the trial phase.
    - phase (str): Indicates the current phase of the experiment ('practice' or 'test').
    - participant_info (dict): Contains information about the participant such as ID and demographic details.
    - stimuli_path (str): Directory path where stimulus files are located.
    - fixation_cross, bracket_pic, nobracket_pic, audio_pic, questionmark_pic (visual.ImageStim):
    Visual stimuli used in the trials.
    - window (visual.Window): The PsychoPy window object for stimulus presentation.
    - nobracket_pos_label, bracket_pos_label (str): Position labels for the stimuli.
    - arrows (list): Visual indicators for response options.
    - progress_file_path (str): Path to the file tracking the progress of the participant through the stimuli.

    Returns:
    - None. Results of the trials are saved to a CSV file.
    """
    # Initial setup for displaying progress and handling user input.
    progress_display = visual.TextStim(window, text='', pos=(0, 0), color='black')
    # Create text stimuli for "next" and "stop"
    next_text = visual.TextStim(window, text="Weiter (Enter)", pos=(-0.5, -0.6), color="black")
    stop_text = visual.TextStim(window, text="Stoppen und Speichern (Esc)", pos=(0.5, -0.6), color="black")

    # Load progress
    labeled_stimuli = load_progress(progress_file_path)
    # Count stimuli in progress file
    labeled_count = len(labeled_stimuli)

    # Filter out labeled stimuli from stimuli_files
    stimuli_files = [file for file in stimuli_files if file not in labeled_stimuli]

    # For displaying progress later after each trial
    total_files = len(stimuli_files) + len(labeled_stimuli)

    kb = keyboard.Keyboard()  # Initialize the keyboard

    # Define the path in results for each labeler
    subj_path_results = os.path.join('results', participant_info['labeler'])
    # Create the directory if it doesn't exist
    if not os.path.exists(subj_path_results):
        os.makedirs(subj_path_results)

    start_time = time.time()
    start_time_str = datetime.datetime.fromtimestamp(start_time).strftime('%H:%M:%S')
    trial_counter = 1

    # Generate output filename using the participant's labeler ID
    output_filename = get_output_file_path(participant_info['labeler'])

    # Check if the file already exists to determine if we need to write headers
    file_exists = os.path.exists(output_filename)

    with open(output_filename, 'a', newline='') as output_file:
        writer = csv.writer(output_file)
        headers = ['experiment', 'labelerID', 'date', 'trial', 'phase', 'response', 'response_condition', 'accuracy',
                   'braPic_position', 'nobPic_position', 'recording_processed', 'recording_nr_repetitions',
                   'recording_speaker', 'recording_name_stim', 'recording_condition', 'recording_experiment',
                   'recording_origin', 'recording_trial', 'start_time', 'end_time', 'duration']
        if not file_exists:
            writer.writerow(headers)

        # Initialize a list to track processed stimuli
        processed_stimuli = []

        for stimulus_file in stimuli_files:
            stimulus = extract_filename_info(stimulus_file)

            recording = sound.Sound(os.path.join(stimuli_path, stimulus_file), sampleRate=48000)
            response_key, nr_repetitions = present_trial(window, fixation_cross, bracket_pic, nobracket_pic, recording,
                                                         kb, audio_pic, questionmark_pic, arrows)

            # Determine correct answer and accuracy
            correct_answer = 'left' if (stimulus['condition'] == 'nob' and nobracket_pos_label == 'left') or (
                        stimulus['condition'] == 'bra' and bracket_pos_label == 'left') else 'right'
            accuracy = 1 if response_key == correct_answer else 2 if response_key == 'down' else 0

            # Determine the response condition based on the key pressed and the position labels
            if response_key == nobracket_pos_label:
                response_condition = 'nob'
            elif response_key == bracket_pos_label:
                response_condition = 'bra'
            else:
                response_condition = 'unknown'  # For responses that don't match either condition

            if phase == 'practice':
                feedback = "Richtig!" if response_key == correct_answer else "Weiß nicht!" \
                    if response_key == 'down' else "Falsch!"
                show_message(window, feedback, wait_for_keypress=False, text_height=0.3)

            # Record end time and duration
            end_time = time.time()
            end_time_str = datetime.datetime.fromtimestamp(end_time).strftime('%H:%M:%S')
            duration = end_time - start_time
            hours, remainder = divmod(duration, 3600)
            minutes, seconds = divmod(remainder, 60)
            duration_str = '{:02d}:{:02d}:{:02d}'.format(int(hours), int(minutes), int(seconds))

            # Add the processed stimulus file to the list
            processed_stimuli.append(stimulus_file)
            # Update progress file
            labeled_count += 1

            # Display progress
            progress_display.setText(f"{labeled_count} von {total_files} Aufnahmen gelabeled")
            # Before each trial, draw the progress display and then flip the window
            progress_display.draw()

            # Display "next" and "stop" options
            next_text.draw()
            stop_text.draw()
            window.flip()

            # Store trial data
            trial_data = [participant_info['experiment'], participant_info['labeler'], participant_info['cur_date'],
                          trial_counter, phase, response_key, response_condition, accuracy, bracket_pos_label,
                          nobracket_pos_label, stimulus_file, nr_repetitions, stimulus['speaker'],
                          stimulus['name_stim'], stimulus['condition'], stimulus["exp"], stimulus["stimulus_origin"],
                          stimulus["trial"], start_time_str, end_time_str, duration_str]

            # Write data to csv file directly here
            writer.writerow(trial_data)

            # Clear the keyboard buffer before checking for "next" or "stop" input
            event.clearEvents(eventType='keyboard')
            keys = event.waitKeys(keyList=['return', 'escape'])

            # Check if the user wants to stop the experiment
            if 'escape' in keys:
                if phase == 'practice':
                    # Display the message for practice phase decision
                    decision_message = "Übungsbeispiele beenden und mit dem Labeln beginnen - Drücke Enter."
                    decision_stim = visual.TextStim(window, text=decision_message, pos=(0, 0), color="black",
                                                    height=0.09)
                    decision_stim.draw()
                    window.flip()
                    event.waitKeys(keyList=['return'])

                    print("Moving to the test phase...")
                    break

                print("Experiment paused by the user. Saving progress...")
                break  # Exit the loop if the escape key is pressed

            # Increment trial counter
            trial_counter += 1

        # After the loop, update the progress file with all processed stimuli
        with open(progress_file_path, 'a', newline='') as csvfile:
            progress_writer = csv.writer(csvfile)
            for stimulus_file in processed_stimuli:
                progress_writer.writerow([stimulus_file])
