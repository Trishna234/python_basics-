# a function is a container with a few lones of code which performs a specific task
# function is a block of code which runs only when it is called.
# function is created when we have use same functionality multiple times.

def first_function():
    return "Hello"


result = first_function()
print(result)


def addition(num_1, num_2, num_3):  # num_1 and num_2 are parameters
    results = num_1 + num_2 + num_3
    return results


x = addition(4, 5, 10)  # calling function
print(x)
