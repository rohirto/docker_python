"""
Data Preprocessing
"""
# data_preprocessing.py
import pandas as pd

def data_evaluation(data):
    """Function to See the Data Evaluation, sees shape, head and describe

    Args:
        data (dataframe): Pandas Dataframe
    """
    print(f"{data.Name} Shape: {data.shape}")
    print(f"{data.Name} Head:\n{data.head()} ")
    print(f"{data.Name} Summary Statistics:\n{data.describe()}")
    print("\n")
    print(f"{data.Name} Columns:\n{data.columns}")


def preprocess_data(humidity_data, temperature_data):
    """Preprocess the data, take 2 dataset and merge the (humidity and temperature)

    Args:
        humidity_data (dataframe): Humidity Dataframe
        temperature_data (dataframe): Temperature Dataframe

    Returns:
        Dataframe: Merged Dataframe containing Humidity and Temperature
    """
    # Data preprocessing steps, e.g., dropping columns, removing zeros, merging dataframes
    # Ensure that humidity_data and temperature_data are cleaned and preprocessed
    # Return the merged dataframe
    # Drop context Frame
    humidity_data.drop('context_humidity', axis=1, inplace=True)
    temperature_data.drop('context_temperature', axis = 1, inplace=True)

    # Remove Zero from the dataset
    humidity_data = humidity_data[humidity_data['humidity'] != 0]
    temperature_data = temperature_data[temperature_data['temperature'] != 0]

    # Convert Unix timestamps to datetime objects
    humidity_data['Datetime'] = pd.to_datetime(humidity_data['timestamp'], unit='ms')
    temperature_data['Datetime'] = pd.to_datetime(temperature_data['timestamp'], unit='ms')

    # Sort both DataFrames by the 'Datetime' column
    humidity_data.sort_values(by='Datetime', inplace=True)
    temperature_data.sort_values(by='Datetime', inplace=True)

    # Set the tolerance in seconds
    tolerance = pd.Timedelta(seconds=10)

    # Merge dataframes based on the common timestamps within the tolerance
    merged_df = pd.merge_asof(humidity_data, temperature_data,
                          on='Datetime', direction='nearest', tolerance=tolerance)

    # Drop the 'Datetime' column as it's no longer needed
    merged_df.drop(columns=['Datetime'], inplace=True)
    merged_df.Name = 'merged frame'
    data_evaluation(merged_df)
    return merged_df
