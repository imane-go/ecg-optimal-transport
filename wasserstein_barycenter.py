# Compute the average cycle (Wasserstein barycenter)
barycenter = np.mean(resampled_cycles, axis=0)

# Plot the original cycles and their barycenter for visualization
plt.figure(figsize=(10, 10))
for cycle in resampled_cycles:
    plt.plot(cycle, color='blue', alpha=0.5)  # Original cycles
plt.plot(barycenter, color='red', linewidth=2)  # Barycenter
plt.title('Average Cycle (Wasserstein Barycenter)')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig('wasserstein barycenter.png')
plt.show()
