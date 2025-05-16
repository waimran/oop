# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.



# # # MRO ka Concept:
# # # MRO decide karta hai kaunsa method kis class se call hoga jab multiple inheritance hoti hai.

# # # Diamond Inheritance ek aisi situation hai jahan ek class do parent classes se inherit karti hai, jisme dono parent classes ek hi grandparent class se inherit karti hain.


class A():
    def show(self):
        print("Show method in A")

class B(A):
    def show(self):
        print("Show method in B")

class C(A):
     def show(self):
        print("Show method in C")

class D(B , C):
      pass


# D ka object banate hain

d = A()
d.show()

d1 = D()
d1.show()  # Output: Show method in B

d2 = B()
d2.show()

d3 = C()
d3.show()


# Class B aur Class C dono A se inherit karte hain aur apni show() method ko override karte hain.






# Extra Example 


class Animal:
    def sound(self):
        print("Animal makes sound")

class Mammal(Animal):
    def sound(self):
        print("Mammal makes sound")

class Bird(Animal):
    def sound(self):
        print("Bird makes sound")

class Bat(Mammal, Bird):
    pass

# Bat ka object banate hain
bat = Bat()
bat.sound()  # Output: Mammal makes sound



