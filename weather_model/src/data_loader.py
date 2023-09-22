"""
Data Loader Module

The Data sets are outout of Ubidots, data for 1 month (Aug - Sept)
"""
import pandas as pd

def load_humidity_data():
    """Reads csv and returns pd Dataframe

    Returns:
        dataframe: Humidity Dataframe
    """
    # Load humidity data from CSV and perform any necessary preprocessing
    humidity_data = pd.read_csv("/workspaces/docker_python/weather_model/data/humidity_data.csv")
    # Data preprocessing steps here
    return humidity_data

def load_temperature_data():
    """Reads csv and returns pd Dataframe

    Returns:
        dataframe: Temperature Dataframe
    """
    # Load temperature data from CSV and perform any necessary preprocessing
    temperature_data = pd.read_csv("/workspaces/docker_python/weather_model/data/temperature_data.csv")
    # Data preprocessing steps here
    return temperature_data
