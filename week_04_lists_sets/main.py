# Author: Galgamuge Emmanuel Fernando
# Student ID: C0918066
# Date: 28/09/2023

# 3-4: Guest list - invite three people to dinner
guest_list = ["Yolimar", "Vihangi", "Chris"]
print("Hey " + guest_list[0] + ", I would like to invite you to dinner at my place.")
print("Hey " + guest_list[1] + ", I would like to invite you to dinner at my place.")
print("Hey " + guest_list[2] + ", I would like to invite you to dinner at my place.")

# 3-5: Changing guest list
# one of the guests can't make it to the dinner
print("Hey " + guest_list[1] + ", I'm sorry that you can't make it to have dinner at my place.")
# replace the guest with someone else
guest_list[1] = "Karthik"
# print the invitations again
print("Hey " + guest_list[0] + ", I would like to invite you to dinner at my place.")
print("Hey " + guest_list[1] + ", I would like to invite you to dinner at my place.")
print("Hey " + guest_list[2] + ", I would like to invite you to dinner at my place.")

# 3-6: More guests
# print that you found a bigger dinner table
print("Great news! I've just got a larger dinner table, which means we can welcome even more guests.")
# add three more guests to the list
guest_list.insert(0, "William")
guest_list.insert(2, "John")
guest_list.append("Samantha")
# print the invitations again
print("Hey " + guest_list[0] + ", I would like to invite you to dinner at my place.")
print("Hey " + guest_list[1] + ", I would like to invite you to dinner at my place.")
print("Hey " + guest_list[2] + ", I would like to invite you to dinner at my place.")
print("Hey " + guest_list[3] + ", I would like to invite you to dinner at my place.")
print("Hey " + guest_list[4] + ", I would like to invite you to dinner at my place.")
print("Hey " + guest_list[5] + ", I would like to invite you to dinner at my place.")

# 3-7: Shrinking guest list
# print that you can only invite two people to the dinner
print("Hey guys, I'm sorry to inform you that I can only invite two people for dinner as the new dinner table won't arrive in time.")
# remove the last 4 guests from the list so that 2 guests remains
print("Hey " + guest_list.pop() + ", I'm sorry that it won't be possible to have you over for dinner.* ")
print("Hey " + guest_list.pop() + ", I'm sorry that it won't be possible to have you over for dinner.* ")
print("Hey " + guest_list.pop() + ", I'm sorry that it won't be possible to have you over for dinner.* ")
print("Hey " + guest_list.pop() + ", I'm sorry that it won't be possible to have you over for dinner.* ")
# print the invitations again
print("Hey " + guest_list[0] + ", you're still invited for dinner.")
print("Hey " + guest_list[1] + ", you're still invited for dinner.")
# remove the last two guests from the list and print the list to make sure that it's empty
del guest_list[1]
del guest_list[0]
print(guest_list)

# 3-8: Seeing the world
# create a list 5 of places you'd like to visit
places_to_visit = ["Switzerland", "Paris", "Dubai", "Maldives", "Sri Lanka"]
print(places_to_visit)
# sort the list alphabetically
print(sorted(places_to_visit))
print(places_to_visit)
# sort the list in reverse alphabetical order
print(sorted(places_to_visit, reverse=True))
print(places_to_visit)
# reverse the order of the list
places_to_visit.reverse()
print(places_to_visit)
# reverse the order of the list again
places_to_visit.reverse()
print(places_to_visit)
# sort the list in alphabetical order
places_to_visit.sort()
print(places_to_visit)
# sort the list in reverse alphabetical order
places_to_visit.sort(reverse=True)
print(places_to_visit)

# 3-9: Dinner guests
# print the number of guests invited to the dinner
print("The number of guests invited to the dinner is " + str(len(guest_list)) + ".")

# 3-10: Every function
# create a list of food
food_list = ["pizza", "burger", "pasta", "sandwich", "hot dog"]
print(food_list)  # print the list
print(food_list[0])  # print the first item in the list
print(len(food_list))  # print the length of the list
print(food_list[-1])  # print the last item in the list
food_list.append("fries")  # add an item to the end of the list
print(food_list)
# add an item to the beginning of the list
food_list.insert(0, "fried rice")
print(food_list)
# add an item to the middle of the list
food_list.insert(3, "noodles")
print(food_list)
# sort the list alphabetically
print(sorted(food_list))
# sort the list in reverse alphabetical order
print(sorted(food_list, reverse=True))
# reverse the order of the list
food_list.reverse()
print(food_list)
# remove the last item from the list
food_list.pop()
print(food_list)
# count the number of times an item appears in the list
print(food_list.count("pasta"))
# remove an item from the list
food_list.remove("pasta")
print(food_list)
# remove an item from the list by index
del food_list[2]
print(food_list)
# remove all items from the list
food_list.clear()
print(food_list)

# Dictionary Practice
course_dict = {
    "Virtualization": "Linchen Wang",
    "Networking Foundations": "Albert Danison",
    "Introduction to DevOps Careers for Canadian Business": "Linchen Wang",
    "Database Design": "Linchen Wang",
    "Cloud Storage Fundamentals for Canadian Enterprises": "Karan Dhawan",
    "Python Programming In Canada": "Amir Samiezadeh",
    "Operating Systems Foundations": "Mike Aleshams"
}
print(course_dict)
# changing instructor name
course_dict["Database Design"] = "John Doe"
print(course_dict)