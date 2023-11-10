# Iteration
# We need to have an iterable object -> list, tuple, set, dictionary, string

# Iteration in python can be done in two ways:
# 1. for loop
#     we need to define a range of values to iterate
#     this loop is preferred as while loops can run forever if the conditions are not met
# 2. while loop
#     we need to define a condition to iterate
#     conditions are in the same format is as of conditionals

# fibonacci list between 1 to 20
my_list_1 = [1, 1, 2, 3, 5, 8, 13]
for _ in my_list_1:
    print(_, end=", ")

print()
# loop using while loop: my_list_1 = [1, 1, 2, 3, 5, 8, 13]
i = 0
while i < len(my_list_1):
    print(my_list_1[i], end=", ")
    i += 1


# continue: skip the current iteration and continue with the next iteration
# break: stop the loop
# pass: do nothing

# TODO: print all even numbers between 1 to 20 using for loop






# if we using something like flask to create a API, do we need to create a UI as well?
# do we need to use docker?
# do we need to implement gitlab runners?