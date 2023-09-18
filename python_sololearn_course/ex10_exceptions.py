""" Exceptions example """
def divide(a_n, b_n):
    """Function to demonstrate exceptions

    Args:
        a_n (_type_): _description_
        b_n (_type_): _description_
    """
    try:
        result = a_n / b_n  # Attempt to perform division
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError as e_n:
        print(f"Error: {e_n}")
    else:
        print(f"Result of division: {result}")
    finally:
        print("Execution completed.")

# Test the divide function with different inputs
try:
    divide(10, 2)   # Successful division
    divide(5, 0)    # Division by zero
    divide(8, '2')  # Type error
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Ex of Raise
    age = int(input("Welcome to Pub, Enter Age:"))
    try:
        if age < 18:
            raise ValueError
    except ValueError:
        print("UnderAge!")
    except TypeError:
        print("Invalid input")
    else:
        print("Enter the pub")
