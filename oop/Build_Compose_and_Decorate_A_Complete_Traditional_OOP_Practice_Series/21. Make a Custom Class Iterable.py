# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.



class Countdown:
    def __init__(self, start):
        self.start = start  # Starting number set kar rahe hain

    def __iter__(self):
        self.current = self.start  # Current value set kar rahe hain
        return self  # Apne aapko return karte hain as iterator

    def __next__(self):
        if self.current >= 0:
            num = self.current
            self.current -= 1  # Har bar 1 kam karenge
            return num
        else:
            raise StopIteration  # Jab 0 se neeche chale jaye to loop khatam

# Object banate hain
countdown = Countdown(5)

# For loop se iterate karte hain
for number in countdown:
    print(number)




