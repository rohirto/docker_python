"""
This is my library to load custom libraries into my projects
"""

# Boston Data set
import pandas as pd
boston = pd.read_csv('/workspaces/docker_python/data_science/datasets/bostondataset.csv',nrows=506)

def load_boston_data():
    """Returns the pandas dataframe made from bostondata csv

    Returns:
        df: Dataframe containing the boston housing data
    """
    # Calculate column means (ignoring NaN values)
    column_means = boston.mean()
    # Fill the Nan with the mean value as the Linear regression wont work
    for col in boston.columns:
        boston[col] = boston[col].fillna(column_means[col])
    return boston

#Iris Dataset
iris = pd.read_csv('/workspaces/docker_python/data_science/datasets/iris.csv',nrows=152)

def load_iris_data():
    """Returns the pandas dataframe made from bostondata csv

    Returns:
        df: Dataframe containing the boston housing data
    """
    # Calculate column means (ignoring NaN values)
    column_means = iris.mean()
    # Fill the Nan with the mean value as the Linear regression wont work
    for col in iris.columns:
        iris[col] = iris[col].fillna(column_means[col])
    return iris

# import pandas as pd  # doctest: +SKIP
# import numpy as np

# data_url = "http://lib.stat.cmu.edu/datasets/boston"
# raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
# data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
# target = raw_df.values[1::2, 2]

# class boston_data:
#     def __init__(self,data_t,target_t):
#         self.data = data_t
#         self.target = target_t

# def load_boston_data():
#     b_data = boston_data(data,target)
#     return b_data
