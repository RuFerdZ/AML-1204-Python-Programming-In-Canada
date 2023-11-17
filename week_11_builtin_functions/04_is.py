# is
# is not

# is checks if two objects are the same object
# is not checks if two objects are not the same object
# is is used for comparison

# == checks if two objects have the same value
# != checks if two objects do not have the same value

# numbers are refereced by value

x = "Hello"

if x is "Hello":
    print("x is Hello")

if x is not "Hello":
    print("x is not Hello")


my_list_1 = [1, 1, 2, 3, 5, 8, 13]
my_list_2 = [1, 1, 2, 3, 5, 8, 13]

if my_list_1 is not my_list_2:
    print("my_list_1 is not my_list_2")

print(id(my_list_1))

my_list_1.append(my_list_2)
print(id(my_list_1))

my_list_3 = my_list_1
print(id(my_list_3))
(print(my_list_3 is my_list_1))
my_list_3.append(100)
print(id(my_list_3))
print(my_list_1)
print(my_list_3)


a = 5
b = 5
print(id(a))
print(id(b))
print(a is b)
# same for tuples since they are immutable
# same for strings since they are immutable

c = "Hi"
d = "Hi"
print(id(c))
print(id(d))
# this changes the address
c += " there"
print(id(c))
print(id(d))