print("Hello World!!!")

my_variable = "1."

print(float(my_variable))       # 1.0
print(int(my_variable))         # ValueError: invalid literal for int() with base 10: '1.0'
print(int(float(my_variable)))  # 1

