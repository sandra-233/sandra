"""NSU Python — Lab 09
Exceptions and OOP Foundations

Main tasks: 1–12. Course minimum: at least 10 main tasks.
Aim to complete all 12, including both exceptions and OOP practice.
Tasks 13–14 are optional bonuses.
Use only Lecture 09 and earlier concepts. No inheritance, super(),
properties, decorators, or external packages are needed.
"""

from pathlib import Path

LAB_DIR = Path(__file__).resolve().parent
DATA = LAB_DIR / "data"


# ============================================================
# Task 1 — Safe integer conversion
# ============================================================
# Ask the user for an integer. Catch ValueError if conversion fails.
# On success print "Number: N". On failure print "Invalid integer".
# Use try/except/else: print the successful result inside else.
# Test: "12" -> Number: 12; "hello" -> Invalid integer;
# "3.5" -> Invalid integer. Do not use a loop in this task.

# Write your code below:
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid integer")
else:
    print("Number:", number)

# ============================================================
# Task 2 — Safe division
# ============================================================
# Ask for two integers. Divide the first by the second.
# Handle ValueError and ZeroDivisionError with separate except blocks.
# Print "Enter integers" for invalid text, "Cannot divide by zero" for a
# zero divisor, and the result on success.
# Tests: 10 and 2 -> 5.0; 10 and 0 -> Cannot divide by zero;
# hello as the first input -> Enter integers (no second prompt is needed).

# Write your code below:
try:
    first= int(input("Enter the 1st integer:"))
    second=int(input("Enter the 2nd integer:"))
    
    result=first/second
except ValueError:
    print("Enter integers")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(result)


# ============================================================
# Task 3 — try, except, else, and finally
# ============================================================
# For each text in ["8", "bad", "0"], attempt int(text).
# Use a try statement INSIDE the loop.
# On success print "Converted: N" using else.
# On ValueError print "Invalid: TEXT".
# Always print "Attempt finished" using finally.
# Expected output:
# Converted: 8
# Attempt finished
# Invalid: bad
# Attempt finished
# Converted: 0
# Attempt finished

# Write your code below:

# Task 3 — try, except, else, and finally

for text in ["8", "bad", "0"]:
    try:
        number = int(text)
    except ValueError:
        print("Invalid:", text)
    else:
        print("Converted:", number)
    finally:
        print("Attempt finished")
# ============================================================
# Task 4 — Validate a score with raise
# ============================================================
# Define validate_score(score). Assume score is an integer.
# Return score when 0 <= score <= 100. Otherwise raise
# ValueError("Score must be between 0 and 100").
# Call the function for [-1, 0, 75, 100, 101]. Use try/except around each
# call and print the returned value or the exception message.
# Expected: error message, 0, 75, 100, error message (one per line).

# Write your code below:

def validate_score(score):
    if 0 <= score <= 100:
        return score
    else:
        raise ValueError("Score must be between 0 and 100")


for score in [-1, 0, 75, 100, 101]:
    try:
        result = validate_score(score)
        print(result)
    except ValueError as error:
        print(error)
# ============================================================
# Task 5 — Read a file safely
# ============================================================
# Define read_first_integer(path).
# Open the file using with and encoding="utf-8". Read the first line,
# strip whitespace, convert it to int, and return the integer.
# Let exceptions propagate from the function. At the CALL SITE, handle
# FileNotFoundError and ValueError separately for these paths:
# DATA / "number_valid.txt" -> print Number: 42
# DATA / "number_invalid.txt" -> print Invalid file content
# DATA / "missing.txt" -> print File not found
# Do not create missing.txt and do not change the supplied files.

# Write your code below:

def read_first_integer(path):
    with open(path, "r", encoding="utf-8") as file:
        line = file.readline().strip()
        number = int(line)
        return number


try:
    number = read_first_integer(DATA / "number_valid.txt")
    print("Number:", number)
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid file content")


try:
    number = read_first_integer(DATA / "number_invalid.txt")
    print("Number:", number)
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid file content")


