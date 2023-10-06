# optional arguments
#   default values
# REQUIRED ARGUMENTS MUST BE BEFORE OPTIONAL ARGUMENTS
def add(x, y, z=0):
    return x + y + z


print(add(2, 3))
print(add(2, 3, 4))


# declaring variable data types in arguments
def add(x: int, y: int, z: int = 0) -> int:
    return x + y + z


def multiply(x: int, y: int, z: int = 0) -> {int, str}:
    return x + y + z, "Multiply"


a, b = multiply(2, 3, 4)
print(a, b)
print(multiply(2, 3, 4))
