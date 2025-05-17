
from src import preprocessing, feature_extraction, wasserstein_barycenter

def main():
    ecg_data = preprocessing.load_and_clean("data/processed/record_001.csv")

    features = feature_extraction.compute_all(ecg_data)

    barycenter = wasserstein_barycenter.compute_by_cluster(ecg_data, distance_matrix)


if __name__ == "__main__":
    main()
