def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int/float): The first number.
    b (int/float): The second number.

    Returns:
    int/fsloat: The sum of a and b.
    """
    return a + b
def subtract(a, b):
    """
    Returns the difference of two numbers.

    Parameters:
    a (int/float): The first number.
    b (int/float): The second number.

    Returns:
    int/float: The difference of a and b.
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of two numbers.

    Parameters:
    a (int/float): The first number.
    b (int/float): The second number.

    Returns:
    int/float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Returns the quotient of two numbers.

    Parameters:
    a (int/float): The first number.
    b (int/float): The second number.

    Returns:
    int/float: The quotient of a and b. Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

print(add(5, 3))        # Output: 8
print(subtract(5, 3))   # Output: 2
print(multiply(5, 3))   # Output: 15
print(divide(5, 3))     # Output: 1.6666666666666667

# To display the module documentation in the terminal, you can use the following code:
import pydoc
print(pydoc.render_doc('ca'))

