my_string_1 = "Hello World"  # json should be double quotes
my_string_2 = 'Hello World'

print(type(my_string_1))  # <class 'str'>
print(type(my_string_2))  # <class 'str'>

print(len(my_string_1))  # 11
print(len(my_string_2))  # 11

# print using for loop
for _ in my_string_1:
    print(_, end=", ")  # H, e, l, l, o,  , W, o, r, l, d,

print()

# print using while loop
i = 0
while i < len(my_string_1):
    print(my_string_1[i], end=", ")  # H, e, l, l, o,  , W, o, r, l, d,
    i += 1

print()

