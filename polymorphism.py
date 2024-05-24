# The literal meaning of polymorphism is the condition of occurrence in different forms.


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"my name is{self.name}.i am {self.age} years old")

    def sound(self):
        print("bark")


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"my name is {self.name}.i am {self.age} years old")

    def sound(self):
        print("meow")


dog1 = Dog(name="abc", age=3)
cat1 = Cat(name="aaa", age=4)

for animal in (dog1, cat1):
    animal.info()
    animal.sound()


class Nepal:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def info(self):
        print(f"my country name is {self.name}.language speak here is {self.language}")

    def lang_1(self):
        print("Nepali")


class India:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def info(self):
        print(f"my country name is {self.name}.language speak here is{self.language}")

    def lang_1(self):
        print("hindi")


Nepali_1 = Nepal(name="Nepal", language="Nepali")
Indian_1 = India(name="India", language="Hindi")

for country in (Nepali_1,Indian_1):
    country.info()
    country.lang_1()
