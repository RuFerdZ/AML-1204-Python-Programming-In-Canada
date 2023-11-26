# Author: Galgamuge Emmanuel Fernando
# Student ID: C0918066
# Date: 24/11/2023

from datetime import datetime, timedelta
import time
import calendar
print("=================================================================")

# 1: Use the datetime module to write a program that gets the current date and prints the day of the week
current_datetime = datetime.now()
day_of_week_int = current_datetime.weekday()
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_of_week_str = days_of_week[day_of_week_int]
print(f"Day of the week: {day_of_week_str}")
print("=================================================================")

# 2: Write a program that takes a birthday of user as input and prints the user’s age and the number of days, hours, minutes and seconds until their next birthday
birthday_str = input("Enter your birthday in the format YYYY-MM-DD: ")
birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
current_date = datetime.now()
age = current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))
current_date = datetime.now()
next_birthday = datetime(current_date.year, birthday.month, birthday.day)
if current_date > next_birthday:
    next_birthday = datetime(current_date.year + 1, birthday.month, birthday.day)
time_until_next_birthday = next_birthday - current_date
print(f"time until next birthday: {time_until_next_birthday}")
print("=================================================================")

# 3: Write a program that takes birthday of a person and calculates the total number of seconds they have been living in epoch time
epoch_time = time.time()
birthday_epoch = calendar.timegm(birthday.timetuple())
living_seconds = epoch_time - birthday_epoch
print(f"Number of seconds lived: {round(living_seconds, 2)}s")
print("=================================================================")

# 4: Write a Python program to print the date for yesterday, today, and tomorrow.
today = datetime.now().date()
print(f"yesterday: {today - timedelta(days=1)}")
print(f"today: {today}")
print(f"tomorrow: {today + timedelta(days=1)}")
print("=================================================================")
