from function import first_function
# set store multiple items in single variables.
# set items are unordered, unchangeable and doesn't allow duplicate value
# my_set = {1, 2, 3, 4, 4, 5, 2, 3, 2, 1}
# print(my_set)
#
# this_set = {"apple", "banana", "cherry", True, 1, 2}  # True and 1 are constant
# print(this_set)
#
# this_set_1 = {"apple", "banana", "cherry", False, 0, 2}  # False and 0 are constant
# print(this_set_1)
#
# a = {"npj", "ktm"}
# a.add("btl")
# print(a)
#
# set_1 = {1, 2, 3, 4, 5, 6}
# set_2 = {1, 2, 3, 5, 6, 8}
# set_3 = set_1.union(set_2)
# set_4 = set_1.intersection(set_2)
# print(f"Union:{set_3}")
# print(f"intersection:{set_4}")

# Multiple set union
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"Ram", "Sita"}
# set4 = {"apple", "banana", "cherry"}
# myset = set1 | set2 | set3 | set4
# print(myset)
#
# # Multiple set intersection
# set_5 = {1, 2, 3, 4, }
# set_6 = {1, 2, 3, 4, 5, }
# set_7 = {4, 5}
# set_8 = set_5.intersection(set_6)
# set_9 = set_5.intersection(set_7)
# print(set_9)

set_10 = {"google", "apple"}
set_11 = {"apple", "microsoft"}
set_12 = set_10.difference(set_11)
print(set_12)

# python frozenset()
# A frozenset is an unindexed and unordered collection of unique elements.
# it is immutable. It is also called an immutable set
# Since the elements are fixed, unlike sets you cant remove elements
fruits = {"apple", "banana", "Cherry", "apple", "kiwi"}
basket = frozenset(fruits)
print("unique elements:", basket)

# add new fruits throws an error!
# basket.add("orange")
print("after adding new elements:", basket)

city = {"npj", "ktm", "btl"}
x = frozenset(city)
x1 = fruits.union(x)
x2 = fruits.intersection(x)
print(x2)
print(x1)


print(first_function())

