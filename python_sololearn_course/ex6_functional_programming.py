""" Functional Programming in Python """
import time
#Higher Order Fubctons -> Take other functions as arguments and return them as results
# Define a higher-order function that applies a given function to each element in a list
def apply_function_to_list(func, input_list):
    """Sample Func to demonstarte Higher order functions

    Args:
        func (function input): input func
        input_list (list): list on which func will be applied

    Returns:
        func: appied on list
    """
    return [func(x) for x in input_list]

# Define a function to square a number
#Pure Functions
# Pure function to calculate the square of a number
def square(x_n):
    """Square Function

    Args:
        x (integer): input

    Returns:
        integer: square of input
    """
    return x_n ** 2  # The result will always be 16 for input 4

numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_function_to_list(square, numbers)
print(squared_numbers)

# Lambdas, map and filter
# Using map() with a lambda function to square each element in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# Using filter() with a lambda function to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Using list comprehension to square each element in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)

# Using list comprehension to filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# Define a generator function to generate squares of numbers from 1 to n
# Generators dont have menory restrictions -> yield one item at atime
def square_generator(n_arg):
    """Generator example demo

    Args:
        n (_type_): _description_

    Yields:
        _type_: _description_
    """
    for i in range(1, n_arg + 1):
        yield i ** 2    # Yield statement is used to define a generator,
                        # replacing the return of a fucntion to provide a result
                        # w/o destroying the local variables

# Use the generator to print squares of numbers from 1 to 5
for square in square_generator(5):
    print(square)

# Result can be converted to List also
print(list(square_generator(5)))

#Decorators ex 1
def decor(func):
    """Decor Func demo, wraps the func with wrap function 

    Args:
        func (function): _description_
    """
    def wrap():
        print("=====================")
        func()
        print("=====================")
    return wrap

def print_text():
    """Simple func to be wrapped
    """
    print("Hello World")

#Method 1 to decor
decorated = decor(print_text)
decorated()

#Method 2 to Decor
@decor
def print_text2():
    """Demo Func
    """
    print("Heello world!")

print_text2()

#Decorators ex 2
# Define a decorator function to measure the execution time of a function
def timing_decorator(func):
    """measure the execution time of a function

    Args:
        func (inp func): whoes time needs to be calculated
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

# Apply the decorator to a function
@timing_decorator
def slow_function():
    """Function takess 2 sec to execute
    """
    time.sleep(2)

slow_function()

#Recursion
# Calculate factorial of a number using recursion
def factorial(n_arg):
    """Calculate Factorial

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n_arg == 0:
        return 1
    else:
        return n_arg * factorial(n_arg - 1)

f_result = factorial(5)  # Calculates 5!
print(f_result)

# *args and **kwargs
# Function that accepts variable positional (*args) and keyword (**kwargs) arguments
# *args is tuple of args,
# args vs kwargs -> kwargs is just key value paired
def variable_args_kwargs(arg1, *args, kwarg1="default", **kwargs):
    """_summary_

    Args:
        arg1 (_type_): This is the first argument, will need this
        kwarg1 (str, optional): First argment of kwarg. Defaults to "default".
    """
    print(f"arg1: {arg1}")
    print(f"args: {args}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwargs: {kwargs}")

# Example usage
variable_args_kwargs("Hello", 1, 2, 3, kwarg1="custom", name="Alice", age=30)
