""" Data hiding in Python """
# Python does not believe in encapsulation
# Python philosphy - we are all consenting adults
# discourages users from tinkering with implementation

# Define a class with encapsulation
class BankAccount:
    """Ex class
    """
    def __init__(self, account_number, balance):
        """init method

        Args:
            account_number (int): _description_
            balance (int): _description_
        """
        self._account_number = account_number  # Protected attribute, convention to discourage
        self.__balance = balance  # Private attribute, need special method to access

    def get_balance(self):
        """get the balance

        Returns:
            private attribute: balance double underscore -> private attribute
        """
        return self.__balance

    def deposit(self, amount):
        """deposit amount

        Args:
            amount (int): update private attribute balance 
        """
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        """withdraw amount

        Args:
            amount (int): update private attribute balance
        """
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

# Create an object and access attributes using methods
account = BankAccount("123456", 1000)
account.deposit(500)
account.withdraw(200)

print(f"Account Number: {account._account_number}")  # Accessing a protected attribute
print(f"Balance: {account.get_balance()}")  # Accessing a private attribute
print(f"Access to private attribute {account._BankAccount__balance}")
