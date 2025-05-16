# Optimal Transport theory overview :
This project explores Optimal Transport (OT) theory in machine learning, focusing on the Wasserstein distance and Wasserstein barycenter. Unlike traditional metrics like Euclidean distance, Wasserstein distance captures the geometry and support of data distributions, making it significantly more precise and robust—especially when comparing non-overlapping or structured data like images, time series, or text embeddings.

These tools have become increasingly important in modern ML, powering advances in generative modeling (e.g., WGANs), clustering, and distributional learning.

🔗 For a foundational introduction, see:
[Cuturi, M. (2013). Sinkhorn Distances: Lightspeed Computation of Optimal Transport. NeurIPS.]
(https://arxiv.org/abs/1306.0895)


# ECG Arrhythmia Trajectory Modeling Using Optimal Transport
🎯 **Objective**
This project aims to develop a preventive diagnostic tool for cardiovascular diseases by analyzing how a patient's ECG signal evolves over time. The core idea is to represent each patient's cardiac state using a Wasserstein barycenter, then track how this representation moves relative to established disease patterns. The long-term goal is to predict the emergence of cardiovascular conditions before clinical symptoms appear, enabling earlier intervention and better outcomes.

📚 **About the Project**
This is an ongoing scientific research project that explores the intersection of:

- ECG signal processing

- Optimal Transport theory

- Time-series analysis

- Unsupervised learning & clustering

The current focus is on extracting meaningful representations from ECG recordings using Wasserstein barycenters, which summarize the electrical activity of the heart for each patient at a given checkup.

🔍 **Current Status**
✅ ECG signals processed into cardiac cycles
✅ Key points detected (P wave, QRS complex, T wave)
✅ Wasserstein barycenter calculated per patient

🚧 **Next steps (planned):**

Define barycenters for disease-specific clusters

Measure OT distances between patient barycenters and disease clusters

Analyze trajectory trends to detect convergence toward specific conditions

Build a clustering-based prediction pipeline

🗃️ **Dataset**
Source: MIT-BIH Arrhythmia Database (v1.0.0)

Contains annotated ECG recordings from multiple patients with various arrhythmia types.

Each recording is segmented into individual heartbeats and further analyzed to extract temporal and morphological patterns.

🧠 **Method Summary**
1. Cycle Extraction
ECG signals are divided into individual cardiac cycles for each patient.

2. Wave Detection
Key electrical events (P, QRS, T waves) are identified to capture relevant features.

3. Barycenter Computation
For each patient, a Wasserstein barycenter is computed from the set of cycles, providing a single, representative distribution of their heart activity.

4. Future Work: Disease Modeling & Prediction
The next phase will focus on defining barycenters for various heart diseases and comparing patient barycenters to these disease barycenters using Optimal Transport distance.

📈 **Visual Outputs (So Far)**
The repo includes:

- Sample barycenters for individual patients

- Visual comparison between cycles and their corresponding barycenter

- Planned: OT distance evolution plots over time

🚀 **Why This Matters** 
This approach introduces a continuous, geometry-based perspective to ECG monitoring. Rather than waiting for a binary diagnosis, patients could be tracked as their heart patterns approach or move away from disease states, allowing for preventive cardiovascular care.
