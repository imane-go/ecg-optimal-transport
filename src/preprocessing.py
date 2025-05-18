import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import resample

record_path = "C://Users//CE//mit-bih-arrhythmia-database-1.0.0//100"
record = wfdb.rdrecord(record_path)
annotation = wfdb.rdann(record_path, 'atr')

# Extract the ECG Signal (Channel 0) 
ecg_signal = record.p_signal[:, 0]
fs = record.fs  # Sampling frequency
r_peaks = annotation.sample

# Define Heartbeat Window Around Each R Peak 
window_size_sec = 1.0  # seconds
window_size_samples = int(fs * window_size_sec)

# Extract ECG Cycles Centered on R Peaks 
cycles = []
for r in r_peaks:
    start = max(0, r - window_size_samples // 2)
    end = min(len(ecg_signal), r + window_size_samples // 2)
    cycle = ecg_signal[start:end]
    
    # Only keep cycles of the expected length
    if len(cycle) == window_size_samples:
        cycles.append(cycle)

# Optional: Resample each cycle to fixed length 
target_length = 20
resampled_cycles = [resample(c, target_length) for c in cycles]

# Plot First 5 Cycles
plt.figure(figsize=(10, 8))
for i in range(5):
    plt.subplot(5, 1, i + 1)
    plt.plot(resampled_cycles[i], color='blue')
    plt.title(f"Cycle {i+

