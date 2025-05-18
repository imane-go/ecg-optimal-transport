
import numpy as np

cycle_length = len(resampled_cycles[0])

p_wave_range = (int(0.1 * cycle_length), int(0.25 * cycle_length))
qrs_range    = (int(0.3 * cycle_length), int(0.5 * cycle_length))
t_wave_range = (int(0.55 * cycle_length), int(0.75 * cycle_length))

ecg_feature_vectors = []

for cycle in resampled_cycles:
    p_wave   = cycle[p_wave_range[0]:p_wave_range[1]]
    qrs_wave = cycle[qrs_range[0]:qrs_range[1]]
    t_wave   = cycle[t_wave_range[0]:t_wave_range[1]]

    # Concatenate all waves into a single feature vector
    feature_vector = np.concatenate([p_wave, qrs_wave, t_wave])
    ecg_feature_vectors.append(feature_vector)

ecg_feature_vectors = np.array(ecg_feature_vectors)  # shape: (num_cycles, total_wave_samples)
