# Classes in  python are used for creating objects that bundle.
# data(attributes) and methods (functions)together.
# They serve as blueprints for creating isinstances, which are individual objects with their own unique attributes and behavior.
# Self
# The word self is used to represent the instance of  a class.
# by using the "self" keyword use access the attributes and method of the class in python

# **init** method
# "**init**" is a reserved method in python class.
# it is called as constructor and this method is called when an object is created from class and it allows the class to initialize the attributes of the class.

class Employee:
    def __init__(self, first, last, email, address):
        self.first = first
        self.last = last
        self.email = email
        self.address = address

    def fullname(self):
        return self.first, self.last

    def em_email(self):
        return self.email

    def abc(self):
        return self.fullname()


emp_1 = Employee(first="ram", last="bbb", email="ram@gmail.com", address="npj")
print(emp_1.fullname())
print(emp_1.em_email())
print(emp_1.abc())
emp_2 = Employee(first="aaa",last="mmm", email="aaa@gmail.com",address="ktm")
print(emp_2.abc())
print(emp_2.em_email())
