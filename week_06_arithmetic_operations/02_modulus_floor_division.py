# Reverse number
def reverse_my_number(my_number):
    reverse_number = 0
    length = len(str(my_number))
    my_number = int(my_number)
    original_number = my_number
    for _ in range(length):
        digit = my_number % 10
        print("digit in iteration " + str(_) + " is: " + str(digit))
        reverse_number = reverse_number * 10 + digit
        print("reverse_number in iteration " + str(_) + " is: " + str(reverse_number))
        my_number //= 10
        print("my_number in iteration " + str(_) + " is: " + str(my_number))
        print("=========================================")
    # add zero at the end if the number has zero at the end
    reverse_number = ("0" if original_number % 10 == 0 else "") + str(reverse_number)
    return reverse_number


user_input = input("Enter a integer: ")
print("Reversed number is: " + str(reverse_my_number(user_input)))
