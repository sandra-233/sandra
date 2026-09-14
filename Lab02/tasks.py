"""
Lab 02 — Python Basics II

Complete all tasks below.

Topics:
- built-in functions
- assignment and augmented assignment
- operator precedence
- type conversion
- strings
- print() options
- collections
- mutable and immutable objects
- formatted output
- basic PEP 8
- reading common errors

Do not use:
- if
- for
- while
- user-defined functions
"""


# ============================================================
# Task 1 — Built-in Functions
# ============================================================

print("Task 1 — Built-in Functions")

values = [12, 7, 19, 5, 14]

# TODO:
# Using built-in functions, calculate and print:
#


# number of values
# smallest value
# largest value
# total
# mean
#
# Do not calculate these manually.

count = len(values)
smallest = min(values)
largest = max(values)
total = sum(values)
mean = sum(values) / len(values)

# TODO:
# Print the results using f-strings.

print(count)
print(smallest)
print(largest)
print(total)
print(mean)

print()


# ============================================================
# Task 2 — Absolute Value and Rounding
# ============================================================

print("Task 2 — Absolute Value and Rounding")


measurement = 19.87654
temperature_change = -7.438
# TODO:
# Print the absolute value of temperature_change.
#
print(abs(temperature_change))



# Expected numerical value:
# 7.438

# TODO:
# Round measurement to:
#
# 1 decimal place
# 2 decimal places
# 3 decimal places
#
# Use round().

print(round(measurement, 1))
print(round(measurement, 2))
print(round(measurement, 3))



print()


# ============================================================
# Task 3 — Assignment and Augmented Assignment
# ============================================================

print("Task 3 — Assignment and Augmented Assignment")

balance = 1000.0

# Perform the following operations using augmented assignment:
#
# 1. Add 250 to the balance.
# 2. Subtract 120.
# 3. Multiply the remaining balance by 1.05.
#
# TODO:
# Replace the normal assignments below with +=, -=, and *=.

balance = balance +250

balance = balance -120

balance = balance * 1.05



balance +=250
balance -= 120
balance *= 1.05






# TODO:
# Print the final balance with two decimal places.
print(f"{balance: .2f}")


print()


# ============================================================
# Task 4 — Operator Precedence
# ============================================================

print("Task 4 — Operator Precedence")

# Before running the program, predict each result.

expression_1 = 2 + 3 * 4
expression_2 = (2 + 3) * 4
expression_3 = 20 / 5 + 3
expression_4 = 20 / (5 + 3)
expression_5 = 2 ** 3 ** 2

# TODO:
# Print each expression and its result.
#
# Example:
# 2 + 3 * 4 = 14

print(expression_1)
print(expression_2)
print(expression_3)
print(expression_4)
print(expression_5)
print()


# ============================================================
# Task 5 — Time Conversion
# ============================================================

print("Task 5 — Time Conversion")

# TODO:
# Ask the user to enter a number of seconds.

total_seconds = int(input("Enter a number of seconds:" ))

# TODO:
# Convert the input to int.
135
# TODO:
# Calculate:
minutes = total_seconds  // 60
remaining_seconds = total_seconds % 60
#
# Example:
# 135 seconds -> 2 minutes and 15 seconds
#
# Hint:
# // and %

#minutes = 0
#remaining_seconds = 0

# TODO:
# Print:
# 135 seconds = 2 minute(s) and 15 second(s)
print(f"{total_seconds} seconds = {minutes} minute(s) and {remaining_seconds} second(s)")

print()


# ============================================================
# Task 6 — Conversion Is Not Always Reversible
# ============================================================

print("Task 6 — Type Conversion")

value = 17.95

# TODO:
# Convert value to int and print it.
#


# Question:
# Does int() round the value?

integer_value  = int(value)

print(integer_value, "is for type:" , type(integer_value))
# TODO:
# Convert integer_value back to float and print it.

float_value = float(integer_value)
print(float_value)


# TODO:
# Convert integer_value to str and print:
#


# Value as text: <value>
# Type: <type>
#
# Use type() for the second line.

text_value = str(integer_value)
print("Value as text:", text_value)
print("Type:", type(text_value))


print()


# ============================================================
# Task 7 — Basic String Operations
# ============================================================

print("Task 7 — Basic String Operations")

first_name = (input("First name: "))
last_name = (input("Last name: "))

# TODO:
# Create full_name using string concatenation.

full_name =(input("full name:"))

# TODO:
# Print:
#
# Full name: <full_name>
# Number of characters: <length>
# First character: <first character>
# Last character: <last character>
# First three characters: <slice>

print(len(full_name))
print(full_name[0])
print(full_name[-1])
print(full_name[: 3])


# TODO:
# Print full_name three times using string repetition.

print(full_name * 3)

print(full_name )
print(full_name )
print(full_name )
print()


# ============================================================
# Task 8 — Useful print() Options
# ============================================================

print("Task 8 — Useful print() Options")

language = "Python"
course = "AI and Big Data Analytics"
university = "NSU"

# TODO:
# Print the three values on one line separated by:
#
#  |
#
# Expected:
# Python | AI and Big Data Analytics | NSU
#
# Use sep=
print(language , course, university, sep = "|")

# TODO:
# Use two print() calls and end= so that the result is:
#
# Python Programming
#
# Do not write "Python Programming" as one string.

print("python", end=" ")
print("programming")
print()


# ============================================================
# Task 9 — Collections and Choosing Data Structures
# ============================================================

print("Task 9 — Collections")

