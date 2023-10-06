# Functions
# SHOULD CONTAIN ONLY LOWER_CASE LETTERS IN camel_case: PEP 8
# f(x) = x ^ 2
# f(2) = 2 ^ 2 = 4

def f(x):
    return x * x


# calling a function means typing its name and passing a value
print(f(2))


# this function does not return anything: pass
def calculated_sum():
    pass


calculated_sum()

# ==========================================
# function with default value
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def clear_list(arg_list):
    # arg_list.clear()
    arg_list[0] = 10


# pass by reference
clear_list(my_list)
print(my_list)
# ==========================================

# pass by value
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def clear_list(arg_list):
    arg_list = []


clear_list(my_list)
print(my_list)
# ==========================================
x = 10


# pass by value
def change_num(y):
    y = 20


change_num(x)
print(x)


# ==========================================

# adding 2 numbers with unordered arguments
def add(x, y):
    return x + y


print(add(2, 3))
print(add(y=3, x=2))

# python supports multiple return values
# return x, y, z
# add(a, b):
#     return a + b, a - b, a * b
# x, y, z = add(2, 3)
# print(x, y, z)
