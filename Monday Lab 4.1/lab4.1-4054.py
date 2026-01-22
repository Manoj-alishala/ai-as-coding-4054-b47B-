
# Leap year checker
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# End of code


# Cm -> Inches converter
cm = float(input("Enter length in centimeters: "))
inches = cm / 2.54
print(f"{cm} cm is equal to {inches:.2f} inches.")

# End of code


# Accepts a full First and Last name
#Example : •	"John Smith" → "Smith, John "Anita Rao" → "Rao, Anita""

name = input("Enter your full name: ")
first_name, last_name = name.split()
print(f"{last_name}, {first_name}")

# End of code



# # vowels in string - zero short
string = input("Enter a string: ")
vowels = "aeiou"
for char in string:
    if char in vowels:
        print(char)

# # End of code

# # vowels in string - Few Short
# #Example : •	"Hello World" → 3 •	"Python Programming is fun" → 5
string = input("Enter a string: ")
vowels = "aeiou"
for char in string:
    if char.lower() in vowels:
        print(char)


# End of code


# reading .txt file and counting lines
file_path = input("Enter the file path: ")
with open(file_path, 'r') as file:
    lines = file.readlines()
    line_count = len(lines)
    print(f"The file has {line_count} lines.")
