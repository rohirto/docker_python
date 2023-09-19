""" Tutorial 1 - Getting started with Numpy  """
import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173,
           175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180,
           170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193,
           182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_arr = np.array(heights)     #convert list into numpy array object
print((heights_arr > 188).sum())    # numpy array object method
print(heights_arr.size)             # size attribute of numpy array object
print(heights_arr.shape)            # dimension of array, output is a tuple,

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56,
        46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62,
        43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]
heights_and_ages = heights + ages   # combine the 2 list
# convert a list to a numpy array
heights_and_ages_arr = np.array(heights_and_ages)
print(heights_and_ages_arr.shape)   # prints (90, ), still 1D, just height appended to age
                                    # need to reshape it, 2nd row height
print(heights_and_ages_arr.reshape((2,45)))

#numpy is homogenous dataset, all of same datatype
print(heights_arr.dtype)    #will print int64

#Indexing and slicing in Numpy
heights_and_ages_arr = heights_and_ages_arr.reshape((2,45)) # Reshape the 1D array into 2D
print(heights_and_ages_arr[1,2])    # Access the 2nd element in row (height of) and 3rd element
                                    # in col (3rd President),
                                    # Indexing starts from zero
print(heights_and_ages_arr[0, :3])  # Slicing ex, 1st row (Hieght of), first 3 elements
                                    # Height of first 3 presidents
print(heights_and_ages_arr[:, 3])   # Entire 4th col, height and age of 4th Pres

# Assigning Single Values, thus such arrays are mutable
heights_arr[3] = 165    # In 1D array, just like a python list
heights_and_ages_arr[0, 3] = 165    # In 2D array, row 1(height of), col 4 (4th Prez)
print(heights_and_ages_arr)
heights_and_ages_arr[0,:] = 180     # Changing vlaues using Slicing, height of all in col changed
print(heights_and_ages_arr)
heights_and_ages_arr[:2, :2] = 0    # Upper left first 2 elements of row and col assigned zero
print(heights_and_ages_arr)

# Assigning an Array to an Array
# a 1darray or a 2darry can be assigned to a subset of another 2darray, as long as their
# shapes match
new_record = np.array([[180, 183, 190], [54, 50, 69]]) # Create a new numpy array with new data
heights_and_ages_arr[:, 42:] = new_record   # Note that shapes match - 2 rows and last 3 cols
print(heights_and_ages_arr)

# Combining 2 arrays
# Horizontal stack
# Horizontal stack ->
# arr1 = [1,2,3] 1x3 array
# arr2 = [4,5,6] 1x3 array
# arr3 = np.hstack((arr1,arr2))
# Now arr3 will be arr3 -> [1,2,3,4,5,6] 1x6 (Columns were increased)

ages_arr = np.array(ages)
print(ages_arr[:3,])

heights_arr = heights_arr.reshape((45,1)) # It will create 45 rows and 1 col
ages_arr = ages_arr.reshape((45,1))

height_age_arr = np.hstack((heights_arr, ages_arr)) # Horizontally stack it on each other,
                                                    # along axis 1, coloumn
print(height_age_arr.shape)                         # It will be 45x2
print(height_age_arr[:3,:])  # 2 cols of first 3 rows will be printed -> 3x2

# Vertical Stack
# Vertical stack ->
# arr1 = [1,2,3] 1x3 array
# arr2 = [4,5,6] 1x3 array
# arr3 = np.vstack((arr1,arr2))
# Now arr3 will be arr3 -> [[1,2,3],[4,5,6]] 2x3 (Rows were increased)
heights_arr = heights_arr.reshape((1,45)) # It will create 1 rown and 45 cols
ages_arr = ages_arr.reshape((1,45))

height_age_arr = np.vstack((heights_arr, ages_arr)) # Vertically stack it on each other,
                                                    # along axis 0, row
                                                    # It will be 2x45
print(height_age_arr.shape)
print(height_age_arr[:,:3]) # 3 cols of all (2) rows will be printed

# Concatenate

heights_arr = heights_arr.reshape((45,1))   # 45 x 1
ages_arr = ages_arr.reshape((45,1))
# height_age_arr = np.hstack((heights_arr, ages_arr))
height_age_arr = np.concatenate((heights_arr, ages_arr), axis=1) # Same effect as hstack,
                                                                 # when axis =1 is passed

print(height_age_arr.shape)
print(height_age_arr[:3,:])

heights_arr = heights_arr.reshape((1,45))   # 1 x 45
ages_arr = ages_arr.reshape((1,45))
# height_age_arr = np.vstack((heights_arr, ages_arr))
height_age_arr = np.concatenate((heights_arr, ages_arr), axis=0) # Same effect as vstack,
                                                                 # when axis =0 is passed

print(height_age_arr.shape)
print(height_age_arr[:,:3])

# Operations
# Mathematical Operations on Numpy Arrays
# to convert the height from cm to feet
heights_arr = heights_arr.reshape((45,1)) # 45 x 1
ages_arr = ages_arr.reshape((45,1))
height_age_arr = np.hstack((heights_arr, ages_arr)) # 45 x 2

print(height_age_arr[:,0]*0.0328084)    # Apply operation to all elements in 1st col
                                        # Op is to convert cm to feet
                                        # returns a new 1D array
# Numpy Array methods
print(height_age_arr.sum())             # Sum of all heights and ages -> 10577
print(height_age_arr.sum(axis = 0))     # Sum across rows, 45 x 2 array, coloumn sum
                                        # So all heights (row) in first col are added -> 8102
                                        # all ages (row) in second col are added -> 2475
# If you want to do row sum ie, add a the elements of a row, use axis =1
# Other operations, such as .min(), .max(), .mean(), work in a similar way to .sum().

# Comparisions of Numpy Array
print(height_age_arr[:, 1] < 55)    # Compare all rows of 2nd col (age) with 55
                                    # If age < 55, then print boolean accordingly
young_presidents_count = height_age_arr[:, 1] < 55
print(young_presidents_count.sum()) # print sum of all Trues, will tell us how
                                    # many presidents were younger than 55
# Masking and Subsetting
# Create a subset based on a mask critera
# Subset of presidents whose ht is greater than 182 cm
mask = height_age_arr[:, 0] >= 182  # Compare all rows of 1st col (height)
print(mask.sum())                   # This will print no of tall presidents

tall_presidents = height_age_arr[mask, ] # Apply the mask condtion to our array
                                         # Store new sub array in new variable
print(tall_presidents.shape)             # See the dimension
print (tall_presidents)                  # Print the sub array

# Mask of Multiple Criteria -> height > 182 cm and age < 50yrs, use '&'
mask = (height_age_arr[:, 0]>=182) & (height_age_arr[:,1]<=50) #Multiple Masks
tall_and_young_presidents = height_age_arr[mask, ]
print(tall_and_young_presidents.shape)
print(tall_and_young_presidents)
