# course = "Python for Beginners"
# print(course[-2])
# print(course[0:3])
# print(course[0:])
# print(course[:0])
# print(course[:50])  # returns 0 to 4th index
# print(course[50])
# print(course[1:-1])
# print(len(course))

#place = "banke bageshwori campus nepalgunj banke"
# print(place.capitalize())  # capitalize first letter
# print(place.lower())
# print(place.count("e"))
# print(place.replace("b", "a"))
#print(f"{place.find('b')}")
# print(f"place.find{'t'})  # if not found it written -1

# txt = "Hello, welcome to my world."
# x = txt.endswith(".")
# print(x)
#
# x = "My name is Trishna"
# y = x.startswith("M")
# print(y)

# text = "50000"
# x = text.zfill(16)
# print(x)

# address = "Nepalgunj"
# print(address[::2])  # print every second character
# print(address[::-1])  # print every character in reverse

# strip, split, join
# stripe remove trailing whitespaces
# split returns a list
# join it concatenates string with another string
string_example = " Hello world"
print(string_example)
print(string_example.strip())
a = string_example.split()
print(a[0])
print(a[1])

jwt_token = "jhdjfhdfgygr.yhfdnskjkjfkd,jfjhdghgj"
b = jwt_token.split(".")
print(b[0])

place = "  dhakeri banke"
c = (place.strip())
d = "hello".join(c)
print(d)

e = place.split()
f = "hello".join(e)
print(f)
