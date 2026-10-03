"""NSU Python — Lab 08
Working with Text Files

Complete Tasks 1–12. Tasks 13–14 are optional bonus tasks.
Use only concepts from Lecture 08 and earlier lectures.
Run each task with your own extra test values.
"""

from pathlib import Path

LAB_DIR = Path(__file__).resolve().parent
DATA = LAB_DIR / "data"
OUTPUT = LAB_DIR / "output"

# ============================================================
# Task 1 — Read a whole file
# ============================================================
# Read data/note.txt with UTF-8 using with and read(). Print the content,
# then print the number of characters. Resolve paths relative to this
# script.
path = DATA / "note.txt"

with open(path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
print(len(content))
# Write your code below:


# ============================================================
# Task 2 — Read two lines
# ============================================================
# Open data/note.txt and call readline() twice. Print repr() of each line
# so the newline character is visible.

# Write your code below:

path = DATA / "note.txt"

with open(path, "r", encoding="utf-8") as file:
    line1 = file.readline()
    line2 = file.readline()

print(repr(line1))
print(repr(line2))
# ============================================================
# Task 3 — Read lines into a list
# ============================================================
# Use readlines() on data/names.txt. Print the number of lines and the
# last name without a trailing newline.
path = DATA / "names.txt"

with open(path, "r", encoding="utf-8") as file:
    lines = file.readlines()

print(len(lines))
print(lines[-1].strip())
# Write your code below:


# ============================================================
# Task 4 — Count nonblank lines
# ============================================================
# Iterate over data/names.txt and count lines whose strip() result is
# nonempty. Print the count. Do not use read() or readlines() for this
# task.

# Write your code below:
count = 0

with open(DATA / "names.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            count += 1

print(count)

# ============================================================
# Task 5 — Write a report
# ============================================================
# Create output/name_report.txt in w mode. Read data/names.txt, count
# nonblank names, and write exactly "Names: N" followed by a newline. The
# output directory already exists.

# Write your code below:

count = 0

with open(DATA / "names.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            count += 1

with open(OUTPUT / "name_report.txt", "w", encoding="utf-8") as file:
    file.write(f"Names: {count}\n")
# ============================================================
# Task 6 — Append a log entry
# ============================================================
# Append "Lab 08 completed" and a newline to output/activity.log. Running
# this task twice should create two entries. Open with a mode.

# Write your code below:
with open(OUTPUT / "activity.log", "a", encoding="utf-8") as file:
    file.write("Lab 08 completed\n")

# ============================================================
# Task 7 — Create without overwriting
# ============================================================
# Create output/first_run.txt with x mode and write "First run". Catch
# FileExistsError and print a clear message on later runs.

# Write your code below:
try:
    with open(OUTPUT / "first_run.txt", "x", encoding="utf-8") as file:
        file.write("First run")
except FileExistsError:
    print("first_run.txt already exists")

# ============================================================
# Task 8 — Handle a missing file
# ============================================================
# Try to read data/missing.txt. Catch FileNotFoundError and print "Input
# file not found". Do not create the missing file.

# Write your code below:

try:
    with open(DATA / "missing.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Input file not found")
# ============================================================
# Task 9 — Filter names to a new file
# ============================================================
# Read data/names.txt one line at a time. Write nonblank names that begin
# with A or a into output/a_names.txt, one name per line. Strip extra
# spaces.

# Write your code below:

with open(DATA / "names.txt", "r", encoding="utf-8") as input_file:
    with open(OUTPUT / "a_names.txt", "w", encoding="utf-8") as output_file:
        for line in input_file:
            name = line.strip()

            if name and name[0].lower() == "a":
                output_file.write(name + "\n")
# ============================================================
# Task 10 — Average from a file
# ============================================================
# data/scores.txt contains one integer per nonblank line. Calculate the
# average and write "Average: 83.0" (one decimal place) into
# output/average.txt. Handle an empty list of scores without dividing by
# zero.

# Write your code below:
scores = []

with open(DATA / "scores.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line:
            scores.append(int(line))

with open(OUTPUT / "average.txt", "w", encoding="utf-8") as file:
    if scores:
        average = sum(scores) / len(scores)
        file.write(f"Average: {average:.1f}\n")
    else:
        file.write("Average: 0.0\n")

# ============================================================
# Task 11 — Read a simple table
# ============================================================
# Each nonblank line of data/students.csv is name,score. Assume no header
# and no commas inside names. Print only students with a score of at least
# 80, with the score converted to int.

# Write your code below:

with open(DATA / "students.csv", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line:
            name, score = line.split(",")
            score = int(score)

            if score >= 80:
                print(name, score)
# ============================================================
# Task 12 — Save a word count
# ============================================================
# Read data/note.txt, use split() to count words, and write "Words: N"
# with a newline to output/word_count.txt.

# Write your code below:

with open(DATA / "note.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()

with open(OUTPUT / "word_count.txt", "w", encoding="utf-8") as file:
    file.write(f"Words: {len(words)}\n")
# ============================================================
# Task 13 — BONUS: Clean nonblank lines
# ============================================================
# Copy data/names.txt to output/clean_names.txt, removing blank lines and
# spaces at the ends of names. Keep the original order.

# Write your code below:
with open(DATA / "names.txt", "r", encoding="utf-8") as input_file:
    with open(OUTPUT / "clean_names.txt", "w", encoding="utf-8") as output_file:
        for line in input_file:
            name = line.strip()

            if name:
                output_file.write(name + "\n")

# ============================================================
# Task 14 — BONUS: File and regex
# ============================================================
# Read data/note.txt and use re.findall(r"[0-9]+", text) to extract all
# digit sequences. Write them one per line to output/numbers.txt.

# Write your code below:

import re

with open(DATA / "note.txt", "r", encoding="utf-8") as file:
    text = file.read()

numbers = re.findall(r"[0-9]+", text)

with open(OUTPUT / "numbers.txt", "w", encoding="utf-8") as file:
    for number in numbers:
        file.write(number + "\n")

