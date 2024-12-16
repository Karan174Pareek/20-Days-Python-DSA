# Built-in module example
import math

# Using math module
print(math.sqrt(16))  # Output: 4.0
print(math.factorial(5))  # Output: 120


# Function call example
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8


# Custom function example
def greet(name):
    return f"Hello, {name}!"

print(greet("Karan"))  # Output: Hello, Karan!


# Importing a custom module
import my_module

# Using functions from my_module
result = my_module.multiply(4, 5)
print(result)  # Output: 20

result_division = my_module.divide(10, 2)
print(result_division)  # Output: 5.0

result_division_by_zero = my_module.divide(10, 0)
print(result_division_by_zero)  # Output: Division by zero is not allowed!
