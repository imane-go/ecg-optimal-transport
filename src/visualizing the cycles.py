import wfdb
import numpy as np
from scipy.signal import resample
from scipy.stats import wasserstein_distance
import matplotlib.pyplot as plt

# Load the ECG record
record_path = "C://Users//CE//mit-bih-arrhythmia-database-1.0.0//100"
patient_record = wfdb.rdrecord(record_path)

# Load the annotation file associated with the ECG record
annotation = wfdb.rdann(record_path, 'atr')

# Get the indices corresponding to the R peaks (heartbeats)
r_peak_indices = annotation.sample

# Define the length of each cycle (e.g., a window around the R peak)
cycle_window = 0.3  # seconds, adjust as needed

# Convert cycle window from seconds to samples
fs = patient_record.fs  # sampling frequency
cycle_length = int(cycle_window * fs)

# Extract individual cycles (heartbeats)
cycles = []
for r_peak_index in r_peak_indices:
    start_index = max(0, r_peak_index - cycle_length // 2)
    end_index = min(len(patient_record.p_signal), r_peak_index + cycle_length // 2)
    cycle = patient_record.p_signal[start_index:end_index, 0]  # Assuming single-channel ECG
    cycles.append(cycle)

# Resample cycles to have the same length
max_cycle_length = max(len(cycle) for cycle in cycles)
resampled_cycles = [resample(cycle, max_cycle_length) for cycle in cycles]
