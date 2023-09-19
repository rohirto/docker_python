""" 
Lib to ensure proper data input by user

"""
def get_user_input(p_n):
    """Get user inpt

    Args:
        p_n (int): no of input desired from user

    Raises:
        ValueError: if that no not equal to user input

    Returns:
        int: user input
    """
    while True:
        try:
            user_input = input(f"Enter no of {p_n} as space-separated integers: ")
            values = [int(x) for x in user_input.split()] # List cpmprehension to take input
                                                            # from user and convert to int
            if len(values) != p_n:
                raise ValueError(f"Please enter exactly {p_n} integers separated by a space.")
            return values
        except ValueError as e_n:
            print(f"Invalid input: {e_n}. Please try again.")
def get_user_input_float(p_n):
    """Get user input in float form

    Args:
        p_n (int): no of input desired

    Raises:
        ValueError: When no of input is not appropriate

    Returns:
        list: list created by list comprehension
    """
    while True:
        try:
            user_input = input(f"Enter {p_n} Elements as space-separated floats: ")
            values = [float(x) for x in user_input.split()] # List cpmprehension to take input
                                                            # from user and convert to float
            if len(values) != p_n:
                raise ValueError(f"Please enter exactly {p_n} floats separated by a space.")
            return values
        except ValueError as e_n:
            print(f"Invalid input: {e_n}. Please try again.")
            