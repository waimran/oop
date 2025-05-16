# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.




class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age is below 18, not eligible.")
    else:
        print("You are eligible!")

try:
    check_age(16)
except InvalidAgeError as e:
    print(f"Error: {e}")

