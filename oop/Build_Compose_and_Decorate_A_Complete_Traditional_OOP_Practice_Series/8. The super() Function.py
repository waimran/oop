# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.



class Person():
    def __init__(self, name):
        self.name  = name


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.name = name
        self.subject = subject


Teacher1 = Teacher("Huma", "Math")
print(Teacher1.name)
print(Teacher1.subject)

Teacher2 = Teacher("Marium", "Science")
print(Teacher2.name)
print(Teacher2.subject)



