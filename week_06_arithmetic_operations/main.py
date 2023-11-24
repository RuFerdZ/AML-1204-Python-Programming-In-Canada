# Author: Galgamuge Emmanuel Fernando
# Student ID: C0918066
# Date: 06/10/2023
# Notes: https://github.com/RuFerdZ/AML_1204_Python-Programming-In-Canada/tree/master/week_06_arithmetic_operations

# 5-1. Conditional Tests
print("=======================================================================")
# Predicting food
food = "pizza"
print("Is food == 'pizza'? I predict True.")
print(food == "pizza")
print("Is food == 'burger'? I predict False.")
print(food == "burger")
# Predicting car
car = "bmw"
print("\nIs car == 'bmw'? I predict True.")
print(car == "bmw")
print("Is car == 'audi'? I predict False.")
print(car == "audi")
# Predicting number
number = 10
print("\nIs number == 10? I predict True.")
print(number == 10)
print("Is number == 20? I predict False.")
print(number == 20)
# Predicting is_online
is_online = "True"
print("\nIs is_online == True? I predict True.")
print(is_online == "True")
print("Is is_online == False? I predict False.")
print(is_online == "False")
# Predicting marks
marks = 100.0
print("\nIs marks = 100.0? I predict True.")
print(marks == 100.0)
print("Is marks = 100.0? I predict False.")
print(marks == 200.0)

# 5-2. More Conditional Tests
print("=======================================================================")
# Test using equality operator
print("\nIs food == 'pizza'? I predict True.")
print(food == "pizza")
# Test using inequality operator
print("Is food == 'burger'? I predict False.")
print(food != "burger")
# Test using lower() method
print("\nIs car == 'BMW'? I predict True.")
print(car.lower() == "bmw")
# Test using greater or equal than operator
print("Is marks >= 80.0? I predict True.")
print(marks >= 80.0)
# Test using less than operator
print("Is marks = 80.0? I predict False.")
print(marks < 80.0)
# test using keyword: and
print("\nIs food == 'pizza' and car == 'bmw'? I predict True.")
print(food == "pizza" and car == "bmw")
# test using keyword: or
print("Is food == 'pizza' or car == 'bmw'? I predict True.")
print(food == "pizza" or car == "bmw")
# test using keyword: in
print("\nIs food in ['pizza', 'burger', 'hotdog']? I predict True.")
print(food in ["pizza", "burger", "hotdog"])
# test using keyword: not in
print("Is food not in ['pizza', 'burger', 'hotdog']? I predict False.")
print(food not in ["pizza", "burger", "hotdog"])

# 5-3. Alien Colors #1
print("=======================================================================")
alien_color = "green"  # change the color of the alien
if alien_color == "green":  # check if alien color is green
    print("You have earned 5 points.")

# 5-4. Alien Colors #2
alien_color = "red"  # change the color of the alien
if alien_color == "green":  # check if alien color is green
    print("You have earned 5 points.")
else:  # if alien color is not green
    print("You have earned 10 points.")

# 5-5. Alien Colors #3
print("=======================================================================")
alien_color = "yellow"  # change the color of the alien
if alien_color == "green":  # check if alien color is green
    print("You have earned 5 points.")
elif alien_color == "yellow":  # check if alien color is yellow
    print("You have earned 10 points.")
else:  # if alien color is not green or yellow
    print("You have earned 15 points.")

# 5-6. Stages of Life
print("=======================================================================")
age = 20  # age of the person
if age < 2:  # check if age is less than 2
    print("You are a baby.")
elif age < 4:  # check if age is less than 4
    print("You are a toddler.")
elif age < 13:  # check if age is less than 13
    print("You are a kid.")
elif age < 20:  # check if age is less than 20
    print("You are a teenager.")
elif age < 65:  # check if age is less than 65
    print("You are an adult.")
else:  # if age is greater than or equal to 65
    print("You are an elder.")

# 5-7. Favorite Fruit
print("=======================================================================")
favorite_fruits = ["apple", "orange", "banana", "grapes"]  # list of favorite fruits
if "apple" in favorite_fruits:  # check if apple is in favorite fruits
    print("You really like apples!")
if "orange" in favorite_fruits:  # check if orange is in favorite fruits
    print("You really like oranges!")
if "banana" in favorite_fruits:  # check if banana is in favorite fruits
    print("You really like bananas!")
if "grapes" in favorite_fruits:  # check if grapes is in favorite fruits
    print("You really like grapes!")
if "mango" in favorite_fruits:  # check if mango is in favorite fruits
    print("You really like mangoes!")

# 5-8. Hello Admin
print("=======================================================================")
usernames = ["admin", "Jaden", "Chris", "John", "Peter"]  # list of usernames
# loop through the list of usernames
for username in usernames:
    if username == "admin":  # check if username is admin
        print("Hello admin, would you like to see a status report?")
    else:  # if username is not admin
        print("Hello " + username + ", thank you for logging in again.")

# 5-9. No Users
print("=======================================================================")
usernames = []  # empty list
# check if list is empty
if usernames:
    # loop through the list of usernames
    for username in usernames:
        if username == "admin":  # check if username is admin
            print("Hello admin, would you like to see a status report?")
        else:  # if username is not admin
            print("Hello " + username + ", thank you for logging in again.")
else:
    print("We need to find some users!")

# 5-10. Checking Usernames
print("=======================================================================")
current_users = ["admin", "Jaden", "Chris", "John", "Peter"]  # list of current users
new_users = ["admin", "Jaden", "Chris", "John", "Peter", "Mike", "Sam", "Bob"]  # list of new users
# loop through the list of new users
for new_user in new_users:
    if new_user in current_users:  # check if new user is already in current users
        print("Sorry! Username, " + new_user + ", is already taken.")
    else:  # if new user is not in current users
        print("Great! Username, " + new_user + ", is still available.")

# 5-11. Ordinal Numbers
print("=======================================================================")
numbers = list(range(1, 10))  # create a list of numbers from 1 to 9
# loop through the list of numbers
for number in numbers:
    if number == 1:  # 1st
        print(str(number) + "st")
    elif number == 2:  # 2nd
        print(str(number) + "nd")
    elif number == 3:  # 3rd
        print(str(number) + "rd")
    else:  # nth
        print(str(number) + "th")
