# Author: Galgamuge Emmanuel Fernando
# Student ID: C0918066
# Date: 10/11/2023

import string

"""
1: Write a Python function that takes a string and calculates the length of a string and returns it.
Print the returned value.
"""


def find_length(my_string: str):
    # return the length of the string
    return len(my_string)


print("Length of the string: ", find_length("Hello World"))

'''
2: Write a Python function that takes a string and counts the number of characters (character 
frequency) in a string. For example, if we send 'google.com' to the function, it should return a 
dictionary like this {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
'''


def count_characters(my_string: str):
    # empty dictionary to store the character frequency
    my_dict = {}
    # loop each character in the string
    for character in my_string:
        # check if the character exists in the dictionary
        if character in my_dict:
            # if exists, increment the value by 1
            my_dict[character] += 1
        else:
            # if not exists, add the character to the dictionary and set the value to 1
            my_dict[character] = 1
    return my_dict


print("Character frequency: ", count_characters("www.google.com"))

"""
3: Create a string of your choice and apply a minimum of 8 of following methods to it and print the 
result.

https://docs.python.org/3.8/library/string.html
"""

my_string_01 = "Hello World"
my_string_02 = "1234.5"
print(f"'{my_string_01}' in uppercase: ", my_string_01.upper())                              # print in uppercase
print(f"'{my_string_01}' in lowercase: ", my_string_01.lower())                              # print in lowercase
print(f"'{my_string_01}' in capitalize: ", my_string_01.capitalize())                        # capitalize first letter
print(f"'{my_string_01}' without whitespaces: ", my_string_01.replace(" ", ""))  # print without whitespaces

print(f"'{my_string_02}' is a digit: ", my_string_02.isdigit())                              # check if the string is numeric only
print(f"'{my_string_02}' is a alpha: ", my_string_02.isalpha())                              # check if the string is alpha only
print(f"'{my_string_02}' is a alphanumeric: ", my_string_02.isalnum())                       # check if the string is a alphanumeric
print(f"'{my_string_02}' is a decimal: ", my_string_02.isdecimal())                          # check if the string is a decimal

# string functions
print(string.octdigits)        # print octal digits from 0 to 7
print(string.ascii_letters)    # print ascii letters from a to z and A to Z
print(string.ascii_lowercase)  # print ascii lowercase letters from a to z
print(string.ascii_uppercase)  # print ascii uppercase letters from A to Z
print(string.digits)           # print digits from 0 to 9
print(string.hexdigits)        # print hexadecimal digits from 0 to 9 and a to f
print(string.punctuation)      # print punctuation characters
print(string.printable)        # print all printable characters


'''
Write a Python function that converts temperatures from Fahrenheit to Celsius. 
Additional practices
It’s a good idea that you make yourself familiar with formatting strings in Python. 

Please check https://docs.python.org/3.8/library/string.html#format-examples and practice a few examples
'''


# this function converts fahrenheit to celsius
def convert_fahrenheit_to_celsius(fahrenheit: float):
    # formular: c = (f − 32) × 5/9
    # rounded to 2 decimal places
    return round(((fahrenheit - 32) * 5 / 9), 2)


print("Fahrenheit to Celsius: ", convert_fahrenheit_to_celsius(100), "\N{DEGREE SIGN}C")

