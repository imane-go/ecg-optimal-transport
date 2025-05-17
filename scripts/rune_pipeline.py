
from src import preprocessing, ot_distance, barycenter, visualization

def main():
    ecg_data = preprocessing.load_and_clean("data/processed/record_001.csv")

    distance_matrix = ot_distance.compute_all(ecg_data)

    barycenters = barycenter.compute_by_cluster(ecg_data, distance_matrix)

    visualization.plot_clusters(barycenters)
    visualization.save_metrics(barycenters)

if __name__ == "__main__":
    main()
