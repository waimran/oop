# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().


# abc module ka use karke abstract class banate hain.
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass
# @abstractmethod se batate hain ki ye method har child class ko banana padega.
class Rectangle(Shape):  # Child class
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Object bana kar use karo
rect = Rectangle(5, 3)
print(rect.area())  # Output: 15





# @abstractmethod ka kaam:
# Jab tum chahte ho har child class apna apna method banaye, tab @abstractmethod lagate ho.

# Ye force karta hai child class ko ke method likho warna error aayega.