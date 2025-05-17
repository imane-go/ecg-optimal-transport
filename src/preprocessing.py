import wfdb
import matplotlib.pyplot as plt

patient_record = wfdb.rdrecord("C://Users//CE//mit-bih-arrhythmia-database-1.0.0//100")

patient_record = wfdb.rdrecord("C://Users//CE//mit-bih-arrhythmia-database-1.0.0//100")
plt.savefig('100')
wfdb.plot_wfdb(patient_record) 

import numpy as np
import wfdb
import matplotlib.pyplot as plt

# Load the ECG record
patient_record = wfdb.rdrecord("C://Users//CE//mit-bih-arrhythmia-database-1.0.0//100")

# Extract the ECG signal and time indices
ecg_signal = patient_record.p_signal[:, 0]  # Assuming the first signal is the ECG signal
time = np.arange(len(ecg_signal)) / patient_record.fs

# Specify the start and end samples for the zoomed-in portion
start_sample = 1000
end_sample = 2000

# Slice the signal and time arrays to get the zoomed-in portion
zoomed_ecg_signal = ecg_signal[start_sample:end_sample]
zoomed_time = time[start_sample:end_sample]

# Plot the zoomed-in portion of the ECG signal
plt.figure(figsize=(10, 4))
plt.plot(zoomed_time, zoomed_ecg_signal, color='blue')
plt.title('Zoomed-In ECG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

import wfdb
import numpy as np
import matplotlib.pyplot as plt

# Load the ECG record
record_path = "C://Users//CE//mit-bih-arrhythmia-database-1.0.0//100"
patient_record = wfdb.rdrecord(record_path)

# Load the annotation file associated with the ECG record
annotation = wfdb.rdann(record_path, 'atr')

# Get the indices corresponding to the R peaks (heartbeats)
r_peak_indices = annotation.sample

# Define the length of each cycle (e.g., a window around the R peak)
cycle_window = 1# seconds, adjust as needed

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

# Plot the first few cycles for visualization
num_cycles_to_plot = 5
plt.figure(figsize=(5, 13))
for i in range(num_cycles_to_plot):
    plt.subplot(num_cycles_to_plot, 1, i+1)
    plt.plot(cycles[i], color='blue')
    plt.title(f"Cycle {i+1}")
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.grid(True)

plt.tight_layout()
plt.show()
