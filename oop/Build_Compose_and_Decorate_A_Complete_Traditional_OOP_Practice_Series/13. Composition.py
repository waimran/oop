# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.



# Composition ka matlab hai ek class ko dusri class ka object pass karna.

# Example: Car class mein Engine ka object pass karte hain, aur Car ke through Engine ki method ko access karte hain.


class Engine():
    def start(self):
        return "Engine started"

class Car():
    def __init__(self, engine):
        self.engine = engine  # Car class mein Engine ka object pass karte hain

    def start_car(self):
        return self.engine.start()  # Engine ki start method ko Car ke through call karte hain

# Engine ka object banaate hain
engine = Engine()

# Car ka object banaate hain aur Engine object pass karte hain
car = Car(engine)

# Car ke through Engine ka method call karte hain
print(car.start_car())  # Output: Engine started

