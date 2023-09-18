""" Class and Static Methods and Properties """
# Class Methods
#  that are bound to the class and not the instance of the class
#  can be called on the class itself and on instances of the class.
# Class methods take the class as their first argument, typically named cls.

class MyClass:
    """Example Class
    """
    class_variable = 0  # class variable, attribute doesnot need init

    def __init__(self, value):
        self.instance_variable = value  # Instance variable comes at init

    @classmethod
    def increment_class_variable(cls):
        """Class method implementation example
        """
        cls.class_variable += 1

    def display_values(self):
        """display value
        """
        print(f"Class Variable: {self.class_variable}")
        print(f"Instance Variable: {self.instance_variable}")

# Create instances of MyClass
obj1 = MyClass(10)
obj2 = MyClass(20)

# Access and modify class variable using class method
MyClass.increment_class_variable()
obj1.increment_class_variable()

# Display values
obj1.display_values()  # Class Variable: 2, Instance Variable: 10
obj2.display_values()  # Class Variable: 2, Instance Variable: 20

## Static Methods
# bound to the class and do not have access to the class or instance state.
# used for utility functions that are related to the class
# but don't depend on instance-specific data.
# defined using the @staticmethod decorator.

class MathUtils:
    """Simple demo of static method, class for that

    Returns:
        _type_: _description_
    """
    @staticmethod
    def add(a_n, b_n):
        """static method to add

        Args:
            a_n (_type_): _description_
            b_n (_type_): _description_

        Returns:
            int: sum
        """
        return a_n + b_n

    @staticmethod
    def subtract(a_n, b_n):
        """static method to subtract

        Args:
            a_n (_type_): _description_
            b_n (_type_): _description_

        Returns:
            int: sub
        """
        return a_n - b_n

    @staticmethod
    def multiply(a_n, b_n):
        """static method to multiply

        Args:
            a_n (_type_): _description_
            b_n (_type_): _description_

        Returns:
            _type_: _description_
        """
        return a_n * b_n

# Use static methods without creating instances
RESULT1 = MathUtils.add(5, 3)
RESULT2 = MathUtils.subtract(10, 4)
RESULT3 = MathUtils.multiply(6, 2)

print(f"Addition: {RESULT1}")
print(f"Subtraction: {RESULT2}")
print(f"Multiplication: {RESULT3}")

# Properties
# properties are a way to control access to attributes of an object
# allow you to define getter, setter, and deleter methods for an attribute
# Properties are defined using the @property, @<attribute>.setter,
# and @<attribute>.deleter decorators.

# Basic property
class Circle:
    """Demo of Properties
    """
    def __init__(self, radius):
        self._radius = radius  # Private attribute with an underscore

    @property
    def radius(self):
        """return a private attribute, getter method

        Returns:
            int: radius which is private attribute
        """
        return self._radius

    @radius.setter
    def radius(self, value): # The name of attribute is used as a method
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Deleting the radius attribute")
        del self._radius

# Create an instance of the Circle class
circle = Circle(5)

# Access the radius property
print(circle.radius)  # Calls the getter method

# Modify the radius property
circle.radius = 7  # Calls the setter method

# Delete the radius property
del circle.radius  # Calls the deleter method

# Ex 2
class Temperature:
    """Demo of properties
    """
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """private attribute getter

        Returns:
            private attribute: _description_
        """
        return self._celsius

    @property
    def fahrenheit(self):
        """derive a new attribute from private attribute

        Returns:
            _type_: _description_
        """
        return (self._celsius * 9/5) + 32

# Create an instance of the Temperature class
temp = Temperature(25)

# Access the read-only properties
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")

# Ex 3
class Rectangle:
    """Demo class for properties
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        """Class takes input of just len and width, but this is a new attribute created

        Returns:
            new atrribute: area
        """
        return self.length * self.width

    @property
    def perimeter(self):
        """class just has 2 attributes len and width, this new atrribute is created
        This is a getter for it

        Returns:
            new attri: perimeter
        """
        return 2 * (self.length + self.width)

# Create an instance of the Rectangle class
rectangle = Rectangle(5, 3)

# Access the computed properties
print(f"Area: {rectangle.area}")
print(f"Perimeter: {rectangle.perimeter}")