try:
    number = read_first_integer(DATA / "missing.txt")
    print("Number:", number)
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid file content")
# ============================================================
# Task 6 — Retry until input is valid
# ============================================================
# Repeatedly ask for a positive integer using while True.
# If conversion fails, print "Enter a whole number" and retry.
# If the number is 0 or negative, print "Enter a positive number" and retry.
# On success print "Accepted: N" and stop the loop.
# Test this input sequence: hello, 0, -3, 7.
# Only 7 should be accepted.

# Write your code below:

while True:
    try:
        number = int(input("Enter a positive integer: "))
    except ValueError:
        print("Enter a whole number")
        continue

    if number <= 0:
        print("Enter a positive number")
        continue

    print("Accepted:", number)
    break
# ============================================================
# Task 7 — A Book class
# ============================================================
# Create Book with __init__(self, title, author).
# Store title and author as instance attributes.
# Create two different books and print each title and author.
# Add describe(self), returning "TITLE by AUTHOR".
# For Book("Python Basics", "A. Ivanov"), describe() must return
# "Python Basics by A. Ivanov".
# The method returns the string; the calling code prints it.

# Write your code below:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return self.title + " by " + self.author


book1 = Book("Python Basics", "A. Ivanov")
book2 = Book("Data Science", "B. Smith")

print(book1.title, book1.author)
print(book2.title, book2.author)

print(book1.describe())
print(book2.describe())
# ============================================================
# Task 8 — A Rectangle class
# ============================================================
# Create Rectangle with width and height instance attributes.
# Initialize both in __init__. Assume positive numeric dimensions for now.
# Add area() and perimeter() methods that RETURN numbers.
# For Rectangle(3, 4), area() returns 12 and perimeter() returns 14.
# Create a second rectangle with dimensions 2 and 5 and print both results
# for both objects. Do not use inheritance.

# Write your code below:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rectangle1 = Rectangle(3, 4)
rectangle2 = Rectangle(2, 5)

print(rectangle1.area())
print(rectangle1.perimeter())

print(rectangle2.area())
print(rectangle2.perimeter())
# ============================================================
# Task 9 — A Counter class
# ============================================================
# Create Counter with __init__(self, start=0), storing self.value.
# Assume start and amounts are integers. Add:
# add(amount): increase value by amount;
# reset(): set value to 0;
# get_value(): return value.
# Test Counter(10), add(3), add(-2): get_value() returns 11.
# After reset(), get_value() returns 0.
# Create Counter() and check that its initial value is 0.

# Write your code below:
class Counter:
    def __init__(self, start=0):
        self.value = start

    def add(self, amount):
        self.value = self.value + amount

    def reset(self):
        self.value = 0

    def get_value(self):
        return self.value


counter1 = Counter(10)

counter1.add(3)
counter1.add(-2)

print(counter1.get_value())

counter1.reset()

print(counter1.get_value())

counter2 = Counter()

print(counter2.get_value())

# ============================================================
# Task 10 — Independent Student objects
# ============================================================
# Create Student with __init__(self, name).
# Store self.name and create self.scores = [] INSIDE __init__.
# Add add_score(score), which appends an integer score (assume valid input).
# Create Anna and Omar. Add 80 and 90 to Anna only.
# Print both scores lists. Expected:
# [80, 90]
# []
# Do not define scores as a class attribute.

# Write your code below:
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)


anna = Student("Anna")
omar = Student("Omar")

anna.add_score(80)
anna.add_score(90)

print(anna.scores)
print(omar.scores)

# ============================================================
# Task 11 — A Student class with validation
# ============================================================
# Create ValidatedStudent with name and scores instance attributes.
# Add add_score(score). Assume score is an integer.
# Accept scores from 0 to 100 inclusive. For other values, raise
# ValueError("Score must be between 0 and 100") BEFORE modifying the list.
# Try to add [80, -1, 100, 101] to Anna, catching ValueError at each call.
# Print "Rejected: N" for each rejected score.
# Finally print the scores list. Expected:
# Rejected: -1
# Rejected: 101
# [80, 100]
# Create a separate class; inheritance is not needed.

