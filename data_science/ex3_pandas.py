""" 
Tutorial on Pandas - From Sololearn Datascience Course
Pandas vs Numpy:
What if we want to inspect the data on Abraham Lincoln in 'height_age_arr'
but cannot remember his integer position. Is there a convenient way to access
the data by indexing the name of the president like 
    print(height_age_arr['Abraham Lincoln'])
It will result in error. 

Thus we shift to Pandas
As numpy ndarrays are homogeneous, pandas relaxes this requirement
and allows for various dtypes in its data structures.
"""
import pandas as pd

# Series - one building block in pandas
# Pandas Series is a one-dimensional labeled array that can
# hold data of any type (integer, string, float, python objects, etc.),
# similar to a column in an excel spreadsheet
# The axis labels are collectively called index.
print(pd.Series([1, 2, 3], index=['a', 'b', 'c'])) # with index

#numpy array and dictonary can also be used as a Series
series = pd.Series({'a': 1, 'b': 2, 'c':3})
print(series['a'])

# Think of Series as numpy 1darray with index or row names.
# Series is 1D thus not very useful thus we go for dataframes
# DataFrames are 2darrays with both row and column labels.
# One way to create a DataFrame from scratch is to pass in a dict.
# Think of DataFrame as a collection of the Series.
wine_dict = {
    'red_wine': [3, 6, 5],
    'white_wine':[5, 0, 10]
}
sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"]) # sales consists of two Series
                                                                  # one named under "red_wine",
                                                                  # the other "white_wine"
print(sales)

# we can access each series by calling its name:
print(sales['white_wine'])

presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv',
                            index_col='name')

print(presidents_df.shape)  # prints the shape 45 rows and 4 cols
print(presidents_df.shape[0]) # no of rows -> 45
print(presidents_df.size) # no of elements in the object

# Shape and size works the same as numpy array atrributes

#Inspect a Dataframe - Head and Tail - This functions are useful for quickly testing
# the objects
# Instead of looking at the entire dataframe, just have a peep
# To see the first few lines in a DataFrame, use .head();
print(presidents_df.head(n=3))  # if n not mentioned then by default 5 is given
# if we want to see the last few rows, we can use .tail(),
print(presidents_df.tail())

# Inspect the dataframe - Info
print(presidents_df.info()) # note the non null count section, imp to root out null values
print("\n")

# Rows with loc - locate - no need memorize the columns ->
# label and condtional statements,
# not integer
print(presidents_df.loc['Abraham Lincoln'])
print(presidents_df.loc['Abraham Lincoln'].shape)
# Slicing also possible with .loc
print(presidents_df.loc['Abraham Lincoln':'Ulysses S. Grant'])
print("\n")

# Rows with .iloc -> we do know the integer position(s), we can use .iloc to access the row(s).
print(presidents_df.iloc[15])
print("\n")

# Slicing using iloc
print(presidents_df.iloc[15:18])

# Columns
print(presidents_df.columns)
print("\n")
#To select multiple columns, we pass the names in a list, resulting in a DataFrame.
print(presidents_df[['height','age']].head(n=3))
print("\n")

# access columns order, age, and height,
print(presidents_df.loc[:, 'order':'height'].head(n=3))
