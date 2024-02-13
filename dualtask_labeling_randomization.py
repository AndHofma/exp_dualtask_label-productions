"""
dualtask_labeling_randomization.py

This module is designed to support the loading and randomization of stimuli for a dual-task labeling experiment.
It facilitates the handling of stimuli files, ensuring that only the necessary stimuli are presented to participants
during each phase of the experiment and that these stimuli are randomized according to specific constraints to prevent
bias and ensure the reliability of the experiment outcomes.
"""

import os
import random
import csv


def load_stimuli(stimuli_path, progress_file=None):
    """
    Load stimuli files from a specified directory and its subdirectories,
    optionally excluding files listed in a progress file.

    Parameters:
    - stimuli_path (str): The directory path where stimuli files and their speaker-specific subdirectories are located.
    - progress_file (str, optional): A CSV file path listing filenames of stimuli that have already been processed.

    Returns:
    - list: A list of paths for stimuli that have not yet been processed.
    """
    all_stimuli = []
    # Recursively walk through stimuli directory to find all .wav files
    for root, dirs, files in os.walk(stimuli_path):
        for file in files:
            if file.endswith('.wav'):
                # Here, instead of adding the full path, we only add the filename
                all_stimuli.append(file)  # Changed from full_path to file

    # If a progress file is provided and exists, filter out labeled stimuli
    if progress_file and os.path.exists(progress_file):
        with open(progress_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            labeled_stimuli = [row[0] for row in reader]
        return [stimulus for stimulus in all_stimuli if stimulus not in labeled_stimuli]

    return all_stimuli


def extract_filename_info(filename):
    """
    Extracts information from a filename based on a predefined pattern.

    Parameters:
    - filename (str): The filename to parse.

    Returns:
    - dict: A dictionary containing extracted information from the filename.
    """
    info = {"filename": filename}
    # Split the filename by underscores
    parts = filename.split("_")

    if "single" in filename:
        # Parsing for filenames that contain "single"
        info["exp"] = parts[0]
        info["speaker"] = parts[1]
        info["trial"] = parts[4]
        info["stimulus_origin"] = "_".join([parts[2], parts[3]])
        info["name_stim"] = "_".join(parts[5:]).split(".wav")[0]
        info["condition"] = parts[-1].split(".wav")[0]
    elif "gating" in filename:
        # Parsing for filenames that contain "single"
        info["exp"] = parts[0]
        info["speaker"] = parts[1]
        info["trial"] = parts[3]
        info["stimulus_origin"] = "_".join([parts[0], parts[2]])
        info["name_stim"] = "_".join(parts[4:]).split(".wav")[0]
        info["condition"] = parts[-1].split(".wav")[0]
    else:
        # Parsing for filenames that do not contain "single"
        info["exp"] = parts[0]
        info["speaker"] = parts[1]
        info["trial"] = parts[6]
        info["stimulus_origin"] = "_".join(parts[2:6])
        info["name_stim"] = "_".join(parts[7:]).split(".wav")[0]
        info["condition"] = parts[-1].split(".wav")[0]

    return info


def constraint_randomization(stimulus_data):
    """
    Applies constraints to the randomization of stimulus data to ensure a balanced distribution.

    Parameters:
    - stimulus_data (list of dict): The stimulus data to randomize, where each item is a dictionary containing
      details of one stimulus.

    Returns:
    - list of dict: The randomized stimulus data adhering to the specified constraints.
    """
    stimuli_copy = stimulus_data.copy()
    random.shuffle(stimuli_copy)

    randomized_stimuli = []
    while stimuli_copy:
        valid_stimulus_found = False
        for stimulus in stimuli_copy:
            if (
                sum(stim['condition'] == stimulus['condition'] for stim in randomized_stimuli) < 4 and
                sum(stim['name_stim'] == stimulus['name_stim'] for stim in randomized_stimuli) < 3 and
                sum(stim['speaker'] == stimulus['speaker'] for stim in randomized_stimuli) < 3 and
                sum(stim['stimulus_origin'] == stimulus['stimulus_origin'] for stim in randomized_stimuli) < 4
            ):
                randomized_stimuli.append(stimulus)
                stimuli_copy.remove(stimulus)
                valid_stimulus_found = True
                break
        if not valid_stimulus_found:
            print(
                "Warning: Constraints cannot be satisfied for remaining stimuli. Adding remaining stimuli in random order.")
            randomized_stimuli.extend(stimuli_copy)
            break
    return randomized_stimuli


def randomize_stimuli(stimuli_files):
    """
    Randomizes a list of stimulus filenames based on specific constraints.

    Parameters:
    - stimuli_files (list of str): The filenames of the stimuli to randomize.

    Returns:
    - list of str: The filenames of the stimuli after applying constraint randomization.
    """
    # Extract stimulus data for each file
    stimulus_data = [extract_filename_info(filename) for filename in stimuli_files]

    # Apply constraint randomization
    randomized_stimuli_data = constraint_randomization(stimulus_data)

    # Now, extract the filenames from the data
    randomized_stimuli = [data['filename'] for data in randomized_stimuli_data]

    return randomized_stimuli


def load_and_randomize(stimuli_path, participant_info, phase):
    """
    Loads stimuli for a given phase and participant, applying randomization as needed.

    Parameters:
    - stimuli_path (str): Directory path containing stimuli files.
    - participant_info (dict): Information about the participant.
    - phase (str): The current phase of the experiment ('practice' or 'test').

    Returns:
    - tuple: (list of str, str) The randomized list of stimuli filenames and the path to the progress file.
    """

    # Determine the progress file name based on the phase
    progress_file_name = f"{participant_info['labeler']}_{phase}_progress.csv"
    progress_directory = os.path.join('results', participant_info['labeler'])
    os.makedirs(progress_directory, exist_ok=True)  # Ensure this directory exists before using it
    progress_file_path = os.path.join(progress_directory, progress_file_name)

    # For the practice phase, load stimuli without randomization and return them with their progress file path
    if phase == "practice":
        practice_stimuli = load_stimuli(stimuli_path, progress_file=progress_file_path)
        return practice_stimuli, progress_file_path

    # Before attempting to correct the directory path, it's mistakenly concatenated. Let's correct it:
    randomization_directory = os.path.join('randomization_lists', participant_info['labeler'])
    os.makedirs(randomization_directory, exist_ok=True)  # This ensures the directory is created before use

    # Then, define the file path within this directory
    randomized_file_path = os.path.join(randomization_directory, f"{phase}_randomized_stimuli.csv")

    # Check if the randomized list already exists for this labeler and phase
    if os.path.exists(randomized_file_path):
        # Load the existing randomized list from CSV
        with open(randomized_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip the header row
            randomized_stimuli = [row[0] for row in reader]
        print(f"Loaded existing randomized stimuli from {randomized_file_path}")
    else:
        # Load and randomize stimuli files
        stimuli_files = load_stimuli(stimuli_path)
        randomized_stimuli = randomize_stimuli(stimuli_files)

        # Save the randomized list directly here, removing the need for a separate function
        with open(randomized_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # writer.writerow(["filename"])  # Optionally include a header
            for stimulus in randomized_stimuli:
                writer.writerow([stimulus])
        print(f"Saved new randomized stimuli to {randomized_file_path}")

    return randomized_stimuli, progress_file_path



