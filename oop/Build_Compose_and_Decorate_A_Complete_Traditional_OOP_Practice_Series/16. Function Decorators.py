# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().



# # Jab koi office ya mall mein gate par aata hai, pehle security check hota hai.

# # Uske baad wo andar enter karta hai.

# # Security check sab visitors ke liye extra step hai, bina visitor ka asli kaam (andar jaana) change kiye.

# # Visitor = Function (jaise say_hello())

# # Security Check = Decorator (jaise log_function_call)

# # Pehlay decorator ka kaam hoga (security check), phir original function chalega (andar jaana).



def  security_check(func):
    def wrapper():
        print("Security Check: Please scan your ID.")
        func()
    return wrapper



@security_check
def enter_mall():
    print("You have entered the mall.")

enter_mall()


