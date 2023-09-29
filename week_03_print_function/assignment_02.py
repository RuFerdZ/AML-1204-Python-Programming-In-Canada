# Author: Rusiru Fernando

# Task 2-1: Printing a message that has been assigned to a variable
message_01 = "Welcome to week 03 assignment."
print(message_01)

# Task 2-2: Printing a message that has been assigned to a variable and changing the value of the variable and print the new message
message_02 = "This is message number 02."
print(message_02)
message_02 = "This is modified message number 02."
print(message_02)

# Task 2-3: Printing a personal message to a person
person_name_01 = "John"
print("Hello " + person_name_01 + ", how are you doing?")

# Task 2-4: Printing a person's name in lower case, upper case, and title case
person_name_02 = "michael"
print(person_name_02.lower())
print(person_name_02.upper())
print(person_name_02.title())

# Task 2-5: Printing a quote and the name of the author
print(
    'Robert Mugabe once said, "Treat every part of your towel nicely because the part that wipes your buttocks today will wipe your face tomorrow"')

# Task 2-6: Printing a quote and the name of the author using variables
famous_person_01 = "Robert Mugabe"
quote = famous_person_01 + ' once said, "Treat every part of your towel nicely because the part that wipes your buttocks today will wipe your face tomorrow"'
print(quote)

# Task 2-7: Printing a quote and the name of the author using variables and adding white space characters and then with lstrip(), rstrip(), and strip()
person_name_03 = "\tJohn Doe\n"
print(person_name_03)
print(person_name_03.lstrip())  # lstrip() removes the white space characters from the left side of the string
print(person_name_03.rstrip())  # rstrip() removes the white space characters from the right side of the string
print(person_name_03.strip())  # strip() removes the white space characters from both sides of the string

# Task 2-8: Print the result of adding, subtracting, multiplying, and dividing two numbers having 8 as the result always
print(3 + 5)
print(16 - 8)
print(2 * 4)
print(int(32 / 4))

# Task 2-9: Print favorite number, assigned to a variable, in a message
favorite_number = 1
message_03 = "My favorite number is " + str(favorite_number) + "."
print(message_03)
