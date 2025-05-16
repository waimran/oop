# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.



class Student():
    def __init__(self, name:str, marks:int):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"The Name of Student is : {self.name}")
        print(f"{self.name} got {self.marks} marks out of 500 in the test.")
        

StudentDetail1  = Student("Dua",500)
print(StudentDetail1.name)
print(StudentDetail1.marks)
StudentDetail1.display()


StudentDetail2  = Student("Misbah",500)
print(StudentDetail2.name)
print(StudentDetail2.marks)
StudentDetail2.display()


