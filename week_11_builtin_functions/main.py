# Author: Galgamuge Emmanuel Fernando
# Student ID: C0918066
# Date: 17/11/2023

print("===== Question 1: Print First 10 natural numbers using while loop")
i = 0
while i < 10:
    print(i)
    i += 1
print()

print("===== Question 2: Print the following pattern.")
rows = int(input("Enter number of rows: "))
for x in range(rows + 1):
    for y in range(x):
        print(y + 1, end=" ")
    print()
print()

print("===== Question 3: Accept number from user and calculate the sum of all number between 1 and given number.")
number = int(input("Enter number to find sum: "))
sum = 0
for _ in range(number + 1):
    sum += _
print("Sum of numbers from 1 to", number, "=", sum)
print()

print("===== Question 4: Print multiplication table of given number")
number = int(input("Enter number to find the multiplication table: "))
for _ in range(1, 11):
    print(number, "x", _, "=", number * _)
print()

print("===== Question 5: Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration")
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
print("Given list:", list1)
for _ in list1:
    if _ > 150:
        break
    if _ % 5 == 0:
        print(_)
print()

print("===== Question 6: Given a number count the total number of digits in a number")
number = int(input("Enter number to find the number of digits: "))
print("Length of the number:", len(str(number)))
print()

print("===== Question 7: Print the following pattern using for loop")
rows = int(input("Enter number of rows: "))
for x in range(rows, 0, -1):
    for y in range(x, 0, -1):
        print(y, end=" ")
    print()
print()

print("===== Question 8: Reverse the following list using for loop")
list2 = [10, 20, 30, 40, 50]
print("Given list:", list2)
for _ in range(len(list2) - 1, -1, -1):
    print(list2[_])
print()

print("===== Question 9: Display a message “Done” after successful execution of for loop")
loop = int(input("Enter number of times to loop: "))
for _ in range(loop):
    print(_)
print("Done!")
print()

print("===== Question 10: Display Fibonacci series up to 10 terms.")
a = 0
b = 1
print("Fibonacci Sequence:", b, end=" ")
for _ in range(8):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
print()
print()

print("===== Question 11: Write a loop to find the factorial of any number")
number = int(input("Enter number to find factorial: "))
factorial = 1
for _ in range(1, number + 1):
    factorial *= _
print(factorial)
print()

print("===== Question 12: Python program to display all the prime numbers within a range")
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
for _ in range(start, end + 1):
    if _ > 1:
        for i in range(2, _):
            if _ % i == 0:
                break
        else:
            print(_)
print()
