# is
# is not

# is checks if two objects are the same object
# is not checks if two objects are not the same object
# is is used for comparison

# == checks if two objects have the same value
# != checks if two objects do not have the same value

x = "Hello"

if x is "Hello":
    print("x is Hello")

if x is not "Hello":
    print("x is not Hello")


my_list_1 = [1, 1, 2, 3, 5, 8, 13]
print(id(my_list_1))