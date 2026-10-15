"""NSU Python — Lab 10
Object-Oriented Programming

Main tasks: 1–12. Course minimum: at least 10 main tasks.
Aim to complete all 12. Tasks 13–14 are optional bonuses.
Use Lecture 10 and earlier concepts. No external packages are needed.
Tasks 7–10 and 12–14 reuse classes defined in earlier tasks.
"""
from pathlib import Path

LAB_DIR = Path(__file__).resolve().parent
OUTPUT = LAB_DIR / "output"


# ============================================================
# Task 1 — Instance and class attributes
# ============================================================
# Create Student with class attribute university = "NSU".
# __init__(name) must store name as an instance attribute.
# Create Anna and Omar. Print each name and university.
# Then set Student.university = "NSU Updated" and print both universities.
# Expected universities after the change: NSU Updated, NSU Updated.
# Do not assign self.university inside __init__.

# Write your code below:


class Student:
   university = "NSU" 
    #university = "Novosibirsk State University"   

   def __init__(self, name):
        self.name = name


Anna = Student("Anna")
Omar = Student("Omar")

print(Anna.name, Anna.university)
print(Omar.name, Omar.university)

Student.university = "NSU Updated"

print(Anna.university)
print(Omar.university)

# ============================================================
# Task 2 — Shadow a class attribute
# ============================================================
# Create Device with class attribute category = "General" and an instance
# attribute name set in __init__. Create a = Device("Laptop") and
# b = Device("Printer"). Set a.category = "Personal" and then
# Device.category = "Shared".
# Print a.category, b.category, and Device.category on separate lines.
# Expected: Personal, Shared, Shared.
# Add a comment explaining why a differs from b.

# Write your code below:



class Device:
    category = "General"  

    def __init__(self, name):
        self.name = name  


a = Device("Laptop")
b = Device("Printer")

a.category = "Personal"  
Device.category = "Shared"  

print(a.category)
print(b.category)
print(Device.category)


# ============================================================
# Task 3 — Fix shared mutable state
# ============================================================
# The following design accidentally shares one list:
# class Team:
#     members = []
#     def __init__(self, name):
#         self.name = name
#     def add_member(self, name):
#         self.members.append(name)
# Fix Team so each instance has its own members list.
# Create Alpha and Beta. Add Anna to Alpha only.
# Print both lists and whether they are the same object.
# Expected: ['Anna'], [], False (one result per line).

# Write your code below:



class Team:
    def __init__(self, name):
        self.name = name
        self.members = []  

    def add_member(self, name):
        self.members.append(name)


# Create two teams
Alpha = Team("Alpha")
Beta = Team("Beta")


Alpha.add_member("Anna")


print(Alpha.members)
print(Beta.members)


print(Alpha.members is Beta.members)


# ============================================================
# Task 4 — Encapsulation and validation
# ============================================================
# Create PositiveCounter with self._value = 0 in __init__.
# add(amount) accepts a positive integer and increases _value.
# Reject zero and negative integers with ValueError("Amount must be positive")
# before changing state. get_value() returns the current value.
# Assume arguments are integers. Use only these public methods in the demo.
# Add 3 and 2, then attempt to add 0 inside try/except.
# Print the value before and after the rejected update: both must be 5.
# Add a comment: the leading underscore is a convention, not enforced privacy.

# Write your code below:



