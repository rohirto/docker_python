# main.py
from src.data_loader import load_humidity_data, load_temperature_data
from src.data_preprocessing import preprocess_data
from src.model import preprocess_and_scale_data, train_kmeans_model, predict_clusters
from src.visualization import plot_data

def main():
    """Main fucntion
    """
     # Load data
    humidity_data = load_humidity_data()
    temperature_data = load_temperature_data()

     # Data preprocessing
    merged_data = preprocess_data(humidity_data, temperature_data)

    # Preprocess and scale data
    x_scaled = preprocess_and_scale_data(merged_data)

    # Train KMeans model
    num_clusters = 3  # Adjust as needed
    kmeans_model = train_kmeans_model(x_scaled, num_clusters)

    # Predict clusters
    cluster_labels = predict_clusters(kmeans_model, x_scaled)

    # Plot data
    plot_data(x_scaled, cluster_labels, kmeans_model.cluster_centers_)

if __name__ == "__main__":
    main()
