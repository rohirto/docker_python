"""Data Science - Average of Rows
In a matrix, or 2-d array X, the averages (or means) of the elements of rows is called row means.

Task
Given a 2D array, return the rowmeans.

Input Format
First line: two integers separated by spaces, the first indicates the rows of matrix X (n) 
and the second indicates the columns of X (p)
Next n lines: values of the row in X

Output Format
An numpy 1d array of values rounded to the second decimal.

2 2
1.5 1
2 2.9

Sample Output
[1.25 2.45]
"""
import numpy as np
from z_get_user_input import get_user_input, get_user_input_float

# 2 approaches - first is mine and second is chatgpt
APPROACH = int(input("Options:\n1.mine\n2.chatgpt"))   # can be "mine" or "chatgpt"
if APPROACH == 1:
    # My attempt
    n, p = get_user_input(2)
    arr = []
    for i in range(n):
        arr = arr + get_user_input_float(p)
    n_arr = np.array(arr)

    n_arr = n_arr.reshape(n,p)
    row_means = n_arr.mean(axis = 1)
    row_means = np.round(row_means, 2)
    print(row_means)
elif APPROACH == 2:
    # Code from chatgpt -> more elegant and robust try to come to this level
    # Read input
    n, p = map(int, input("enter r and c:").split()) #input().split() will be a list
                                                     # map will apply int fucntion to
                                                     # the list intput().split()
    matrix = []
    for _ in range(n):
        row = list(map(float, input("enter row elements: ").split()))   #input().split() will be a list
                                                                        # map will apply floar fucntion to
                                                                        # the list intput().split()
                                                                        # list function will convert the
                                                                        # result into list
        matrix.append(row)      # List is appended -> [[1.2, 2.3], [1.6, 4.3]]
    print(matrix)
    # Calculate row means
    row_means = np.mean(matrix, axis=1)

    # Round the row means to two decimal places
    row_means = np.round(row_means, 2)

    # Print the result
    print(row_means)
else:
    print("Invalid input")
