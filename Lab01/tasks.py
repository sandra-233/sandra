
"""
Lab 01 — Python Basics

Complete all tasks below.

Topics:
- variables
- basic data types
- input and output
- type conversion
- arithmetic operators
- basic PEP 8
"""


# ============================================================
# Task 1 — Personal Information
# ============================================================

print("Task 1 — Personal Information")

# TODO:
# Ask the user to enter their name.

name = input("Enter your name: ")


# TODO:
# Ask the user to enter their age.
# Remember that input() returns a string.

age = int(input("enter your age: "))

# TODO:
# Print:
print(f"hello, {name}")
print(f"next year you will be {age + 1} years old")
# Hello, <name>!
# Next year you will be <age + 1> years old.


print()


# ============================================================
# Task 2 — Rectangle
# ============================================================

print("Task 2 — Rectangle")

# TODO:
# Ask the user to enter width and height.

#width = 0.0
#height = 0.0

width = float(input("Enter the width: "))

height = float(input("Enter the height: "))


# Calculate the area.

area = height * width


# Calculate the perimeter.

perimeter = 2 * (height + width)


# Print the results.

print("The area is:", area)
print("The perimeter is:", perimeter)


print()











# ============================================================
# Task 3 — Temperature Converter
# ============================================================

print("Task 3 — Temperature Converter")

# Formula:
# Fahrenheit = Celsius * 9 / 5 + 32

# TODO:
# Read Celsius temperature.
celsius = float(input("Enter Celsius temperature: "))

# celsius = 0.0

# TODO:
# Calculate Fahrenheit temperature.
fahrenheit = celsius * 9 / 5 + 32

#fahrenheit = 0.0

# TODO:
# Print the result.

print(" The Temperature in Fahrenheit is:", fahrenheit)

print()


# ============================================================
# Task 4 — Purchase Calculator
# ============================================================

print("Task 4 — Purchase Calculator")

# TODO:
# Ask for the number of items.
quantity = int(input("Enter the number of items: "))

#quantity = 0

# TODO:
# Ask for the price of one item.
price = float(input("Enter the price of one item: "))

#price = 0.0

# TODO:
# Calculate the total price.
total_price = quantity * price

#1total_price = 0.0

# TODO:
# Apply a 10% discount.

discounted_price = total_price * 0.90
#discounted_price = 0.0

# TODO:
# Print both results.
print(" The Total price is:", total_price)

print(" The Price after 10% discount is:", discounted_price)

print()


# ============================================================
# Task 5 — Arithmetic Operators
# ============================================================

print("Task 5 — Arithmetic Operators")

a = 17
b = 5

# TODO:
# Print the result of each operation:

print(a  + b)
print(a - b)

print(a * b)

print(a / b)

