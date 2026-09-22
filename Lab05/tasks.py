"""
NSU Python — Lab 05
Functions in Practice: Arguments, Recursion, math, and List Methods

Complete Tasks 1–12.
Tasks 13–14 are optional bonus tasks.

Use only concepts covered in Lecture 05 and earlier lectures.
Do not use lambda, sorted(), filter(), or map() in this lab.
"""

# ============================================================
# Task 1 — Positional and keyword arguments
# ============================================================
# Create a function:
#
#   describe_student(name, age, city)
#
# The function should print:
#   Name: ...
#   Age: ...
#   City: ...
#
# Call the function three times:
# 1. using only positional arguments;
# 2. using only keyword arguments in a different order;
# 3. using one positional argument and the rest as keyword arguments.
#
# Example:
# describe_student("Anna", 23, "Novosibirsk")
#
# Output:
# Name: Anna
# Age: 23
# City: Novosibirsk

# Write your code below:
# Create the function
def describe_student(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


# 1. Using only positional arguments
describe_student("Anna", 23, "Novosibirsk")


# 2. Using only keyword arguments in a different order
describe_student(city="Novosibirsk", name="Anna", age=23)


# 3. Using one positional argument and the rest as keyword arguments
describe_student("Anna", age=23, city="Novosibirsk")


# ============================================================
# Task 2 — Default arguments
# ============================================================
# Create a function:
#
#   shipping_cost(weight, rate=2.5)
#
# It should return:
#   weight * rate
#
# Call it:
# 1. with only weight;
# 2. with a custom rate;
# 3. with rate passed as a keyword argument.
#
# Example:
# shipping_cost(4)
# returns 10.0

# Write your code below:
def shipping_cost(weight, rate=2.5):
    return weight * rate
print(shipping_cost(4))
print(shipping_cost(4, 3.0))
print(shipping_cost(4, rate= 2.5))


# ============================================================
# Task 3 — Early return
# ============================================================
# Create a function:
#
#   safe_divide(a, b)
#
# If b is 0, return None immediately.
# Otherwise return a / b.
#
# Test:
# safe_divide(10, 2)  -> 5.0
# safe_divide(10, 0)  -> None

# Write your code below:
def safe_divide(a, b):
    if b == 0:
        return None
    
    return a / b


# Test
print(safe_divide(10, 2))
print(safe_divide(10, 0))

# ============================================================
# Task 4 — *args: total score
# ============================================================
# Create a function:
#
#   total_score(*scores)
#
# Return the sum of all scores.
#
# The function must work with any number of arguments,
# including zero arguments.
#
# Examples:
# total_score(10, 20, 30) -> 60
# total_score(5)          -> 5
# total_score()           -> 0
#
# Inside the function, scores is a tuple.

# Write your code below:
def total_score(*scores):
    return sum(scores)


print(total_score(10, 20, 30))
print(total_score(5))
print(total_score())

# ============================================================
# Task 5 — *args: average score
# ============================================================
# Create a function:
#
#   average_score(*scores)
#
# If no scores are given, return None.
# Otherwise return the arithmetic mean.
#
# Examples:
# average_score(80, 90, 100) -> 90.0
# average_score()             -> None

# Write your code below:
def average_score(*scores):
    if len(scores)==0:
        return None
    return  sum(scores) / len(scores)  
print(average_score(80, 90, 100))
print(average_score())


# ============================================================
# Task 6 — **kwargs: profile
# ============================================================
# Create a function:
#
#   show_profile(**details)
#
# Print each key and value in this form:
#   key: value
#
# Example call:
# show_profile(name="Anna", city="Novosibirsk", year=1)
#
# Possible output:
# name: Anna
# city: Novosibirsk
# year: 1

# Write your code below:
def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_profile(name="Anna", city="Novosibirsk", year=1)

# ============================================================
# Task 7 — Combining fixed arguments, *args, and **kwargs
# ============================================================
# Create a function:
#
#   course_report(student, *scores, **options)
#
# It should print:
#   Student: ...
#   Scores: (...)
#   Options: {...}
#
# Example:
# course_report(
#     "Mira",
#     80, 92, 75,
#     rounded=True,
#     scale=100
# )
#
# Expected structure:
# Student: Mira
# Scores: (80, 92, 75)
# Options: {'rounded': True, 'scale': 100}

# Write your code below:
def course_report(student, *scores, **options):
    print("Student:", student)
    print("Scores:", scores)
    print("Options:", options)


# Function call
course_report(
    "Mira",
    80, 92, 75,
    rounded=True,
    scale=100
)


# ============================================================
# Task 8 — Scope
# ============================================================
# Create a global variable:
#
#   TAX_RATE = 0.20
#
# Create a function:
#
#   final_price(price)
#
# Inside the function:
# 1. calculate a LOCAL variable called tax;
# 2. return price + tax.
#
# Do not modify TAX_RATE.
#
# Example:
# final_price(100) -> 120.0
#
# Think about:
# - TAX_RATE is global.
# - tax exists only inside final_price().

# Write your code below:
TAX_RATE = 0.20

def final_price(price):
    tax = price * TAX_RATE
    return price + tax
print(final_price(100))


# ============================================================
# Task 9 — Recursive countdown
# ============================================================
# Create a recursive function:
#
#   countdown(n)
#
# If n == 0:
#   print("Go!")
#   stop the function.
#
# Otherwise:
#   print n
#   call countdown(n - 1)
#
# Do NOT use a loop.
#
# Example:
# countdown(3)
#
# Output:
# 3
# 2
# 1
# Go!

# Write your code below:
# Task 9 — Recursive countdown

def countdown(n):
    if n == 0:
        print("Go!")
        return
    
    print(n)
    countdown(n - 1)


countdown(3)



# ============================================================
# Task 10 — Recursive factorial
# ============================================================
# Create a recursive function:
#
#   factorial(n)
#
# Rules:
# - if n < 0, return None;
# - if n == 0, return 1;
# - otherwise return n * factorial(n - 1).
#
# Do NOT use a loop.
#
# Examples:
# factorial(5)  -> 120
# factorial(0)  -> 1
# factorial(-2) -> None

# Write your code below:

def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))   # 120
print(factorial(0))   # 1
print(factorial(-2))  # None
# ============================================================
# Task 11 — Recursive sum
# ============================================================
# Create a recursive function:
#
#   sum_to(n)
#
# It should return:
#   1 + 2 + 3 + ... + n
#
# Rules:
# - if n < 0, return None;
# - if n == 0, return 0;
# - otherwise use recursion.
#
# Do NOT use a loop and do NOT use sum().
#
# Examples:
# sum_to(4) -> 10
# sum_to(0) -> 0

