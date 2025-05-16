# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee():
    def __init__(self, name, _salary , __ssn):
        self.name = name
        self._salary = _salary
        self.__ssn = __ssn


Employee1 = Employee("Mahab",202,363)  
print(Employee1.name)
print(Employee1._salary)
print(Employee1._Employee__ssn)  # best practice nahi hai private variable ko access karna, lekin agar zarurat ho toh aise kar sakte hain.

# print(Employee1.salary) # ye nahi chalega kyunki ye protected hai.
# print(Employee1.ssn) # ye nahi chalega kyunki ye private hai.


