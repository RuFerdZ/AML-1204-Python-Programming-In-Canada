# Author: Rusiru Fernando

# get range of elements from list
my_list_1 = [1, 2, 3, 4, 5]

# format: list_name[start_index:end_index] - end_index is not included
print(my_list_1[1:3])  # get elements from index 1 to 3 (not including 3)
print(my_list_1[1:])  # get elements from index 1 to end of list
print(my_list_1[:3])  # get elements from start of list to index 3 (not including 3)
print(my_list_1[:])  # get all elements from list

# with step size
print(my_list_1[::2])  # get elements from start of list to end of list with step size of 2
print(my_list_1[::-1])  # get elements from start of list to end of list with step size of -1 (i.e. reverse list)

# step from the 2nd element
print(my_list_1[1::2])  # get elements from index 1 to end of list with step size of 2
print(my_list_1[1::-1])  # get elements from index 1 to end of list with step size of -1 (i.e. reverse list)

# Note: the object type of the returned value is a "list" because we are getting a collection of objects

print(my_list_1[-4:-1])  # get elements from index -4 to -1 (not including -1)
print(my_list_1[-1:-4])  # this returns an empty list because the start index is greater than the end index
print(my_list_1[-1:-4:-1])  # this will return the range because the step is -1

# format: list_name[start_index:end_index:step_size]
print(my_list_1[1:5:2])  # get elements from index 1 to end of list with step size of 2

# when step size is negative, you are moving from right to left
# when step size is positive, you are moving from left to right
# Note: ":" means everything

print(my_list_1[-4:])  # get elements from index -4 to end of list
print(my_list_1[-4:-1])  # get elements from index -4 to -1 (not including -1)

# giving an end index of which is grater than the actual length of the list won't give an error
print(my_list_1[1:100])  # this will return all elements from index 1 to end of list
# giving a start index of which is grater than the actual length of the list will return an empty list
print(my_list_1[10:20])  # this will return an empty list
# negative indexing with out of ranges
print(my_list_1[-10:-1])  # this will return the list as above from reverse indexing

# reversing the list
print(my_list_1[::-1])
print(my_list_1[::-2])


