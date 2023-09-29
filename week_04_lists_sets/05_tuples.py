# Author: Rusiru Fernando
# Tuples: Collection of objects
# Properties:
#   ordered
#   immutable (i.e. cannot be changed) - cannot add, remove, update elements
#   can contain duplicate values
# format: tuple_name = (element1, element2, element3, ...) - PEP8 recommends to use single quotes, space after comma
# faster than lists

my_tuple_01 = (1, 2, 3, 4, 5)
print("tuple: ", my_tuple_01)

# multi data type tuple
my_tuple_02 = (1, 2, 3, 4.5, True, 'a', 'b', 'c', 'd', 'e')
print("multi-datatype tuple: ", my_tuple_02)

# tuple with duplicate values
my_tuple_03 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print("tuple with duplicate values: ", my_tuple_03)

# tuple with nested tuple - 2D tuple
my_tuple_04 = (1, 2, 3, 4, 5, (1, 2, 3, 4, 5))
print("tuple with nested tuple: ", my_tuple_04)

# negative indexing in tuple - indexes from the end of the tuple
print("negative indexing in tuple: ", my_tuple_01[-2])

#  count() method - returns the number of times a specified value occurs in a tuple
print("count() method: ", my_tuple_03.count(3))

# index() method - searches the tuple for a specified value and returns the position of where it was found
print("index() method: ", my_tuple_03.index(3))