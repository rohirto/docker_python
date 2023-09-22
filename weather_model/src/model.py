"""
Modelling Module 
"""
# model.py
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

def preprocess_and_scale_data(data):
    """Basic Preprocessing Done here, removing zeroes and all, Scale data

    Args:
        data (data frame): merged dataframe
    """
    # Preprocess and scale the data
    # Return the scaled data

    # Feature Dataframe
    x_n = data[['humidity', 'temperature']]
    x_n = x_n.dropna()

    # Do the Scaling
    # instantiate the scaler
    scale = StandardScaler()
    # compute the mean and std to be used later for scaling
    scale.fit(x_n)
    # Now we Transform/Scale the data around 0,0
    x_scaled = scale.transform(x_n)

    # return the scaled data
    return x_scaled

def train_kmeans_model(x_scaled, num_clusters):
    """Train the model here

    Args:
        x_scaled (scaled dataframe): scaling is done to properly fit the model
        num_clusters (int): no of centroids to have, it is based on elbow method
    """
    # Train a KMeans clustering model
    # Return the trained model
    # instantiate the model
    kmeans = KMeans(n_clusters=num_clusters)
    # fit the model
    kmeans.fit(x_scaled)
    # make predictions


    #return the trained mode
    return kmeans

def predict_clusters(model, x_scaled):
    """Predict the clusters based on training

    Args:
        model (kmmeans cluster): Our model chosen, kmeans cluster
        x_scaled (dataframe): Scaled dataframe
    """
    # Predict clusters using the trained KMeans model
    # Return cluster labels
    y_pred = model.predict(x_scaled)
    return y_pred
