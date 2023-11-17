# Calculator
def my_calculator(input_1: float, input_2: float, operation_type: list):

    if isinstance(operation_type, list):
        addition_result = None
        subtraction_result = None
        multiplication_result = None
        division_result = None
        for operation in operation_type:
            if operation == "+":
                addition_result = find_addition(input_1, input_2)
            elif operation == "-":
                subtraction_result = find_subtraction(input_1, input_2)
            elif operation == "*":
                multiplication_result = find_multiplication(input_1, input_2)
            elif operation == "/":
                division_result = find_division(input_1, input_2)
        # return multiple values: if one operator is not found, it will throw an error, unless initialized with default values
        return addition_result, subtraction_result, multiplication_result, division_result
    else:
        raise TypeError("operation_type should be a list")


def find_addition(x: float, y: float):
    return x + y


def find_subtraction(x: float, y: float):
    return x - y


def find_multiplication(x: float, y: float):
    return x * y


def find_division(x: float, y: float):
    return x / y


addition_result, subtraction_result, multiplication_result, division_result = my_calculator(20, 10, ["+"])
print("Addition result: ", addition_result)  # 30
print("Subtraction result: ", subtraction_result)  # None
print("Multiplication result: ", multiplication_result)  # None
print("Division result: ", division_result)  # None
print("---------------------------------------------")

addition_result, subtraction_resul, multiplication_result, division_result = my_calculator(20, 10, ["+", "-"])
print("Addition result: ", addition_result)  # 30
print("Subtraction result: ", subtraction_result)  # 10
print("Multiplication result: ", multiplication_result)  # None
print("Division result: ", division_result)  # None
print("---------------------------------------------")

addition_result, subtraction_result, multiplication_result, division_result = my_calculator(20, 10, ["+", "-", "*"])
print("Addition result: ", addition_result)  # 30
print("Subtraction result: ", subtraction_result)  # 10
print("Multiplication result: ", multiplication_result)  # 200
print("Division result: ", division_result)  # None
print("---------------------------------------------")

addition_result, subtraction_result, multiplication_result, division_result = my_calculator(20, 10, ["+", "-", "*", "/"])
print("Addition result: ", addition_result)  # 30
print("Subtraction result: ", subtraction_result)  # 10
print("Multiplication result: ", multiplication_result)  # 200
print("Division result: ", division_result)  # 2.0
print("---------------------------------------------")
