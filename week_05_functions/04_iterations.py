# for loop
# The variable that is to be looped should be iterable
# objects: list, tuple, set, dictionary, string


my_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

for i in my_list:
    print(i, end=", ")

print()

# range(start, stop, step)
for i in range(3, 10):
    print(i, end=", ")

# with step
print()
for i in range(3, 10, 2):
    print(i, end=", ")

# print key and value of dictionary
print()

my_dict = {"name": "John", "age": 36, "country": "Norway"}

for key, value in my_dict.items():
    print(key, value)
