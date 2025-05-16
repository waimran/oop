# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class Math:
    @staticmethod
    def add(a, b):
        return a + b

# Direct call without object
print(Math.add(3, 4))  # Output: 7


        

# Jab method na class variable use kare na object (self) use kare, tab @staticmethod lagate hain.

# Static method simple kaam karta hai — input lo aur result do, bina kisi object ya class ka data touch kiye.


# Real Time Example of @staticmethod:
# 🚗 Car Speed Converter
# Hum ek method banate hain jo km/h ko m/s mein convert kare — ismein car ka object ya class ka naam zarurat nahi.

class SpeedConverter:
    @staticmethod
    def kmph_to_mps(speed):
        return speed * 1000 / 3600

# Direct call without object
print(SpeedConverter.kmph_to_mps(72))  # Output: 20.0
# ➡️ Use: Jab sirf calculation karni ho, data save nahi karna.