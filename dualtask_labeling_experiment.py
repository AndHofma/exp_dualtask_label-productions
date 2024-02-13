"""
dualtask_labeling_experiment.py

This module orchestrates the execution of a dual-task labeling experiment using PsychoPy. It manages the experiment's
flow from initialization, through practice and test phases, to completion, ensuring data collection and participant
interaction are handled smoothly.

The script checks and verifies necessary paths, gathers participant information, initializes the PsychoPy window and
stimuli, and controls the flow of the experiment based on participant progress. It utilizes modular design, with
functionality spread across several external modules for path checking, configuration, instruction management,
and trial execution.
"""

# Import necessary libraries and modules for the experiment setup and execution.
# For core PsychoPy functionalities like timing and quitting the experiment.
from psychopy import core
# For handling file and directory paths.
import os
# Import custom modules for specific functionalities.
# Checks if necessary paths exist.
from dualtask_labeling_path_check import check_config_paths
# Configuration and setup functions.
from dualtask_labeling_configuration import (create_window, initialize_stimuli, get_participant_info,
                                             practice_stimuli_path, test_stimuli_path, results_path,
                                             pics_path, random_path, load_progress)
# Core experiment functions.
from dualtask_labeling_functions import display_text_and_wait, run_trial_phase
# Instructional text.
from dualtask_labeling_instructions import (begin, begin_1, begin_2, begin_3, begin_4, test,
                                            intermediate, intermediate_1, end)
# Stimuli randomization function.
from dualtask_labeling_randomization import load_and_randomize


# Verify that input and output paths required for the experiment are available.
check_config_paths(test_stimuli_path, practice_stimuli_path, results_path, pics_path, random_path)

# Gather participant information through a GUI dialog.
participant_info = get_participant_info()

# Load and randomize stimuli for both practice and test phases, based on participant information.
practice_stimuli, practice_progress_file_path = load_and_randomize(practice_stimuli_path, participant_info, 'practice')
test_stimuli, test_progress_file_path = load_and_randomize(test_stimuli_path, participant_info, 'test')

# Initialize the main window where the experiment will be displayed.
window = create_window()

# Initialize stimuli to be used throughout the experiment.
fixation_cross, bracket_pic, bracket_pos_label, nobracket_pic, nobracket_pos_label, pictograms_order, \
    audio_pic, questionmark_pic, arrows = initialize_stimuli(window, participant_info['labeler'])

# Create a flag file path to indicate whether the practice phase has been completed.
practice_done_flag = os.path.join('results', participant_info['labeler'], 'practice_done.txt')

# Check whether the practice phase has been completed and load the progress for the test phase.
practice_done = os.path.exists(practice_done_flag)
test_progress = load_progress(test_progress_file_path)

# If the practice phase is not done, display instructions and run the practice phase.
if not practice_done:
    # Sequentially display the introduction and instructions before starting the practice phase.
    display_text_and_wait(begin, window)
    display_text_and_wait(begin_1, window)
    display_text_and_wait(begin_2, window)
    display_text_and_wait(begin_3, window)
    display_text_and_wait(begin_4, window)

    # Clear the screen before starting the practice phase.
    window.flip()

    # Execute the practice phase trials.
    run_trial_phase(practice_stimuli, 'practice', participant_info, practice_stimuli_path,
                                          fixation_cross, bracket_pic, nobracket_pic, window, nobracket_pos_label,
                                          bracket_pos_label, audio_pic, questionmark_pic, arrows,
                                          practice_progress_file_path)

    # Mark the practice phase as completed by creating a flag file.
    with open(practice_done_flag, 'w') as file:
        file.write('done')
    display_text_and_wait(test, window)
    window.flip()
else:
    # If practice is completed, check whether to start or resume the test phase.
    if test_progress:
        # If directly resuming the test phase (and practice is done)
        display_text_and_wait(intermediate_1, window)
    else:
        # Starting or resuming the test phase after practice
        display_text_and_wait(test, window)

# Clear the screen before starting the test phase.
window.flip()

# Execute the test phase trials.
run_trial_phase(test_stimuli, 'test', participant_info, test_stimuli_path, fixation_cross, bracket_pic,
                nobracket_pic, window, nobracket_pos_label, bracket_pos_label, audio_pic, questionmark_pic, arrows,
                test_progress_file_path)

# Check if all test stimuli have been labeled.
all_test_done = len(test_stimuli) == len(load_progress(test_progress_file_path))

# Display the appropriate end screen based on whether all test stimuli have been labeled.
if all_test_done:
    display_text_and_wait(end, window)
else:
    display_text_and_wait(intermediate, window)

# Close the experiment window and exit the experiment.
window.close()
core.quit()

