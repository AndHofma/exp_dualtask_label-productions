"""
This module contains utility functions for verifying the existence and readiness of various directory paths required
for a dual-task labeling experiment. It focuses on ensuring that all necessary directories for storing test stimuli,
practice stimuli, pictures, results, and randomization lists are present before the experiment begins. If any required
directories are missing, the module will raise an exception to prevent the experiment from proceeding without the
necessary file structure in place.
"""

import os


def check_config_paths(test_stimuli_path, practice_stimuli_path, results_path, pics_path, random_path):
    """
    Verifies the existence of specified directories crucial for running the dual-task labeling experiment. If certain
    directories do not exist, the function will attempt to create them (for results and randomization lists), or raise
    an exception for critical missing directories (test/practice stimuli and pictures).

    Parameters:
    - test_stimuli_path (str): The path to the directory containing test stimuli.
    - practice_stimuli_path (str): The path to the directory containing practice stimuli.
    - results_path (str): The path where experiment results will be saved.
    - pics_path (str): The path to the directory containing picture files used in the experiment.
    - random_path (str): The path where randomization lists are stored.

    Raises:
    - Exception: If any of the test stimuli, practice stimuli, or pictures directories do not exist.

    Side Effects:
    - Creates the results and randomization directories if they do not already exist, ensuring that the experiment
      can proceed with saving outputs and applying randomization as required.
    """

    # Check if the input directory for test stimuli exists
    if not os.path.exists(test_stimuli_path):
        # Raise exception if not
        raise Exception("No input folder detected. Please make sure that "
                        "'test_stimuli_path' is correctly set in the configurations")
    # Check if the input directory for test stimuli exists
    if not os.path.exists(practice_stimuli_path):
        # Raise exception if not
        raise Exception("No input folder detected. Please make sure that "
                        "'practice_stimuli_path' is correctly set in the configurations")
    # Check if the pics directory exists
    if not os.path.exists(pics_path):
        # Raise exception if not
        raise Exception("No pics folder detected. Please make sure that "
                        "'pics_path' is correctly set in the configurations")
    # Check if the output directory exists, if not, create it
    if not os.path.exists(results_path):
        os.mkdir(results_path)
    # Check if the path to randomization files exists, if not, create it
    if not os.path.exists(random_path):
        os.mkdir(random_path)
