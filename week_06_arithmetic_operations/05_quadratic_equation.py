# Write a function that finds the roots of a quadratic equation in the format of
#                               a*x^2 + b*x + c = 0.
# The formular to find the roots are:
#                       (-b + sqrt(d))/(2*a) and (-b - sqrt(d))/(2*a)
# where d = b^2 - 4*a*c

import math


# quadratic equation = (+b - sqrt(b^2 - 4*a*c) / 2*a) or
#                       (-b + sqrt(b^2 - 4*a*c) / 2*a)

def quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return "No real roots"
    elif d == 0:
        return (-b + math.sqrt(d)) / (2 * a)
    else:
        return (-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)


def find_root(a, b, c):
    # this doesn't have the validations as above
    x_1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x_2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x_1, x_2


# with 2 roots
print(quadratic_equation(1, 8, 4))
print(find_root(1, 8, 4))

# where no roots
print(quadratic_equation(1, 2, 3))
# print(find_root(1, 2, 3))

# with 1 root
print(quadratic_equation(1, 2, 1))
print(find_root(1, 2, 1))