print(a // b)

print(a % b)

print(a ** b)

print()

#
# a + b
# a - b
# a * b
# a / b
# a // b
# a % b
# a ** b


#a = 17
#b = 5

# def add(a, b):
#     result = a + b
#     print("The sum of a and b is:", result)

# def subtract(a, b):
#     result = a - b
#     print("The difference of a and b is:", result)

# def multiply(a, b):
#     result = a * b
#     print("The product of a and b is:", result)

# def divide(a, b):
#     result = a / b
#     print("The division of a and b is:", result)

# def floor_divide(a, b):
#     result = a // b
#     print("The floor division of a and b is:", result)

# def remainder(a, b):
#     result = a % b
#     print("The remainder of a and b is:", result)

# def power(a, b):
#     result = a ** b
#     print("a raised to the power of b is:", result)


# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b)
# floor_divide(a, b)
# remainder(a, b)
# power(a, b)

# ============================================================
# Task 6 — Data Types
# ============================================================

print("Task 6 — Data Types")

integer_value = 42
float_value = 3.14
complex_value = 2 + 3j
text_value = "Python"
boolean_value = True

# TODO:
# Use type() to print the type of every variable above.
#
# Example:
# print(type(integer_value))
print("Data type of integer_value is:", type(integer_value))
print("Data type of float_value is:", type(float_value))
print("Data type of complex_value is:", type(complex_value))
print("Data type of text_value is:", type(text_value))
print("Data type of boolean_value is:", type(boolean_value))


print()


# Print the type of every variable
#print(type(integer_value))
#print(type(float_value))
#print(type(complex_value))
#print(type(text_value))
#print(type(boolean_value))

#print()

# ============================================================
# Task 7 — Comparisons and Boolean Logic
# ============================================================

print("Task 7 — Comparisons and Boolean Logic")

age = 22
is_master_student = True

# TODO:
# Print the result of the following expressions:
#
print("age >= 18:", age >= 18)
print("age < 30:", age < 30)
print("age == 22:", age == 22)
print("age != 25:", age != 25)

print("age >= 18 and is_master_student:", age >= 18 and is_master_student)
print("age < 18 or is_master_student:", age < 18 or is_master_student)
print("not is_master_student:", not is_master_student)


# age >= 18
# age < 30
# age == 22
# age != 25
#
# age >= 18 and is_master_student
# age < 18 or is_master_student
# not is_master_student
#
# Predict each result before running the program.


print()


# ============================================================
# Task 8 — Python Collections
# ============================================================

print("Task 8 — Python Collections")

# TODO:
# Create:
#
# 1. A list containing three programming languages.
# 2. A tuple containing three numbers.
# 3. A set containing several city names.
# 4. A dictionary describing a student with:
#       name
#       age
#       university

programming_languages = []
numbers = ()
cities = set()
student = {}

# 1. A list containing three programming languages.
programming_languages = ["Python", "Java", "C++"]

# 2. A tuple containing three numbers.
numbers = (10, 20, 30)

# 3. A set containing several city names.
cities = {"Lagos", "Moscow", "London"}

# 4. A dictionary describing a student.
student = {
    "name": "Sandra",
    "age": 22,
    "university": "NSU"
}





# TODO:

print("Programming languages:", programming_languages)
print("Numbers:", numbers)
print("Cities:", cities)
print("Student:", student)
# Print all four variables.
#
# TODO:
# Use type() to print the type of each collection.

print("Type of programming_languages:", type(programming_languages))
print("Type of numbers:", type(numbers))
print("Type of cities:", type(cities))
print("Type of student:", type(student))


print()


# ============================================================
# Task 9 — Indexing and Slicing
# ============================================================

print("Task 9 — Indexing and Slicing")

numbers = [0, 1, 2, 3, 4, 5, 6, 7]

# TODO:
# Print the first element.
print(numbers[0])

# TODO:
# Print the last element.
print(numbers[-1])
# TODO:
# Print elements from index 1 up to index 4.
print(numbers[1:4])
#
# Expected:
# [1, 2, 3]

# TODO:
# Print every second element.
print(numbers[::2])
#
# Expected:
# [0, 2, 4, 6]


word = "Python"

# TODO:
# Print the first character.
print(word[0])

# TODO:
# Print the last character.
print(word[-1])

# TODO:

print(word[0:3])
# Print:
# Pyt


print()


# ============================================================
# Task 10 — Dictionaries and Membership
# ============================================================

print("Task 10 — Dictionaries and Membership")

student = {
    "name": "Anna",
    "age": 22,
    "city": "Novosibirsk",
}

# TODO:
print("Student's name:", student["name"])
# Print the student's name.

# TODO:
# Print the student's age.
print("Student's age:", student["age"])

# TODO:
# Check whether "age" exists in the dictionary.
# Print the result.
print("Is age in the dictionary?", "age" in student)

# TODO:
# Check whether "email" exists in the dictionary.
# Print the result.
print("Is email in the dictionary?", "email" in student)


numbers = [10, 20, 30, 40]

# TODO:
# Check whether 20 is in numbers.
print("Is 20 in numbers?", 20 in numbers)
# TODO:
# Check whether 50 is in numbers.
print("Is 50 in numbers?", 50 in numbers)

print()


# ============================================================
# Task 11 — Formatted Output
# ============================================================

print("Task 11 — Formatted Output")

# TODO:
# Ask the user to enter the radius of a circle.
radius = float(input("Enter the radius of the circle: "))

#radius = 0.0

# Use:
# area = 3.14159 * radius ** 2

#area = 0.0

# TODO:
# Print the radius and area using an f-string.
#
print(f"Radius: {radius}")

# Example:
# Radius: 10.0
# Area: 314.16
#
# Print the area with exactly two digits after the decimal point.
#
print(f"Area: {area:.2f}")
# Hint:
# {value:.2f}


print()


# ============================================================
# Task 12 — Trip Cost Calculator
# ============================================================

print("Task 12 — Trip Cost Calculator")

# A car consumes a certain number of liters of fuel
# for every 100 kilometers.

# TODO:
# Ask the user to enter:
#

distance = float(input("Enter distance in kilometers: "))
# distance in kilometers
# fuel consumption in liters per 100 km
fuel_consumption = float(input("Enter fuel consumption (liters per 100 km): "))


# fuel price per liter

fuel_price = float(input("Enter fuel price per liter: "))
#distance = 0.0
#fuel_consumption = 0.0
#fuel_price = 0.0

# TODO:
# Calculate how many liters of fuel are required.
#
liters_needed = distance / 100 * fuel_consumption

# Formula:
# liters_needed = distance / 100 * fuel_consumption

#liters_needed = 0.0

# TODO:
# Calculate the total cost of the trip.

trip_cost = liters_needed * fuel_price
#trip_cost = 0.0

# TODO:
# Print something similar to:
#

print(f"Distance: {distance} km")
print(f"Fuel required: {liters_needed:.2f} liters")
print(f"Trip cost: {trip_cost:.2f}")

# Distance: 450.0 km
# Fuel required: 36.00 liters
# Trip cost: 2160.00
#
# Use f-strings and two decimal places where appropriate.
