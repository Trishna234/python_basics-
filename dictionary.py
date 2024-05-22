# dictionary add data in key, value, pairs,
# it is ordered, changeable and doesn't allow key duplicate
info = {
    "name": "Trishna",
    "age": 22,
    "address": "Nepalgunj",
    "is_verified": True,

}
print(info["name"])
print(info)
info["address"] = "ktm"  # change values of dictionary
print(info["address"])
print(info)
del info["is_verified"]
print(info)
info["gender"] = "male"  # add key in dictionary
print(info)
for a, b in info.items():
    print(f'"Key: {a}": value {b}')
# nested dictionary:
family = {
    "child1": {
        "name": "Ram",
        "age": 24,
        "address": "npj"
    },
    "child2": {
        "name": "sita",
        "age": 22,
        "address": "ktm"
    },
    "child3": {
        "name": "hari",
        "age": 25,
        "address": "npj"
    }
}
print(family["child2"]["name"])
print(family)
