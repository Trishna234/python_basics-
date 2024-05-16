a = 100
b = 100
if b > a:
    print("b is greater than a")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")

is_hot = True
is_cold = False
if is_hot and is_cold:
    print("Drink more Water and keep your body warm")
# elif is_cold:
#     print("keep your body warm")
else:
    print("it's a lovely day")

amount = 1000
is_good_credit = True
if is_good_credit:
    down_payment = amount * (10 / 100)
else:
    down_payment = amount * (20 / 100)
print(down_payment)

normal_speed = 60
bike_speed = 80
if normal_speed < bike_speed:
    print("chance of not having accident")
else:
    print("chance of having accident")

speed = 60
if speed > 60:
    print("chance of not having accident")
else:
    print("Chance of having accident")

speed = int(input("Enter the Speed"))
if speed < 60:
    print("Chance of being safe")
else:
    print("chance of having accident")

num = int(input("Enter the number"))
if num % 2 == 0:
    print("num is even")
else:
    print("num is odd")
