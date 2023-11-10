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

my_string_3 = "this\tis a string"
print(my_string_3)  # this     is a string

# \ escape character
# \t tab
# \n new line
# \b backspace
# \' single quote
# \" double quote
# \\ backslash

my_string_4 = "this\bis a string"
print(my_string_4)  # "thiis a string"

my_string_5 = "this is a \"string\""
print(my_string_5)  # this is a "string"


# exists in string
# function: in
if "i" in my_string_4:
    print("\"i\" exists in my_string_4")

# not exists in string
# function: not in
if "z" not in my_string_4:
    print("\"z\" does not exist in my_string_4")