# Write your code below:

def sum_to(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    return n + sum_to(n - 1)


print(sum_to(4))   # 10
print(sum_to(0))   # 0
# ============================================================
# Task 12 — math module and list methods
# ============================================================
# Part A — math
#
# Import math.
#
# Ask the user for the radius of a circle.
# Calculate and print:
# - circumference = 2 * math.pi * radius
# - area = math.pi * radius ** 2
# - area rounded UP with math.ceil()
# - area rounded DOWN with math.floor()
#
# Example for radius 3:
# Circumference: 18.849...
# Area: 28.274...
# Area ceil: 29
# Area floor: 28
#
#
# Part B — list methods
#
# Start with:
# numbers = [10, 20, 20, 30]
#
# Perform these operations in order:
# 1. append 40
# 2. extend with [50, 60]
# 3. insert 15 at index 1
# 4. print how many times 20 appears
# 5. print the index of the first 30
# 6. remove the first 20
# 7. pop the last item and save it in removed
# 8. print numbers
# 9. print removed
#
# Do not use sorted() in this task.

# Write your code below:
import math

# ============================================================
# Part A — math
# ============================================================

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("Circumference:", circumference)
print("Area:", area)
print("Area ceil:", math.ceil(area))
print("Area floor:", math.floor(area))


# ============================================================
# Part B — list methods
# ============================================================

numbers = [10, 20, 20, 30]

# 1. Append 40
numbers.append(40)

# 2. Extend with [50, 60]
numbers.extend([50, 60])

# 3. Insert 15 at index 1
numbers.insert(1, 15)

# 4. Print how many times 20 appears
print("Count of 20:", numbers.count(20))

# 5. Print the index of the first 30
print("Index of 30:", numbers.index(30))

# 6. Remove the first 20
numbers.remove(20)

# 7. Pop the last item and save it in removed
removed = numbers.pop()

# 8. Print numbers
print("Numbers:", numbers)

# 9. Print removed
print("Removed:", removed)

# ============================================================
# Task 13 — BONUS: Recursive digit sum
# ============================================================
# Create a recursive function:
#
#   digit_sum(n)
#
# Assume n is a non-negative integer.
#
# Return the sum of its digits.
#
# Hint:
# - last digit: n % 10
# - remaining digits: n // 10
#
# Base case:
# if n < 10, return n
#
# Examples:
# digit_sum(1234) -> 10
# digit_sum(7)    -> 7
#
# Do NOT convert the number to a string.
# Do NOT use a loop.

# Write your code below:

def digit_sum(n):
    if n < 10:
        return n
    return (n % 10) + digit_sum(n // 10)


print(digit_sum(1234))  # 10
print(digit_sum(7))     # 7
# ============================================================
# Task 14 — BONUS: Student result summary
# ============================================================
# Create a function:
#
#   result_summary(name, *scores, passing=60)
#
# Requirements:
# - if no scores are given, return:
#     "No scores"
# - calculate the average;
# - count how many scores are >= passing;
# - return a string in this form:
#
#   "Anna: average=80.0, passed=3/4"
#
# Example:
# result_summary("Anna", 80, 70, 50, 120, passing=60)
#
# returns:
# "Anna: average=80.0, passed=3/4"
#
# Use a loop to count passed scores.
# Do not use filter() or map().

# Write your code below:
def result_summary(name, *scores, passing=60):
    if not scores:
        return "No scores"

    # Calculate average
    average = sum(scores) / len(scores)

    # Count passed scores using a loop
    passed = 0

    for score in scores:
        if score >= passing:
            passed += 1

    return f"{name}: average={average:.1f}, passed={passed}/{len(scores)}"


print(result_summary("Anna", 80, 70, 50, 120, passing=60))