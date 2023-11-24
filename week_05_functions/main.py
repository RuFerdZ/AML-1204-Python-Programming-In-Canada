# Author: Galgamuge Emmanuel Fernando
# Student ID: C0918066
# Date: 06/10/2023

# 4-1: Pizzas
# create a list of pizzas
pizzas = ["Pepperoni", "Cheese", "BBQ"]
# print the list using a for loop
for pizza in pizzas:
    print(pizza)
# print the list using a for loop and a sentence
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
# print a sentence that includes the name of the pizza
print("I really love pizza!")

# 4-2: Animals
# create a list of animals
animals = ["Cat", "Dog", "Parrot"]
# print the list using a for loop
for animal in animals:
    print(animal)
# print the list using a for loop and a sentence
for animal in animals:
    print("A " + animal + " would make a great pet.")
# print a sentence that includes the name of the animal
print("Any of these animals would make a great pet!")

# 4-3: Counting to twenty
# use a for loop to print the numbers from 1 to 20
for number in range(1, 21):
    print(number)

# 4-4: One million
# create a list of numbers from 1 to 1,000,000
numbers = list(range(1, 1000001))
# print the list using a for loop
# for number in numbers:
#     print(number)

# 4-5: Summing a million
# print the minimum, maximum and sum of the list
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6: Odd numbers
# use the third argument of the range() function to make a list of odd numbers from 1 to 20
odd_numbers = list(range(1, 21, 2))
# print the list using a for loop
for odd_number in odd_numbers:
    print(odd_number)

# 4-13: Buffet
# create a tuple of 5 basic foods
foods = ("Rice", "Chicken", "Beef", "Pork", "Fish")
# print the tuple using a for loop
for food in foods:
    print(food)
# try to modify one of the items and make sure that Python rejects the change
# foods[0] = "Noodles"
# create a new tuple with the same items as the original
foods = ("Noodles", "Chicken", "Beef", "Mutton", "Fish")
# print the new tuple using a for loop
for food in foods:
    print(food)

# 8-3: T-Shirt
# write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt
def make_shirt(size, text):
    print("The size of the shirt is " + size + " and the text is " + text + ".")
# call the function with positional arguments
make_shirt("Large", "Hello World!")
# call the function with keyword arguments
make_shirt(size="Medium", text="Good Morning!")

# 8-4: Large shirts
# modify the make_shirt() function so that shirts are large by default with a message that reads I love Python
def make_shirt(size="Large", text="I love Python"):
    print("The size of the shirt is " + size + " and the text is " + text + ".")
# make a large shirt and a medium shirt with the default message
make_shirt()
make_shirt(size="Medium")

# 8-5: Cities
# write a function called describe_city() that accepts the name of a city and its country
def describe_city(city, country="Sri Lanka"):
    print(city + " is in " + country + ".")
# call the function with positional arguments
describe_city("Colombo")
describe_city(city="Kandy")
describe_city(city="Toronto", country="Canada")

# 8-6: City names
# write a function called city_country() that accepts the name of a city and its country
def city_country(city, country):
    print(city + ", " + country)
# call the function with positional arguments
city_country('"Colombo', 'Sri Lanka"')
city_country('"Kandy', 'Sri Lanka"')
city_country('"Toronto', 'Canada"')

# 8-7: Album
# write a function called make_album() that builds a dictionary describing a music album
def make_album(artist_name, album_title, number_of_songs = None):
    album = {"artist_name": artist_name, "album_title": album_title}
    if number_of_songs:
        album["number_of_tracks"] = number_of_songs
    return album
# call the function with positional arguments
print(make_album("Eminem", "Kamikaze"))
print(make_album("Eminem", "Kamikaze", 13))

# 8-8: User albums
# write a while loop that allows users to enter an album's artist and title
while True:
    print("\nPlease enter the album's artist and title:")
    print("(enter 'q' at any time to quit)")
    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break
    album_title = input("Album title: ")
    if album_title == 'q':
        break
    print(make_album(artist_name, album_title))



