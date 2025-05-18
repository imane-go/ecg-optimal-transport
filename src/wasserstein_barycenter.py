import numpy as np
import matplotlib.pyplot as plt
import ot  

resampled_cycles = np.array(resampled_cycles)  

# Normalize each cycle to form a probability distribution 
resampled_cycles = np.maximum(resampled_cycles, 0)  
resampled_cycles /= np.sum(resampled_cycles, axis=1, keepdims=True)  

# Support (assuming all signals are sampled on the same grid)
n_points = resampled_cycles.shape[1]
x = np.linspace(0, 1, n_points)  # Uniform grid

# Compute Wasserstein barycenter using POT
barycenter = ot.barycenter.barycenter_1d(resampled_cycles, x)

# Plot original cycles and Wasserstein barycenter
plt.figure(figsize=(10, 10))
for cycle in resampled_cycles:
    plt.plot(x, cycle, color='blue', alpha=0.3)
plt.plot(x, barycenter, color='red', linewidth=2, label='Wasserstein Barycenter')
plt.title('Wasserstein Barycenter of ECG Cycles')
plt.xlabel('Normalized Time')
plt.ylabel('Amplitude (Probability)')
plt.grid(True)
plt.legend()
plt.savefig('wasserstein_barycenter.png')
plt.show()