# Write your code below:

class ValidatedStudent:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")

        self.scores.append(score)


anna = ValidatedStudent("Anna")

for score in [80, -1, 100, 101]:
    try:
        anna.add_score(score)
    except ValueError:
        print("Rejected:", score)

print(anna.scores)
# ============================================================
# Task 12 — Average and empty data
# ============================================================
# Create StudentReport with name and scores instance attributes.
# Implement add_score(score) with the validation from Task 11.
# Add average(): return the average of scores. If the list is empty,
# raise ValueError("No scores recorded").
# Create Anna, add 80 and 90, and print her average: 85.0.
# Create Omar without scores. Call average() inside try/except and print
# the message: No scores recorded.
# Do not return 0 for an empty list: 0 can be a real average.

# Write your code below:
class StudentReport:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")

        self.scores.append(score)

    def average(self):
        if len(self.scores) == 0:
            raise ValueError("No scores recorded")

        return sum(self.scores) / len(self.scores)


anna = StudentReport("Anna")

anna.add_score(80)
anna.add_score(90)

print(anna.average())


omar = StudentReport("Omar")

try:
    print(omar.average())
except ValueError as error:
    print(error)

# ============================================================
# Task 13 — BONUS: Skip invalid file records
# ============================================================
# Read data/mixed_scores.txt one line at a time using with.
# Skip blank lines. Convert each nonblank line to int and validate it
# with validate_score() from Task 4. Catch ValueError INSIDE the loop.
# Print "Rejected: TEXT" for invalid text or out-of-range integers.
# Append accepted scores to a list. Print the list and its average.
# Expected rejected values (in order): bad, 105, -2.
# Expected accepted list: [80, 100, 60]. Expected average: 80.0.
# Also handle FileNotFoundError around opening/reading the file.

# Write your code below:
scores = []

try:
    with open(DATA / "mixed_scores.txt", "r", encoding="utf-8") as file:
        for line in file:
            text = line.strip()

            if text == "":
                continue

            try:
                score = int(text)
                score = validate_score(score)
                scores.append(score)
            except ValueError:
                print("Rejected:", text)

except FileNotFoundError:
    print("File not found")

if scores:
    print(scores)
    print(sum(scores) / len(scores))

# ============================================================
# Task 14 — BONUS: Objects from a text file
# ============================================================
# Use StudentReport from Task 12. Read data/student_scores.txt.
# Each nonblank line is NAME,SCORE, with exactly one comma and a nonempty
# name. These formatting rules are guaranteed for the supplied file.
# Split the line, strip both fields, convert SCORE to int, and call
# add_score(). Keep one StudentReport per name in a dictionary.
# Skip invalid scores, printing "Rejected: NAME,SCORE". Create an object
# only after conversion and validation succeed.
# Finally print each student's average to one decimal place in first
# accepted appearance order. Expected:
# Rejected: Anna,bad
# Rejected: Omar,101
# Anna: 85.0
# Omar: 70.0
# Use only dictionaries, loops, functions, classes, and exceptions.
# Handle FileNotFoundError. Do not use inheritance or external packages.

# Write your code below:
students = {}

try:
    with open(DATA / "student_scores.txt", "r", encoding="utf-8") as file:
        for line in file:
            text = line.strip()

            if text == "":
                continue

            name, score_text = text.split(",")

            name = name.strip()
            score_text = score_text.strip()

            try:
                score = int(score_text)

                if not 0 <= score <= 100:
                    raise ValueError("Score must be between 0 and 100")

                if name not in students:
                    students[name] = StudentReport(name)

                students[name].add_score(score)

            except ValueError:
                print("Rejected:", text)

except FileNotFoundError:
    print("File not found")


for name, student in students.items():
    print(f"{name}: {student.average():.1f}")