"""Functions example."""
# Function to calculate factorial
def factorial(n_fact):
    """Function to calculate factorial"""
    if n_fact == 0:
        return 1
    else:
        return n_fact * factorial(n_fact - 1)

def swap(arg_a, arg_b):
    """Swap 2 variables

    Args:
        arg_a (variable): can be abythin
        arg_b (variable): can be anything
    """
    print(f"Before Swapping a: {arg_a} b: {arg_b}")
    arg_b, arg_a = arg_a, arg_b
    print(f"After Swapping a: {arg_a} b: {arg_b}")

# Input a number
num = int(input("Enter a number: "))

# Calculate and display factorial
result = factorial(num)
print(f"The factorial of {num} is {result}")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
swap(a,b)
