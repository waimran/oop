# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.



# # # Concept:
# # # callable(): Ye function check karta hai agar kisi object ko function ki tarah call kiya jaa sakta hai. Agar object mein __call__() method defined hai to wo callable hota hai.

# # # __call__(): Ye special method hai jo object ko function ki tarah call karne ki permission deta hai. Jab object ko function ki tarah call kiya jaata hai, to __call__() method execute hota hai.

# # # Daily Life Example:
# # # Multiplier Example:

# # # Socho tumhare paas ek Multiplier machine hai jo tumhe kisi number ko ek factor se multiply karke result deti hai.

# # # Tum is machine ko function ki tarah use karte ho, matlab tum machine ko call karte ho aur wo tumhare input ko multiply kar ke result de deti hai.

# # # Yahan __call__() method ko define karte hain jo machine ko call karne ka kaam karega.




class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # factor jo input ko multiply karega

    def __call__(self, number):
        return number * self.factor  # number ko factor se multiply karna

# Multiplier object banate hain
multiply_by_3 = Multiplier(3)

# Test karte hain callable() ke saath
print(callable(multiply_by_3))  # Output: True (object ko function ki tarah call kar sakte hain)

# Ab is object ko function ki tarah call karte hain
result = multiply_by_3(10)  # Output: 30
print(result)





# # # Concept	Explanation
# # # __call__()	Object ko function ki tarah call karne ka method.
# # # callable()	Check karta hai ki object ko function ki tarah call kiya jaa sakta hai.