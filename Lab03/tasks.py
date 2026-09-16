"""
NSU Python — Lab 03
Conditions and for Loops

Complete Tasks 1–12.
Tasks 13–14 are optional bonus tasks.

Use only concepts covered in Lecture 03.
"""


# ============================================================
# Task 1 — Positive, negative, or zero
# ============================================================
# Ask the user to enter an integer.
# Print exactly one of:
#   Positive
#   Negative
#   Zero
#
# Example:
# Input: -7
# Output: Negative

# Write your code below:

number = int(input("Enter an integer: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

     

# ============================================================
# Task 2 — Age category
# ============================================================
# Ask the user for their age.
#
# Print:
#   Child      -> age < 13
#   Teenager   -> 13–17
#   Adult      -> 18–64
#   Senior     -> 65 or older
#
# Test boundary values: 12, 13, 17, 18, 64, 65.

# Write your code below:
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")

# ============================================================
# Task 3 — Grade classifier
# ============================================================
# Ask the user for a score.
#
# First check whether the score is between 0 and 100 inclusive.
#
# For a valid score:
#   A    -> 90–100
#   B    -> 75–89
#   C    -> 60–74
#   Fail -> below 60
#
# For an invalid score print:
#   Invalid score

# Write your code below:
score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("Fail")

# ============================================================
# Task 4 — Access decision
# ============================================================
# Ask the user for:
#   age
#   whether they have a ticket: yes/no
#
# A person may enter only if:
#   age >= 18 AND they have a ticket.
#
# Print one of:
#   Access granted
#   Ticket required
#   Must be 18 or older

# Write your code below:

age = int(input("Enter your age: "))
ticket = input("Do you have a ticket? yes/no: ")

if age >= 18 and ticket == "yes":
    print("Access granted")
elif age < 18:
    print("Must be 18 or older")
else:
    print("Ticket required")
# ============================================================
# Task 5 — Even numbers with range()
# ============================================================
# Print all even numbers from 2 through 30.
#
# Required:
# Use range(start, stop, step).

# Write your code below:
for number in range(2, 32, 2):
    print(number)
    


# ============================================================
# Task 6 — Sum of multiples of 3
# ============================================================
# Calculate and print the sum of all multiples of 3
# from 3 through 99.
#
# Required:
# Use a for loop and an accumulator.
#
# Expected result:
# 1683

# Write your code below:
total = 0

for number in range(3, 100, 3):
    total = total + number

print(total)

# ============================================================
# Task 7 — Count number categories
# ============================================================
numbers = [4, -2, 0, 7, -5, 9, 0, -1, 8]

# Count how many values are:
#   positive
#   negative
#   zero
#
# Print all three counts.
# Do not manually count the values.

numbers = [4, -2, 0, 7, -5, 9, 0, -1, 8]

positive = 0
negative = 0
zero = 0

for number in numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
# Write your code below:


# ============================================================
# Task 8 — Count vowels
# ============================================================
# Ask the user to enter a word or short text.
# Count how many vowels it contains.
#
# Treat uppercase and lowercase equally.
# Vowels: a e i o u
#
# Example:
# Input: Artificial Intelligence
# Output: 10
#
# Hint:
# Iterate directly over the string.

text = input("Enter a word or short text: ")

vowels = 0

for letter in text:
    if letter.lower() in "aeiou":
        vowels += 1

print(vowels)
# Write your code below:


# ============================================================
# Task 9 — Student results
# ============================================================
scores = [85, 42, 67, 91, 58, 73, 100, 39]

# Count:
#   passed students: score >= 60
#   failed students: score < 60
#
# Also print the average score.
#
# Required:
# Use a loop to calculate the total.
#
# Expected:
# Passed: 5
# Failed: 3
# Average: 69.38

# Write your code below:
scores = [85, 42, 67, 91, 58, 73, 100, 39]

passed = 0
failed = 0
total = 0

for score in scores:
    total += score

    if score >= 60:
        passed += 1
    else:
        failed += 1

average = total / len(scores)

print("Passed:", passed)
print("Failed:", failed)
print("Average:", round(average, 2))

# ============================================================
# Task 10 — Search and stop
# ============================================================
names = ["Anna", "Boris", "Sasha", "Maria", "Oleg", "Dina"]

# Ask the user for a name.
# Search the list using a for loop.
#
# If found:
#   print "Found"
#   stop immediately with break
#
# If not found:
#   print "Not found"
#
# Do not use:
#   if target in names
#
# Hint:
# A Boolean variable such as found = False can help.

# Write your code below:
names = ["Anna", "Boris", "Sasha", "Maria", "Oleg", "Dina"]

target = input("Enter a name: ")

found = False

for name in names:
    if name == target:
        print("Found")
        found = True
        break

if found == False:
    print("Not found")

# ============================================================
# Task 11 — Skip invalid scores
# ============================================================
raw_scores = [78, -5, 91, 120, 66, 0, 88, 101, 54]

# Valid scores are from 0 to 100 inclusive.
#
# Use continue to skip invalid scores.
# For valid scores:
#   print each valid score
#   calculate the average of valid scores
#
# At the end print:
#   Valid scores: ...
#   Average: ...
#
# Required:
# Use continue.

# Write your code below:

raw_scores = [78, -5, 91, 120, 66, 0, 88, 101, 54]

total = 0
count = 0

for score in raw_scores:
    if score < 0 or score > 100:
        continue

    print(score)
    total += score
    count += 1

average = total / count

print("Valid scores:", count)
print("Average:", round(average, 2))
# ============================================================
# Task 12 — Dictionary iteration
# ============================================================
student_scores = {
    "Anna": 92,
    "Boris": 58,
    "Sasha": 76,
    "Maria": 49,
    "Oleg": 84,
}

# Iterate using .items().
#
# Print:
#   Anna: Pass
#   Boris: Fail
#   ...
#
# Score >= 60 means Pass.
# Then print how many students passed.

# Write your code below:
student_scores = {
    "Anna": 92,
    "Boris": 58,
    "Sasha": 76,
    "Maria": 49,
    "Oleg": 84,
}

passed = 0

for name, score in student_scores.items():
    if score >= 60:
        print(name + ": Pass")
        passed += 1
    else:
        print(name + ": Fail")

print("Students passed:", passed)

# ============================================================
# BONUS Task 13 — FizzBuzz
# ============================================================
# Print numbers 1 through 30.
#
# If divisible by both 3 and 5 -> FizzBuzz
# If divisible only by 3       -> Fizz
# If divisible only by 5       -> Buzz
# Otherwise print the number.
#
# Hint:
# Check the most specific condition first.

# Write your code below:

for number in range(1, 31):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
# ============================================================
# BONUS Task 14 — Limited login attempts
# ============================================================
correct_pin = "4821"

# Give the user at most 3 attempts to enter the PIN.
#
# Use:
#   for
#   range()
#   break
#
# Correct PIN:
#   Access granted
#
# Three wrong attempts:
#   Access denied
#
# Do NOT use a while loop.

# Write your code below:
correct_pin = "4821"

for attempt in range(3):
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Access granted")
        break
else:
    print("Access denied")