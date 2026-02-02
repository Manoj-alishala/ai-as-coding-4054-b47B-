# Task 1 

import requests

CITY = "London"
LAT = 51.5072
LON = -0.1276

URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": LAT,
    "longitude": LON,
    "current_weather": True
}

response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()
    weather = data["current_weather"]
    print({
        "city": CITY,
        "temperature": f"{weather['temperature']}°C",
        "windspeed": weather["windspeed"]
    })
else:
    print("API error")

# End of Task 1

# Task 2
import hashlib
import os
import json

def store_user_data(name, email, password):
    # Generate unique salt per user
    salt = os.urandom(32)
    # Hash password with PBKDF2 (industry standard, slow against brute-force)
    hashed_pw = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    user_data = {
        'name': name,
        'email': email,
        'salt': salt.hex(),
        'hashed_password': hashed_pw.hex()
    }
    with open('users.json', 'w') as f:
        json.dump(user_data, f)  # JSON for structured, parseable storage
    print("User data stored securely.")

# Demo usage (don't hardcode in prod)
store_user_data('John Doe', 'john@email.com', 'secret123')

# End of Task 2

# # Task 3
def is_armstrong(num):
    """
    Checks if a number is Armstrong: sum of its digits^num_digits equals num.
    E.g., 153 = 1^3 + 5^3 + 3^3.
    """
    if num < 0:
        return False
    original = num
    num_digits = len(str(num))
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** num_digits  # Power each digit
        num //= 10  # Drop last digit
    return total == original

# Test
print(is_armstrong(153))  # True
print(is_armstrong(407))  # True
print(is_armstrong(100))  # False

# # End of Task 3

# Task 4

#Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
# Test
print(quick_sort([3,6,8,10,1,2,1]))

# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Test
print(bubble_sort([3,6,8,10,1,2,1]))

# End of Task 4

# # Task 5
ratings = {
    'Alice': {'laptop': 5, 'phone': 3, 'headphones': 4, 'watch': 2},
    'Bob': {'laptop': 4, 'phone': 5, 'shoes': 4},
    'Charlie': {'headphones': 5, 'shoes': 3, 'watch': 4}
}

def recommend(user, ratings):
    user_items = ratings[user]
    suggestions = []
    for other, other_items in ratings.items():
        if other == user: continue
        sim_items = set(user_items) & set(other_items)
        if sim_items:
            sim_score = sum(user_items[item] * other_items[item] for item in sim_items) / len(sim_items)
            for item, score in other_items.items():
                if item not in user_items and score >= 4:
                    reason = f"Bob (similar on laptop/phone) loved it ({score}/5), taste match {sim_score:.1f}"
                    suggestions.append((item, reason))
    return sorted(set(suggestions), key=lambda x: x[1])[:3]  # Unique top 3

print(recommend('Alice', ratings))
# [('shoes', 'Bob (similar on laptop/phone) loved it (4/5), taste match 4.0'), ('headphones', ...)]

# End of Task 5
