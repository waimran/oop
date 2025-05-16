# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.




# # # Class Decoration ka simple example ho sakta hai ek shop jisme decorator ek discount offer hai. Agar shop ko decorate kiya jaaye, to wo discount de sakta hai jo pehle available nahi tha.

# # # Example:
# # # Shop = Class

# # # Discount = Class Decorator

# # # Shop ko decorate karna = Shop ko discount offer add karna


def add_greeting(cls):
    # Class ko modify karte hain aur greet() method add karte hain
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Ab Person ka object banate hain aur greet method use karte hain
person = Person("Ali")
print(person.greet())  # Output: Hello from Decorator!
