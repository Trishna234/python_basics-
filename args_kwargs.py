def first_function(*args, **kwargs):
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(f"{key},{value}")


a = (1, 3, 4, 4)
b = {"name": "trishna", "address": "nepalgunj", "college":"abc"}
first_function(*a,**b)
