# a function is a container with a few lones of code which performs a specific task
# function is a block of code which runs only when it is called.
# function is created when we have use same functionality multiple times.

# def first_function():
#     return "Hello"
#
#
# result = first_function()
# print(result)
#
#
# def addition(num_1, num_2, num_3):  # num_1 and num_2 are parameters
#     results = num_1 + num_2 + num_3
#     return results
#
#
# x = addition(4, 5, 10)  # calling function
# print(x)

def number(num1, num2):
    results = num1 + num2
    results1 = num1 - num2
    results3 = num1 / num2
    results4 = num1 * num2
    return results, results1, results3, results4


# a, b, c, d = number(10, 5) # positional arguments
# Unpacking
a, b, c, d = number(num2=10, num1=5)  # keyword arguments
print(a)





