# python decorator allows to change the behavior of a function without modifying the function  itself
# and takes another function as parameter.

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("start..........")
        result = original_function(*args, **kwargs)
        print(result)
        print("End..........")
        return result

    return wrapper_function


@decorator_function
def name(a):
    return a


@decorator_function
def place(b):
    return b


x = name("Trishna")
print(x)
y = place("npj")
print(y)




