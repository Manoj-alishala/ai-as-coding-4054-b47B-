#Problem Statement 1: AI-Assisted Bug Detection

# manual code
def factorial(n):
result = 1
for i in range(1, n):
    result = result * i
return result

# AI-assisted code
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120


Problem Statement 2: Task 2 — Improving Readability & Documentation

# manual code :
def calc(a, b, c):
    if c == "add":
        return a + b
    elif c == "sub":
        return a - b
    elif c == "mul":
        return a * b
    elif c == "div":


ai assisted code :
def calculate(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float: The result of the arithmetic operation.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'.")
    
# Example usage:
result = calculate(10, 5, 'add') # Output: 15
print(result)




#Problem Statement 3:  Enforcing Coding Standards 

# # manual code :
def Checkprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# # AI-assisted code :
def is_prime(number):
    """
    Check if a number is prime.

    Parameters:
    number (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage:
print(is_prime(11))  # Output: True



# Problem Statement 4: AI as a Code Reviewer in Real Projects 

#Task 4
'''def processData(d):
    return [x * 2 for x in d if x % 2 == 0]
print(multiply_even_numbers([1, 2, 3, 4]))          # [4, 8]
print(multiply_even_numbers([2, 6, 7], 3))          # [6, 18]
print(multiply_even_numbers([]))                    # []'''
#PEP8 Style Guide with complete code
def multiply_even_numbers(d):
    """
    Multiply even numbers in a list by 2.

    Args:
        d (list): A list of integers.
    Returns:
        list: A list containing the even numbers from the input list multiplied by 2.
    """
    return [x * 2 for x in d if x % 2 == 0]
print(multiply_even_numbers([1, 2, 3, 4]))          # [4, 8]
print(multiply_even_numbers([2, 6, 7]))          # [4, 12]
print(multiply_even_numbers([]))                    # []



#Task5
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total
numbers = range(1000000)
#Optimized High-Performance Code with numpy
import numpy as np
def sum_of_squares(numbers):
    """
    Calculate the sum of squares of a list of numbers.

    Args:
        numbers (iterable): An iterable of numerical values.
    Returns:
        float: The sum of squares of the input numbers.
    """
    return np.sum(np.square(numbers))
numbers = np.arange(1000000)
#Execution time comparision code
import time
# Original code execution time
start_time = time.time()
numbers = range(1000000)
print(sum_of_squares(numbers))
end_time = time.time()
print(f"Original code execution time: {end_time - start_time} seconds")
# Optimized code execution time
start_time = time.time()
numbers = np.arange(1000000)
print(sum_of_squares(numbers))
end_time = time.time()
print(f"Optimized code execution time: {end_time - start_time} seconds")