student_name = "Anna"
student_age = 22
student_skills = ["Python", "Mathematics", "Machine Learning"]
student_university = "NSU"

# TODO:
# Create a dictionary named student with the keys:
#
# name
# age
# skills
# university

student = {"name" : student_name,  "age": student_age,  "skills" : student_skills, "university": student_university}

# accessing information

print(student["name"])

print(student["university"])

print(student["skills"][0])

print(len(student["skills"]))


# TODO:
# Print:
#
# student's name
# student's university
# first skill
# number of skills
#
# Use dictionary access, indexing, and len().


print()


# ============================================================
# Task 10 — Mutable and Immutable Objects
# ============================================================

print("Task 10 — Mutable and Immutable Objects")

# List example — mutable

numbers = [10, 20, 30]
same_numbers = numbers

# TODO:
# Change the first item in numbers to 99.



numbers [0]=99

#
# Then print both:
#
# numbers
# same_numbers
#
# Observe what happened.

print(numbers)
print(same_numbers)

# String example — immutable

text = "Python"
same_text = text

text= text +  " course "

print(text)

print(same_text)

# TODO:
# Create a new string by adding " Course" to text.
#
# Then print:
#
# text
# same_text
#
# Compare this result with the list example.


print()


# ============================================================
# Task 11 — Small Statistics Report
# ============================================================

print("Task 11 — Small Statistics Report")

scores = [78, 92, 85, 69, 88]

# TODO:
# Calculate:
#
# number of scores
# minimum score
# maximum score
# total score
# mean score
#
# Use built-in functions.

score_count = len(scores)
minimum_score = min(scores)
maximum_score = max(scores)
total_score = sum(scores)
mean_score = sum(scores)/ len(scores)


# TODO:
# Print a clean report:
#
# Number of scores: 5
# Minimum: 69
# Maximum: 92
# Mean: 82.40
#
# Format the mean to exactly two decimal places.
print(len(scores))
print(min(scores))
print(max(scores))
print(mean_score)

print()


# ============================================================
# Task 12 — PEP 8 Cleanup
# ============================================================

print("Task 12 — PEP 8 Cleanup")

# The following code works, but it is difficult to read.
#
# TODO:
# Rewrite it using:
#
# meaningful variable names
# snake_case
# spaces around operators
# intermediate variables
# formatted output
#
# Keep the same calculation.

P=1250
Q=3
D=10
X=P*Q-D/100*P*Q


print("Final:",X)



p= "price"
Q= "quantity"
D= "Discounted_percent"
X = "subtotal"


print()


# ============================================================
# Optional Challenge — Student Score Summary
# ============================================================

print("Optional Challenge — Student Score Summary")

# Create a small program using only concepts from Sections 1–2.
#
# Ask the user for:
#
# student name
# three test scores
#
# Store the three scores in a list.
#
# Calculate:
#
# minimum score
# maximum score
# mean score
#
# Print a clean summary similar to:
#
# Student: Anna
# Scores: [78.0, 85.0, 91.0]
# Minimum: 78.00
# Maximum: 91.00
# Mean: 84.67
#
# Use:
# input()
# float()
# list
# min()
# max()
# sum()
# len()
# f-strings


# ============================================================
# Task 13 — Multiple Assignment
# ============================================================

print("Task 13 — Multiple Assignment")

# TODO:
# Assign these three values using ONE statement:
#
# x = 10
# y = 20
# z = 30

x = 10
y = 20
z = 30

# TODO:
# Print x, y, and z.
print(x)
print(y)
print(z)




# TODO:
# Swap a and b using one Python statement.

a = 5
b = 10

a, b = b, a

# Expected after swapping:
# a = 10
# b = 5
print(a)
print(b)


print()



# ============================================================
# Task 14 — String Methods
# ============================================================

print("Task 14 — String Methods")

text = "  Python Programming Course  "

print(text)

# TODO:
# Print the text:
#
# 1. without surrounding spaces
# 2. in lowercase
# 3. in uppercase
# 4. with "Course" replaced by "Lab"

cleaned_text= text.strip()
print(cleaned_text)

print(cleaned_text.lower())

print(cleaned_text.upper())

print(cleaned_text.replace("Course", "Lab"))

print(cleaned_text.startswith("Python"))

print(cleaned_text.endswith("Course"))


# TODO:
# Check and print whether the cleaned text:
#
# starts with "Python"
# ends with "Course"
#
# Use:
# strip()
# lower()
# upper()
# replace()
# startswith()
# endswith()


print()

# ============================================================
# Task 15 — Boolean Expressions
# ============================================================

print("Task 15 — Boolean Expressions")

age = 22
score = 85
is_master_student = True

# TODO:
# Print the result of:

# age >= 18
# score >= 60
# score >= 60 and is_master_student
# score < 60 or age < 18
# not is_master_student

print(age >= 18)

print(score >= 60)
print(score >= 60 and is_master_student)
print( score < 60 or age < 18)
print(not is_master_student)


# TODO:
# Predict and then print:

print(bool(0))
print (bool(1))
print(bool(""))
print (bool("Python"))
print(bool([]))
print(bool([1, 2]))


print()

# ============================================================
# Task 16 — Membership
# ============================================================

print("Task 16 — Membership")

numbers = [10, 20, 30]
text = "Python Programming"
student = {
    "name": "Anna",
    "age": 22,
}

# TODO:
# Print the result of:

print("20 in numbers")
print("50 not in numbers")
print("Python" in text)
print( "Java" not in text)
print("age" in student)
print("email" in student)


print()