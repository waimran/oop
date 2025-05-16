# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


# 1. Constructor = Jab object banta hai, __init__ chalta hai.

# 2. Destructor = Jab object destroy hota hai, __del__ chalta hai.

# 3. Tumhe dono mein print karwana hai message.


class Logger:
    def __init__(self):
        print("Logger object created.")  # Constructor ka kaam

    def __del__(self):
        print("Logger object destroyed.")  # Destructor ka kaam

# Object banate hain
log = Logger()

# Jab program khatam hoga ya manually del(log) karoge, destructor chalega
del log  # Force destroy