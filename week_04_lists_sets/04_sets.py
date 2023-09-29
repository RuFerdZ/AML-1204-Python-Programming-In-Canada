# Author: Rusiru Fernando
# Sets are ordered collections of unique elements
# mutable
# duplicates are not allowed
# if there are duplicates in the list, they will be removed when converting to set

set_01 = {1, 2, 3, 4, 5}
print("set: ", set_01)
set_2 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print("duplicated value set: ", set_2)

# remove duplicates from list
list_01 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
set_03 = set(list_01)
print("set from list: ", set_03)

# list to set to back to list
list_02 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
list_03 = list(set(list_02))
print("list from set: ", list_03)

# Intersection of sets
set_04 = {1, 2, 3, 4, 5}
set_05 = {4, 5, 6, 7, 8}
print("intersection of sets: ", set_04.intersection(set_05))

# Union of sets
set_06 = {1, 2, 3, 4, 5}
set_07 = {4, 5, 6, 7, 8}
print("union of sets: ", set_06.union(set_07))

# Difference of sets
set_08 = {1, 2, 3, 4, 5}
set_09 = {4, 5, 6, 7, 8}
print("difference of sets 8-9: ", set_08.difference(set_09))
print("difference of sets 9-8: ", set_09.difference(set_08))

# Symmetric difference of sets
set_10 = {1, 2, 3, 4, 5}
set_11 = {4, 5, 6, 7, 8}
print("symmetric difference of sets: ", set_10.symmetric_difference(set_11))

# Add element to set
set_12 = {1, 2, 3, 4, 5}
set_12.add(6)
print("add element to set: ", set_12)

# Remove element from set
set_13 = {1, 2, 3, 4, 5}
set_13.remove(5)
print("remove element from set: ", set_13)

# Remove all elements from set
set_14 = {1, 2, 3, 4, 5}
set_14.clear()
print("remove all elements from set: ", set_14)

# Delete set
set_15 = {1, 2, 3, 4, 5}
del set_15
# print("delete set: ", set_15) # NameError: name 'set_15' is not defined

# Set operations
set_16 = {1, 2, 3, 4, 5}
set_17 = {4, 5, 6, 7, 8}
set_18 = {1, 2, 3, 4, 5}
set_19 = {4, 5, 6, 7, 8}
print("set_16 == set_17: ", set_16 == set_17)
print("set_16 == set_18: ", set_16 == set_18)
print("set_16 != set_17: ", set_16 != set_17)
print("set_16 != set_18: ", set_16 != set_18)
print("set_16 < set_17: ", set_16 < set_17)
print("set_16 < set_18: ", set_16 < set_18)
print("set_16 > set_17: ", set_16 > set_17)
print("set_16 > set_18: ", set_16 > set_18)
print("set_16 <= set_17: ", set_16 <= set_17)
print("set_16 <= set_18: ", set_16 <= set_18)
print("set_16 >= set_17: ", set_16 >= set_17)
print("set_16 >= set_18: ", set_16 >= set_18)

# Set membership
set_20 = {1, 2, 3, 4, 5}
print("1 in set_20: ", 1 in set_20)
print("6 in set_20: ", 6 in set_20)

# Set iteration
set_21 = {1, 2, 3, 4, 5}
for element in set_21:
    print(element)

# Set comprehension
set_22 = {element for element in range(1, 6)}
print("set comprehension: ", set_22)

# Set comprehension with condition
set_23 = {element for element in range(1, 6) if element % 2 == 0}
print("set comprehension with condition: ", set_23)

# Set comprehension with condition and if-else
set_24 = {element if element % 2 == 0 else element * 2 for element in range(1, 6)}
print("set comprehension with condition and if-else: ", set_24)

# Set comprehension with nested loop
set_25 = {element_01 + element_02 for element_01 in range(1, 6) for element_02 in range(1, 6)}
print("set comprehension with nested loop: ", set_25)

# Set comprehension with nested loop and condition
set_26 = {element_01 + element_02 for element_01 in range(1, 6) for element_02 in range(1, 6) if element_01 % 2 == 0}
print("set comprehension with nested loop and condition: ", set_26)

# Set comprehension with nested loop and condition and if-else
set_27 = {element_01 + element_02 if element_01 % 2 == 0 else element_01 * element_02 for element_01 in range(1, 6) for element_02 in range(1, 6)}
print("set comprehension with nested loop and condition and if-else: ", set_27)

# Set comprehension with nested loop and condition and if-else and if-else
set_28 = {element_01 + element_02 if element_01 % 2 == 0 else element_01 * element_02 if element_02 % 2 == 0 else element_01 - element_02 for element_01 in range(1, 6) for element_02 in range(1, 6)}
print("set comprehension with nested loop and condition and if-else and if-else: ", set_28)

# Set comprehension with nested loop and condition and if-else and if-else and if-else
set_29 = {element_01 + element_02 if element_01 % 2 == 0 else element_01 * element_02 if element_02 % 2 == 0 else element_01 - element_02 if element_01 > element_02 else element_01 + element_02 for element_01 in range(1, 6) for element_02 in range(1, 6)}
print("set comprehension with nested loop and condition and if-else and if-else and if-else: ", set_29)

