# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

# # Concept:
# # @property: Isse hum ek method ko attribute ke tarah access kar sakte hain, matlab wo method ek value return karega jaise ek normal variable.

# # @setter: Isse hum private attribute ko modify kar sakte hain jab wo @property ke through access kiya jaaye.

# # @deleter: Isse hum attribute ko delete kar sakte hain jab wo @property ke through access kiya jaaye.


# # # Daily Life Example:
# # # Product Price Example:

# # # Aapke paas ek product hai, jiska price hai.

# # # Price ko access karne, update karne aur delete karne ke liye aapko control chahiye.

# # # @property ka use price ko get karne ke liye, @setter ka use price ko update karne ke liye aur @deleter ka use price ko delete karne ke liye kiya jaata hai.
    



class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # private variable

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, new_price):
        print("Setting new price...")
        if new_price > 0:
            self._price = new_price
        else:
            print("Price must be positive.")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Product object banate hain
product = Product("Laptop", 1000)

# Get price using @property
print(product.price)  # Output: Getting price... 1000

# Set price using @setter
product.price = 1200  # Output: Setting new price...
print(product.price)  # Output: Getting price... 1200

# Try setting invalid price
product.price = -500  # Output: Price must be positive.

# Delete price using @deleter
del product.price  # Output: Deleting price...
