#Problem 1:
#Consider the following Python function:
def find_max(numbers):
    return max(numbers)
print(find_max([3, 1, 4, 1, 5, 9]))

def find_max(numbers):
    """
    This function takes a list of numbers as input and returns the maximum value from the list.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    int/float: The maximum value from the input list.
    """
    return max(numbers)

# (b) Inline comments
def find_max(numbers):
    # Use the built-in max function to find the maximum value in the list
    return max(numbers)

# (c) Google-style documentation
def find_max(numbers):
    """
    Finds the maximum value in a list of numbers.

    Args:
        numbers (list): A list of numerical values.
    Returns:
        int/float: The maximum value from the input list.
    """
    return max(numbers)

# Comparison of documentation styles:
# (a) Docstring:
# Advantages:
# - Provides a clear and structured way to document the function.
# - Can be easily accessed using the help() function in Python.
# Disadvantages:
# - May be overlooked by developers who are not familiar with the format.
# Suitable use cases:
# - Ideal for documenting functions, classes, and modules in Python.
# (b) Inline comments:
# Advantages:
# - Provides immediate context and explanations for specific lines of code.
# Disadvantages:
# - Can clutter the code if overused, making it harder to read.
# Suitable use cases:
# - Best for explaining complex logic or specific implementation details within the code.
# (c) Google-style documentation:
# Advantages:
# - Provides a clear and consistent format for documenting code, making it easier to read and understand
# Disadvantages:
# - May require more effort to maintain and update compared to inline comments.
# Suitable use cases:
# - Ideal for larger projects or libraries where consistent documentation is crucial for maintainability.
# Recommendation:
# For a mathematical utilities library, the Google-style documentation is most effective. This is because it provides a consistent and readable format that is widely recognized and supported by tools like Sphinx, making it easier for developers to understand and maintain the library.


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Problem 2: Consider the following Python function:
def login(user, password, credentials):
    return credentials.get(user) == password

# 1. Documentation in all three formats:
# (a) Docstring
def login(user, password, credentials):
    """
    This function checks if the provided user credentials are valid.

    Parameters:
    user (str): The username to be authenticated.
    password (str): The password to be authenticated.
    credentials (dict): A dictionary containing valid username-password pairs.

    Returns:
    bool: True if the credentials are valid, False otherwise.
    """
    return credentials.get(user) == password
# (b) Inline comments
def login(user, password, credentials):
    # Check if the provided user exists in the credentials dictionary and if the password matches
    return credentials.get(user) == password
# (c) Google-style documentation
def login(user, password, credentials):
    """
    Authenticates a user based on provided credentials.

    Args:
        user (str): The username to be authenticated.
        password (str): The password to be authenticated.
        credentials (dict): A dictionary containing valid username-password pairs.

    Returns:
        bool: True if the credentials are valid, False otherwise.
    """
    return credentials.get(user) == password

# 2. Comparison of documentation styles:
# (a) Docstring:
# Advantages:
# - Provides a clear and structured way to document the function.
# - Can be easily accessed using the help() function in Python.
# Disadvantages:
# - May be overlooked by developers who are not familiar with the format.
# Suitable use cases:
# - Ideal for documenting functions, classes, and modules in Python.
# (b) Inline comments:
# Advantages:
# - Provides immediate context and explanations for specific lines of code.
# Disadvantages:
# - Can clutter the code if overused, making it harder to read.
# Suitable use cases:
# - Best for explaining complex logic or specific implementation details within the code.
# (c) Google-style documentation:
# Advantages:
# - Provides a clear and consistent format for documenting code, making it easier to read and understand.
# Disadvantages:
# - May require more effort to maintain and update compared to inline comments.
# Suitable use cases:
# - Ideal for larger projects or libraries where consistent documentation is crucial for maintainability.
# 3. Recommendation:
# For new developers onboarding a project, the Google-style documentation would be most helpful. This is
# because it provides a clear and consistent format that is widely recognized and supported by tools like Sphinx, making it easier for new developers to understand the function's purpose, parameters, and return values. Additionally, the structured format can help new developers quickly grasp the functionality of the code without needing to read through inline comments or decipher less formal docstrings.


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Problem 3: Calculator (Automatic Documentation Generation)
# Task: Design a Python module named calculator.py and
# demonstrate automatic documentation generation.

# calculator.py
def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int/float): The first number.
    b (int/float): The second number.

    Returns:
    int/float: The sum of a and b.
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
print(pydoc.render_doc('calculator.py'))
# To generate and export the module documentation in HTML format, you can run the following command in the terminal:
# pydoc -w calculator
# This will create a file named calculator.html in the current directory. You can open this file in a web browser to verify the output. 



# Problem 4: Conversion Utilities Module

# conversion.py
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
print(pydoc.render_doc('conversion.py'))
# To generate and export the module documentation in HTML format, you can run the following command in the terminal:
# pydoc -w conversion
# This will create a file named conversion.html in the current directory. You can open this file in a web browser to verify the output. 


# Problem 5 – Course Management Module
# Task:
# 1. Create a module course.py with functions:
# o add_course(course_id, name, credits)
# o remove_course(course_id)
# o get_course(course_id)
# 2. Add docstrings with Copilot.
# 3. Generate documentation in the terminal.
# 4. Export the documentation in HTML format and open it in a
# browser.

# course.py
courses = {}
def add_course(course_id, name, credits):
    """
    Adds a course to the course management system.

    Parameters:
    course_id (str): The unique identifier for the course.
    name (str): The name of the course.
    credits (int): The number of credits for the course.

    Returns:
    None
    """
    courses[course_id] = {'name': name, 'credits': credits}
def remove_course(course_id):
    """Removes a course from the course management system.
    Parameters:
    course_id (str): The unique identifier for the course to be removed.
    Returns:
    None
    """
    if course_id in courses:
        del courses[course_id]

def get_course(course_id):
    """
    Retrieves the details of a course from the course management system.

    Parameters:
    course_id (str): The unique identifier for the course to be retrieved.

    Returns:
    dict: A dictionary containing the name and credits of the course, or None if the course does not exist.
    """
    return courses.get(course_id)

print(get_course('CS101'))  # Output: None
add_course('CS101', 'Introduction to Computer Science', 4)
print(get_course('CS101'))  # Output: {'name': 'Introduction to Computer Science', 'credits': 4}
remove_course('CS101')
print(get_course('CS101'))  # Output: None
# To display the module documentation in the terminal, you can use the following code:
import pydoc
print(pydoc.render_doc('course.py'))
# To generate and export the module documentation in HTML format, you can run the following command in
# the terminal:
# pydoc -w course

# commands
# python -m pydoc -w calculator
# python -m pydoc -w conversion
# python -m pydoc -p 3000 
