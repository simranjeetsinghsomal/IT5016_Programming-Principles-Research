# Divide two numbers, handle ZeroDivisionError
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    else:
        return result

# Test the divide_numbers function
num1 = 10
num2 = 0
result = divide_numbers(num1, num2)
if result is not None:
    print("Result of division:", result)