class PositiveCounter:
    def __init__(self):
        self._value = 0

    
    def add(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._value += amount

    def get_value(self):
        return self._value



counter = PositiveCounter()

# Add positive amounts
counter.add(3)
counter.add(2)


print(counter.get_value())


try:
    counter.add(0)
except ValueError as error:
    print(error)


print(counter.get_value())


# ============================================================
# Task 5 — Return a copy of internal data
# ============================================================
# Create ScoreBook with self._scores = [] inside __init__.
# add_score(score) accepts integer scores from 0 to 100 inclusive.
# Otherwise raise ValueError("Score must be between 0 and 100").
# get_scores() must return a COPY of the internal list.
# Add 80. Store snapshot = book.get_scores(), then append 100 to snapshot.
# Print snapshot and book.get_scores(). Expected: [80, 100] and [80].
# Create a second ScoreBook and verify its scores remain empty.

# Write your code below:

class ScoreBook:
    def __init__(self):
        self._scores = []

    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self._scores.append(score)

    def get_scores(self):
        return self._scores.copy()



book = ScoreBook()
book.add_score(80)


snapshot = book.get_scores()
snapshot.append(100)


print(snapshot)
print(book.get_scores())


book2 = ScoreBook()
print(book2.get_scores())


# ============================================================
# Task 6 — Inherit a method
# ============================================================
# Create Person with __init__(name) and describe(), returning
# "Person: NAME". Create Visitor(Person) with an empty body using pass.
# Create Visitor("Omar") and print its description: Person: Omar.
# Also print isinstance(visitor, Visitor), isinstance(visitor, Person),
# and issubclass(Visitor, Person). All three must be True.
# Do not redefine __init__ or describe inside Visitor.

# Write your code below:
class Person:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Person: {self.name}"


class Visitor(Person):
    pass


visitor = Visitor("Omar")

print(visitor.describe())
print(isinstance(visitor, Visitor))
print(isinstance(visitor, Person))
print(issubclass(Visitor, Person))

# ============================================================
# Task 7 — Initialize a subclass with super
# ============================================================
# Using Person from Task 6, create StudentPerson(Person).
# __init__(name, program) must call super().__init__(name), then store program.
# Create StudentPerson("Anna", "AI"). Print name, program, and describe().
# Expected: Anna, AI, Person: Anna (one result per line).
# Do not duplicate the assignment to self.name in the subclass.

# Write your code below:
class StudentPerson(Person):
    def __init__(self, name, program):
        super().__init__(name)
        self.program = program


student = StudentPerson("Anna", "AI")

print(student.name)
print(student.program)
print(student.describe())

# ============================================================
# Task 8 — Override a method
# ============================================================
# Using Person, create Teacher(Person). Its __init__(name, subject) calls
# the parent initializer and stores subject.
# Override describe() to return "Teacher: NAME, subject: SUBJECT".
# Print Teacher("Mira", "Python").describe().
# Expected: Teacher: Mira, subject: Python.
# Then print Person("Omar").describe(): Person: Omar.
# The Person implementation must remain unchanged.

# Write your code below:
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def describe(self):
        return f"Teacher: {self.name}, subject: {self.subject}"


teacher = Teacher("Mira", "Python")

print(teacher.describe())
print(Person("Omar").describe())

# ============================================================
# Task 9 — Extend an inherited method
# ============================================================
# Create DetailedStudent(StudentPerson).
# Inherit __init__ unchanged. Override describe() by calling
# super().describe(), then appending ", program: PROGRAM".
# For DetailedStudent("Anna", "AI"), the result must be:
# Person: Anna, program: AI.
# Return a string; do not print inside describe().

# Write your code below:

class DetailedStudent(StudentPerson):
    def describe(self):
        return f"{super().describe()}, program: {self.program}"


student = DetailedStudent("Anna", "AI")

print(student.describe())
# ============================================================
# Task 10 — Polymorphic descriptions
# ============================================================
# Create a list containing Person("Omar"), Teacher("Mira", "Python"),
# and DetailedStudent("Anna", "AI") from Tasks 6–9.
# Use ONE for loop to call describe() and print each result.
# Expected:
# Person: Omar
# Teacher: Mira, subject: Python
# Person: Anna, program: AI
# Do not use type(), isinstance(), or if/elif to choose a description.

# Write your code below:

people = [
    Person("Omar"),
    Teacher("Mira", "Python"),
    DetailedStudent("Anna", "AI")
]

for person in people:
    print(person.describe())
# ============================================================
# Task 11 — Duck typing with shapes
# ============================================================
# Create unrelated Rectangle and Square classes (no custom common parent).
# Rectangle(width, height).area() returns width * height.
# Square(side).area() returns side * side. Assume positive numeric dimensions.
# Define total_area(shapes), which sums shape.area() in a loop and returns it.
# For [Rectangle(3, 4), Square(5)], print 37.
# For an empty list, print 0. Do not branch on the shape's type.

# Write your code below:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


def total_area(shapes):
    total = 0

    for shape in shapes:
        total += shape.area()

    return total


print(total_area([Rectangle(3, 4), Square(5)]))
print(total_area([]))
# ============================================================
# Task 12 — Composition: a course roster
# ============================================================
# Create Course with title and an independent self.students list.
# enroll(person) appends the supplied object. Assume it supports describe().
# roster() returns a list of the enrolled objects' describe() results.
# Enroll Teacher("Mira", "Python") and DetailedStudent("Anna", "AI").
# Print each roster string in enrollment order:
# Teacher: Mira, subject: Python
# Person: Anna, program: AI
# Create a second course and verify its roster() returns [].
# Course contains objects; it must not inherit from Person or StudentPerson.

# Write your code below:

class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def enroll(self, person):
        self.students.append(person)

    def roster(self):
        return [person.describe() for person in self.students]


course = Course("Python Programming")

course.enroll(Teacher("Mira", "Python"))
course.enroll(DetailedStudent("Anna", "AI"))

for description in course.roster():
    print(description)


second_course = Course("Mathematics")
print(second_course.roster())
# ============================================================
# Task 13 — BONUS: a further subclass
# ============================================================
# Create ResearchStudent(DetailedStudent) with __init__(name, program, thesis).
# Call super().__init__(name, program), then store thesis.
# Override describe() by extending super().describe() with ", thesis: THESIS".
# ResearchStudent("Anna", "AI", "XAI").describe() must return:
# Person: Anna, program: AI, thesis: XAI.
# Enroll this object in Course from Task 12. Its roster must use the new
# description without changes to Course.

# Write your code below:
class ResearchStudent(DetailedStudent):
    def __init__(self, name, program, thesis):
        super().__init__(name, program)
        self.thesis = thesis

    def describe(self):
        return f"{super().describe()}, thesis: {self.thesis}"


researcher = ResearchStudent("Anna", "AI", "XAI")

print(researcher.describe())

# ============================================================
# Task 14 — BONUS: save the roster
# ============================================================
# Define save_roster(course, path). Use course.roster() and write one
# returned description per line using with, mode "w", and UTF-8.
# Use the Course from Task 12. Save to OUTPUT / "roster.txt".
# At the call site, catch OSError and print "Cannot save roster" on failure.
# Print "Roster saved" only on success. Do not catch unrelated exceptions.
# The supplied output/ directory already exists. Do not create other folders.
# Also test OUTPUT / "missing_folder" / "roster.txt"; it should fail while
# missing_folder does not exist. Do not create that folder.
# Repeated successful runs should replace roster.txt, not append duplicates.

# Write your code below:
from pathlib import Path


def save_roster(course, path):
    with open(path, "w", encoding="utf-8") as file:
        for description in course.roster():
            file.write(description + "\n")


OUTPUT = Path("output")

# Save to the existing output directory.
try:
    save_roster(course, OUTPUT / "roster.txt")
except OSError:
    print("Cannot save roster")
else:
    print("Roster saved")


# Test a path whose parent directory does not exist.
try:
    save_roster(course, OUTPUT / "missing_folder" / "roster.txt")
except OSError:
    print("Cannot save roster")
else:
    print("Roster saved")