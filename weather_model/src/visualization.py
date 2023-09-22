"""
Visualizations Module
"""
# visualization.py
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

def view_scatter_matrix(data):
    """Plot the scatter Matrix

    Args:
        data (dataframe): merged data after combining the temperature and humidity params
    """
    #Data Visualization before Scaling
    scatter_matrix(data.iloc[:,[1,4]])
    plt.savefig("/workspaces/docker_python/weather_model/output/plot_merged.png")
    plt.show()

def plot_data(x_scaled, cluster_labels, centroids):
    """Plot the centroids

    Args:
        x_scaled (dataframe): scaled dataframe
        cluster_labels (dataframe): _description_
        centroids (_type_): _description_
    """
    # Create and save data visualization plots
    # plot the scaled data
    plt.scatter(x_scaled[:,0],
                x_scaled[:,1],
                c= cluster_labels)
    # identify the centroids
    plt.scatter(centroids[:, 0],
                centroids[:, 1],
                marker="*",
                s = 250,
                c = [0,1,2],
                edgecolors='k')

    plt.xlabel('temperature')
    plt.ylabel('humidity')
    plt.title('k-means (k=3)')
    plt.savefig("/workspaces/docker_python/weather_model/output/plot_centroid.png")
    plt.show()
