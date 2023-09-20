"""
This is my library to load custom libraries into my projects
"""

# Boston Data set
import pandas as pd
import numpy as np

boston = pd.read_csv('/workspaces/docker_python/data_science/datasets/bostondataset.csv',nrows=506)

def load_boston_data():
    return boston

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
