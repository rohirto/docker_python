""" Classes Example Python """
import random
# Creating Classes and Objects
# Define a simple class
class Dog:
    """Dog class
    """
    def __init__(self, name, breed):
        """This is a Dunder method: Double underscore  methods
        This is not called by user, but by python when something is happening

        Args:
            name (_type_): _description_
            breed (_type_): _description_
        """
        self.name = name
        self.breed = breed

    def bark(self):
        """Bark method

        Returns:
            String: bark
        """
        return f"{self.name} is barking!"

# Create instances (objects) of the class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Milo", "Labrador")

# Access attributes and call methods of objects
print(dog1.name)
print(dog2.bark())

# Inheritance
# Define a base class (parent class)
class Animal:
    """Superclass
    """
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Superclass method
        """
        print("Grrr!")

# Define a derived class (child class) inheriting from Animal
class Doggo(Animal):
    """Sub class Doggo

    Args:
        Animal (class): Its super class
    """
    def speak(self):
        """Overriden method of superclass

        Returns:
            string: say woof!
        """
        return f"{self.name} says Woof!"

class Cat(Animal):
    """Subclass of Animal

    Args:
        Animal (class): Superclass
    """
    def speak(self):
        """Method of subclass, also demonstrates the super() inheritance from super class

        Returns:
            string: Meow
        """
        super().speak()
        return f"{self.name} says Meow!"

# Create objects of derived classes
dog = Doggo("Buddy")
cat = Cat("Whiskers")

# Call the overridden method
print(dog.speak())
print(cat.speak())


# Magic Methods  -> the one with 2 underscores __init__, also know as dunders,
# #used create functionalities no possible by normal methods
# common use of magic methods is operator overloading
# Operator overlaoding is used by objects to give functionalities to operators like ->
# like -> + - / * % < <= > >= == != etc
class Point:
    """Example class
    """
    def __init__(self, x_n, y_n):
        self.x_n = x_n
        self.y_n = y_n

    def __add__(self, other):
        """Operator Overload of add

        Args:
            other (Class): class type

        Raises:
            TypeError: If not same as Point class

        Returns:
            int: overloaded operator calculation
        """
        if isinstance(other, Point):
            return Point(self.x_n + other.x_n, self.y_n + other.y_n) # will do vector addition,
                                                                     #add corresponding attributes
                                                                     # of objects
        else:
            raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        """Subtract operator overloading

        Args:
            other (class): class type

        Raises:
            TypeError: if not the same class

        Returns:
            int: overloaded operation of sub
        """
        if isinstance(other, Point):
            return Point(self.x_n - other.x_n, self.y_n - other.y_n)  # will do vector subtraction,
                                                                      # add corresponding attributes
                                                                      # of object
        else:
            raise TypeError("Unsupported operand type")

point1 = Point(1, 2)
point2 = Point(3, 4)

result_add = point1 + point2  # Calls __add__ method
result_sub = point1 - point2  # Calls __sub__ method

print(f"Addition: ({result_add.x_n}, {result_add.y_n})")
print(f"Subtraction: ({result_sub.x_n}, {result_sub.y_n})")

# Some more magic operators
class SpecialString:
    """String class
    """
    def __init__(self,cont):
        self.cont = cont
    # Magic operator for greater than gt
    def __gt__(self,other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)
spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

# Some more magic operators

class VagueList:
    """Vague list uses random lib to generate output
    """
    def __init__(self,cont):
        self.cont = cont
    def __getitem__(self, index):
        return self.cont[index + random.randint(-1,1)]
    def __len__(self):
        return random.randint(0,len(self.cont)*2)

vague_list = VagueList(["A","B","C","D","E"])
print(len(vague_list))  #random shit
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
