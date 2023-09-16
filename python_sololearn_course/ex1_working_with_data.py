"""Working with Data examples."""
# Input length and width of a rectangle
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Calculate the area
area = length * width

"""
new string formatting mechanism known as Literal String Interpolation or more commonly as F-strings
 (because of the leading f character preceding the string literal). The idea behind f-strings is to make string interpolation simpler.

To create an f-string, prefix the string with the letter “ f ”. The string itself can be formatted in much the same way that you
 would with str.format(). F-strings provide a concise and convenient way to embed python expressions inside string literals 
 for formatting. 
"""
# Display the result
print(f"The area of the rectangle is {area}")

# Data type checking
print(f"Area variable type: {type(area)}")

# Convert the data to integer
print(f"Area changed data type to int: {int(area)}")

# Comparision operators
print(f"Various comparision operators shows boolean data: {5 > 7} {7 > 5}")

# logical Operators
print(f"Logical operators: {(5 > 7) and (1 < 2) or False}")
