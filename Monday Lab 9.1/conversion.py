def decimal_to_binary(n):
    """
    Converts a decimal number to its binary representation.

    Parameters:
    n (int): The decimal number to be converted.

    Returns:
    str: The binary representation of the input decimal number.
    """
    return bin(n)[2:]

def binary_to_decimal(b):
    """
    Converts a binary number to its decimal representation.

    Parameters:
    b (str): The binary number to be converted.

    Returns:
    int: The decimal representation of the input binary number.
    """
    return int(b, 2)

def decimal_to_hexadecimal(n):
    """
    Converts a decimal number to its hexadecimal representation.

    Parameters:
    n (int): The decimal number to be converted.

    Returns:
    str: The hexadecimal representation of the input decimal number.
    """
    return hex(n)[2:]

print(decimal_to_binary(10))        # Output: '1010'
print(binary_to_decimal('1010'))    # Output: 10
print(decimal_to_hexadecimal(255)) # Output: 'ff'
# To display the module documentation in the terminal, you can use the following code:
import pydoc
print(pydoc.render_doc('conversion'))
