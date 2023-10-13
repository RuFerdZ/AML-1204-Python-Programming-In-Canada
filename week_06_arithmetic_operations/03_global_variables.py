my_number = 5
print(my_number)


def my_function(my_number):
    """
    Docstring
    This function adds 1 to the number passed to it
    :param my_number
    :return int
    :raises: TypeError
    """
    print(my_number)
    num = my_number + 1
    return num


print(my_number)
print(my_function(3))
