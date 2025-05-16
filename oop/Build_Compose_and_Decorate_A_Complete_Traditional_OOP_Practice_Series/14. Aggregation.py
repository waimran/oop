# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.



# # # Aggregation ka Concept:
# # # Aggregation mein ek class doosri class ke object ka reference hold karti hai.

# # # Ye relationship independent hota hai, matlab agar Department object delete ho jaye, to Employee object apni jagah pe rahega.

# # # Ye has-a type ka relationship hota hai.



class Employee():
    def __init__(self,  name, position):
        self.name = name
        self.position = position
    
    def display(self):
        return f"{self.name} is a {self.position}"
    
class Department():
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Department object mein Employee ka reference store kar rahe hain

    def show_info(self):
        return f"Department: {self.dept_name}, Employee: {self.employee.display()}"
    

# Employee object banaate hain
employee1 = Employee("Ali", "Manager")

# Department object banaate hain aur Employee ka reference pass karte hain
dept1 = Department("HR", employee1)

# Department ke through Employee ka info access karte hain
print(dept1.show_info())  # Output: Department: HR, Employee: Ali is a Manager


