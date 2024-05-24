# python decorator allows to change the behavior of a function without modifying the function  itself
# and takes another function as parameter.

def function(function_1):
    def function_2(*args, **kwargs):
        print("start.......")
        result = function_1(*args, **kwargs)
        print(result)
        print("end........")
        return result

    return function_2()


def name(a):
    return a


def address(b):
    return b


x = name("Trishna")
y = address("ktm")
