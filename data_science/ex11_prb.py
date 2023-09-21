""" 
Data Science - Binary Disorder
Confusion matrix of binary classification.

For binary classifications, a confusion matrix is a two-by-two matrix to visualize the performance of an algorithm. Each row of the matrix represents the instances in a predicted class while each column represents the instances in an actual class.

Task
Given two lists of 1s and 0s (1 represents the true label, and 0 represents the false false) of the same length, output a 2darrary of counts, each cell is defined as follows

Top left: Predicted true and actually true (True positive)
Top right: Predicted true but actually false (False positive)
Bottom left: Predicted false but actually true (False negative)
Bottom right: Predicted false and actually false (True negative)

Input Format
First line: a list of 1s and 0s, separated by space. They are the actual binary labels.
Second line: a list of 1s and 0s, the length is the same as the first line. They represented the predicted labels.

Output Format
A numpy 2darray of two rows and two columns, the first row contains counts of true positives and false positives and the second row contains counts of false negatives and true negatives.

Sample Input
1 1 0 0
1 0 0 0

Sample Output
[[1., 0.],
[1., 2.]]
"""

y_true = [int(x) for x in input().split()]
y_pred =  [int(x) for x in input().split()]

import numpy as np

out = np.array([[0,0], [0,0]])
np_true = np.array(y_true)
np_pred = np.array(y_pred)

np_sum = np_true + np_pred 
np_diff = np_true - np_pred 

out[0][0] = np.count_nonzero(np_sum  == 2)
out[1][1] = np.count_nonzero(np_sum  == 0)
out[0][1] = np.count_nonzero(np_diff  == -1)
out[1][0] = np.count_nonzero(np_diff == 1)

print(out.astype(float))
     
#BINaRY DISORDER