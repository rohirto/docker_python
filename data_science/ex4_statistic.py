""" Summary Statistics """
# Measures of Location - Minimum, Maximum, Mean
import pandas as pd

presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv',
                            index_col='name')
print("Exercise 1: ")
print(presidents_df.min())
print("\n")
print(presidents_df.max())
print("\n")
try:
    print(presidents_df.mean())
except TypeError as e_n:
    print(f"For some reason mean() method is not working, Error: {e_n}")
finally:
    print("\n")
print("\n")

# Quantiles
# Quantiles are cut points dividing the range of the data into
# continuous intervals with an equal number of observations.
# Median Quantile - 2 groups
# Both .quantile(0.5) and .median() result in the same output.
# Quartiles - divide a set of data into four groups
print("Exercise 2: ")
print(presidents_df['age'].quantile([0.25, 0.5, 0.75, 1]))
print("\n")

# Mean and median are usually not of the same value, unless the data is perfectly symmetric.
print("Exercise 3:")
print(presidents_df['age'].mean())

print(presidents_df['age'].median())
print("\n")

# Variance and Standard Deviation
# variance is the mean squared deviation of each data point from the mean of the entire dataset
# Standard deviation (std) is the square root of variance
# Below Examples on series
const = pd.Series([2, 2, 2])
print("Exercise 4:")
print(const.var())
print(const.std())
print("\n")
dat = pd.Series([2, 3, 4])
print(dat.mean())
print(dat.var())
print(dat.std())
print("\n")
# Outputs:
# 3.0
# 1.0

# Variance and std deviation on President Example
print("Exercise 5: ")
print(presidents_df['age'].var())
print(presidents_df['age'].std())
# Outputs:
# 43.5
# 6.595354
print("\n")
numeric_columns = ['order', 'age', 'height']
print(presidents_df[numeric_columns].std())  # Applied on columns
# Outputs:
# order: 13.136502
# age: 6.595354
# height: 6.977236
print("\n")

# Describe - describe() prints out almost all of the summary statistics
print("Exercise 6: ")
print(presidents_df.describe())
# .describe() ignores the null values, such as `NaN` (Not a Number)
print("\n")

# Categorical Variable
# A categorical variable is one that takes on a single value from a limited set of categories
# 'party' column in president example is such that
#  We can check the unique values and corresponding frequency by using .value_counts():
print(" Exercise 7: ")
print(presidents_df['party'].value_counts())
print("\n")
print(presidents_df['party'].describe())
