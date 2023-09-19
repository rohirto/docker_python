"""
To find the value based on a condition, we can use the groupby operation. 
Think of groupby doing three steps: split, apply, and combine
1. he split step breaks the DataFrame into multiple DataFrames based on the
    value of the specified key
2. the apply step is to perform the operation inside each smaller DataFrame
3. the last step combines the pieces back into the larger DataFrame 

A groupby Object is different from dataframes
"""
import pandas as pd
import numpy as np

# Groupby method
print("Exercise 1: ")
presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv',
                            index_col='name')
print(presidents_df.groupby('party')) # The .groupby("party") returns a DataFrameGroupBy object,
                                      # not a set of DataFrames
# To produce a result, apply an aggregate (.mean()) to this DataFrameGroupBy object
print(presidents_df.groupby('party').mean())
print(presidents_df.groupby('party').std())
print("\n")

# Aggregation
# perform multiple operations on the groupby object using .agg() method
print("exercise 2: ")
print(presidents_df.groupby('party')['height'].agg(['min', np.median, max]))
print("\n")

print(presidents_df.groupby('party')  # Create a groupby object
  .agg({'height': [np.median, np.mean], # apply aggregate method to it,
        'age': [min, max]}))            # Here a dictonary is passed 
                                        # ({'column': [methods]})
    