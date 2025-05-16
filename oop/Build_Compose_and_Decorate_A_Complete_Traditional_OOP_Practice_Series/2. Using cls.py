# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1  # jab bhi object banega, count +1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

# Object banate hain
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Count dikhate hain
Counter.show_count()






# Jab hum @classmethod likhte hain, iska matlab hota hai ye method class ke liye hai, object ke liye nahi.

# Is method ka pehla parameter cls hota hai (jaise self hota hai object ke liye).

# Is method se hum class variables ko access aur change kar sakte hain.




