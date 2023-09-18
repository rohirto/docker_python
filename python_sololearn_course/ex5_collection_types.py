"""Various Collection tyes like Dictonaries, Tuples and Sets"""
# Basic Dictonary
nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

# Input a string
text = input("Enter a string: ")

# Create a dictionary to store letter counts
""" Dictonaries comes in Key: Value Pair"""
letter_counts = {}

# Count occurrences of each letter
for char in text:
    if char.isalpha():
        char = char.lower()
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

# Display letter counts
for char, count in letter_counts.items():
    print(f"'{char}' appears {count} times")
print(letter_counts.get('r',"Not Found"))

#Tuple Example
# Creating a tuple with elements, elements immutable, faster access
fruits_tuple = ("apple", "banana", "cherry")
# Slicing a tuple
selected_fruits = fruits_tuple[1:3]
print(selected_fruits)


# Finding the index of an element
index = fruits_tuple.index("banana")
# Counting occurrences of an element
count = fruits_tuple.count("cherry")

# Iterating through a tuple using a for loop
for fruit in fruits_tuple:
    print(fruit)


# Creating a tuple without parentheses (tuple packing)
point = 3, 4, 7, 8, 9
# Unpacking a tuple into variables
x, y, *z = point
print(f"x: {x} y: {y} z:{z}")

#sets
skills = {'Python', 'HTML', 'CSS', 'SQL'}
job_skills = {'HTML', 'NodeJS', 'C#'}

matched_skills = skills & job_skills  #Intersection &, Union |
print(matched_skills.pop())
