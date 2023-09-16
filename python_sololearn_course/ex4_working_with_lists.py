"""Workng with list."""
# Create a list of numbers
numbers = [5, 12, 9, 7, 3, 15]

# Find the maximum element
max_num = max(numbers)

# Display the maximum element
print(f"The maximum element is {max_num}")

#indexing example - Lists are indexed - but mutable
numbers[0] = 6
print(numbers[0])

#indxing - Strings are indexed but immutable
ANIMAL = "Dog"
print(ANIMAL[0])

# Slicing [2:5] -> prints a range, [:5] prints starts till 5, [2:] from 2 till end, [:] prints all
cart = ["hello", "world", "this", "is", "slicing", 1]
print(f"Slicing example: {cart[2:5]}")

# Negative Slicing
print(f"Negative Slicing example: {cart[-6:-4]}")
