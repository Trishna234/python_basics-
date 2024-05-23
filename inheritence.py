class Person:
    def __init__(self, name, place):
        self.name = name
        self.place = place

    def info(self):
        return self.name, self.place


class Employee(Person):
    pass


a = Employee("abc", "ktm")
print(a.info())


class Dog:
    def eat(self):
        print("Dog is eating")


class Animal(Dog):
    def display(self):
        print("display")


a = Animal()
a.display()
a.eat()


class Cat:
    def eat(self):
        print("cat is eating")


class Dog:
    def walk(self):
        print("dog is walking")


class Animal(Cat, Dog):
    pass


a = Animal()
a.eat()
a.walk()


class Ram:
    def dance(self):
        print("Ram is dancing")


class Sita:
    def sing(self):
        print("Sita is singing")


class Person(Ram, Sita):
    pass


b = Person()
b.dance()
b.sing()
