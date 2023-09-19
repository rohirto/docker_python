"""
Data Science - Reshape
Task
Given a list of numbers and the number of rows (r), reshape the list into a 2-dimensional array.
Note that r divides the length of the list evenly.

Input Format
First line: an integer (r) indicating the number of rows of the 2-dimensional array
Next line: numbers separated by the space

Output Format
An numpy 2d array of values rounded to the second decimal.

Sample Input
2
1.2 0 0.5 -1

Sample Output
[[ 1.2 0. ]
[ 0.5 -1. ]] 
"""
import numpy as np
from z_get_user_input import get_user_input, get_user_input_float

r = int(get_user_input(1)[0])

lst = get_user_input_float((r*2))
arr = np.array(lst)
print(arr.reshape((r,int(len(lst)/r))))
