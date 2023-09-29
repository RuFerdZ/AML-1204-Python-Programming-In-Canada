# Author: Rusiru Fernando

# List
# DefinitionL List is a collection of objects
#  Properties:
#   1. List is ordered
#   2. List can contain duplicate values
#   3. List is mutable (i.e. can be changed)
# format: list_name = [element1, element2, element3, ...] - PEP8 recommends to use single quotes, space after comma
# Index of python list starts from 0

my_list_01 = [1, 2, 3, 4, 5]
print(my_list_01)
print(type(my_list_01))

# multi data type list
my_list_02 = [1, 2, 3, 4.5, True, 'a', 'b', 'c', 'd', 'e']
my_list_02.pop()
print(my_list_02)
my_list_02.pop(0)
print(my_list_02)

# list with duplicate values
my_list_03 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(my_list_03[0])
print(my_list_03.count(3))

# list with nested list - 2D list
my_list_04 = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5]]
print(len(my_list_04))
print(my_list_04[5][0])
my_list_04.append(10)
print(my_list_04)

# negative indexing in list - indexes from the end of the list
print(my_list_04[-1])
print(my_list_04[-2])
print(my_list_04[-2][0])
print(my_list_04[-2][-1])
print(my_list_04[5][-3])


# adding elements to list
my_list_05 = [1, 2, 3, 4, 5]
my_list_05.append(6)
print(my_list_05)

# remove elements from list
my_list_06 = [1, 2, 3, 4, 5]
my_list_06.pop()
print(my_list_06)
my_list_06.pop(2) # remove element at index 0
print(my_list_06)

# insert element at specific index
my_list_07 = [1, 2, 3, 4, 5]
my_list_07.insert(2, 10)  # insert 10 at index 2
print(my_list_07)

# remove element by value
my_list_08 = [1, 2, 3, 4, 5] # remove first occurrence of 3 from list (in the case where there is multiple occurrences of 3)
my_list_08.remove(3)
print(my_list_08)

# printing on an append statement - returns None
my_list_09 = [1, 2, 3, 4, 5]
print(my_list_09.append(6)) # append returns None
print(type(my_list_09.append(6))) # append returns 'NoneType'

# clear list
my_list_10 = [1, 2, 3, 4, 5]
my_list_10.clear()
print(my_list_10)



