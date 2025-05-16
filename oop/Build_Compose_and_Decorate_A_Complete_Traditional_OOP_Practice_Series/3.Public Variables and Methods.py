# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.



class Car():
    def __init__(self, brand): 
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} car started!")        



Car1 = Car("Toyota")
print(Car1.brand)
Car1.start()



