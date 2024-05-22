# if the variable is outside the class it is called global variable

class Person:
    raise_amount = 1.5

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def get_name(self):
        return self.name

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay


p_1 = Person(name="ram", pay=1000)
print(p_1.name)
print(p_1.pay)
p_1.apply_raise()
print(p_1.pay)

