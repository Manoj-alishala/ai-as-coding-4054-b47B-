def is_palindrome(num: int) -> bool:
    # Negative numbers are not palindromes
    if num < 0:
        return False
    
    original = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10          # Extract last digit
        reversed_num = reversed_num * 10 + digit  # Build reversed number
        num //= 10                # Remove last digit
    
    return original == reversed_num

print(is_palindrome(121))    # True
print(is_palindrome(-121))   # False
print(is_palindrome(12321))  # True
print(is_palindrome(123))    # False


def factorial(n: int) -> int:
    # Factorial is not defined for negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ✅ Examples
print(factorial(5))   # 120
print(factorial(0))   # 1
# print(factorial(-3)) # Raises ValueError



n = int(input().strip())

if n <= 1:
    print("Neither")
else:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print("Prime")
    else:
        print("Composite")



n = int(input().strip())

if n <= 1:
    print("Not a Perfect Number")
else:
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1

    if total == n:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")




try:
    n = int(input().strip())
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    pass

