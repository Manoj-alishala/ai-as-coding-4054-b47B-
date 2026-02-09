# Task 1 
# Bug: Mutable default argument
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
print(add_item(1))
print(add_item(2))


# Task 2
# Bug: Floating point precision issue
def check_sum():
    return abs((0.1 + 0.2) - 0.3) < 1e-9
print(check_sum())


# Task 3
# Bug: No base case
def countdown(n):
    if n == 0:
        return  
    print(n)
    return countdown(n-1)
countdown(5)


# Task 4
# Bug: Accessing non-existing key
def get_value():
    data = {"a": 1, "b": 2}
    return data.get("c", None)  
print(get_value())


# Task 5
# Bug: Infinite loop
def loop_example():
    i = 0
    while i < 5:
        print(i)
        i += 1
    
loop_example()


# Task 6
# Bug: Wrong unpacking
a, *b = (1, 2, 3)
print(a)  # 1
print(b)  # [2, 3]


# Task 7
# Bug: Mixed indentation
def func():
    x = 5
    y = 10
    return x+y
print(func())


# Task 8 
# Bug: Wrong import
import math
print(math.sqrt(16))


# Task 9 
# Bug: Early return inside loop
def total(numbers):
    total_sum = 0
    for n in numbers:
        total_sum += n
    return total_sum    
print(total([1,2,3]))


# Task 10 
# Bug: Using undefined variable
def calculate_area(length, width):
    return length * width
length = 5
width = 10
print(calculate_area(length, width))


# Task 11
# Bug: Adding integer and string
def add_values():
    return 5 + int("10")
print(add_values())


# Task 12
# Bug: Adding string and list
def combine():
    return "Numbers: " + str([1, 2, 3])
print(combine())


# Task 13
# Bug: Multiplying string by float
def repeat_text():
    return "Hello" * int(2.5)
print(repeat_text())


# Task 14
# Bug: Adding None and integer
def compute():
    value = None
    return (value or 0) + 10

print(compute())


# Task 15
# Bug: Input remains string
def sum_two_numbers():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    return int(a) + int(b)

print(sum_two_numbers())
