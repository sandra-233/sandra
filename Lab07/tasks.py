"""NSU Python — Lab 07
Strings and Regular Expressions

Complete Tasks 1–12. Tasks 13–14 are optional bonus tasks.
Use only concepts from Lecture 07 and earlier lectures.
Run each task with your own extra test values.
"""

# ============================================================
# Task 1 — Clean a student name
# ============================================================
# Given raw = "  aLiCe SMITH  ", print "Alice Smith". Use strip() and a
# case method. Explain in a comment why the original raw value does not
# change.

# Write your code below:

raw = "  aLiCe SMITH  "

cleaned = raw.strip().title()

print(cleaned)

# Output: Alice Smith

# The original raw value does not change because strings are immutable.
# strip() and title() create a new string instead of modifying raw.
# ============================================================
# Task 2 — Extract a filename extension
# ============================================================
# Given filename = "final.report.pdf", print the text after the last dot.
# Then test "notes.txt". You may use split(). Assume a dot exists.

# Write your code below:
filename = "final.report.pdf"

extension = filename.split(".")[-1]

print(extension)

filename = "notes.txt"

extension = filename.split(".")[-1]

print(extension)


# ============================================================
# Task 3 — Split and join words
# ============================================================
# Given text = "  Python   files  are useful  ", create the list of words
# using split() and print the cleaned sentence with single spaces using
# join().

# Write your code below:

text = "  Python   files  are useful  "

words = text.split()
print(words)

cleaned_sentence = " ".join(words)
print(cleaned_sentence)

# ============================================================
# Task 4 — Count a substring
# ============================================================
# For text = "banana bandana", print how many times "ana" occurs using
# count(). Then print whether the text starts with "ban" and ends with
# "ana". count() uses non-overlapping matches.

# Write your code below:

text = "banana bandana"

print(text.count("ana"))
print(text.startswith("ban"))
print(text.endswith("ana"))
# ============================================================
# Task 5 — Find an optional separator
# ============================================================
# Write split_code(value). If value contains a hyphen, return the text
# before it. Otherwise return the whole value. Use find(), check for -1,
# and test "NS-205" and "NS205".

# Write your code below:

def split_code(value):
    position = value.find("-")

    if position != -1:
        return value[:position]
    else:
        return value


print(split_code("NS-205"))
print(split_code("NS205"))
# ============================================================
# Task 6 — Normalize a simple record
# ============================================================
# Given row = "  Anna , 82 , NSU  ", split on commas, strip each piece,
# and print "Anna | 82 | NSU". Assume no commas occur inside a field.

# Write your code below:
row = "  Anna , 82 , NSU  "

parts = row.split(",")

cleaned = [part.strip() for part in parts]

print(" | ".join(cleaned))

# ============================================================
# Task 7 — Find numbers in text
# ============================================================
# Import re. From "Rooms B-204, C-17, A-315", use re.findall() with a raw-
# string pattern to extract the digit sequences as strings. Convert them
# to integers and print both lists.

# Write your code below:
import re

text = "Rooms B-204, C-17, A-315"

digit_strings = re.findall(r"\d+", text)
numbers = [int(x) for x in digit_strings]

print(digit_strings)
print(numbers)


# ============================================================
# Task 8 — Check a student ID
# ============================================================
# Write is_valid_id(value). Return True only if the entire string has two
# uppercase ASCII letters, one hyphen, and exactly four ASCII digits. Use
# re.fullmatch(). Test "AB-2047", "A-2047", and "xAB-2047".

# Write your code below:
import re

def is_valid_id(value):
    return re.fullmatch(r"[A-Z]{2}-[0-9]{4}", value) is not None


print(is_valid_id("AB-2047"))
print(is_valid_id("A-2047"))
print(is_valid_id("xAB-2047"))

# ============================================================
# Task 9 — Compare three regex functions
# ============================================================
# With pattern r"[0-9]+" and text "Room 204", print Boolean results from
# re.search(), re.match(), and re.fullmatch(). Then repeat fullmatch()
# with "204". Add a comment explaining each result.

# Write your code below:
import re

pattern = r"[0-9]+"
text = "Room 204"

print(re.search(pattern, text) is not None)      # True: search finds 204 anywhere in the text
print(re.match(pattern, text) is not None)      # False: match looks only at the beginning, and text starts with "Room"
print(re.fullmatch(pattern, text) is not None)  # False: fullmatch requires the entire text to be digits

print(re.fullmatch(pattern, "204") is not None) # True: the entire string is digits

# ============================================================
# Task 10 — Extract candidate dates
# ============================================================
# From "Due 28/09/2026; revised 02/10/2026; invalid 99/99/2026", use
# findall() to extract all DD/MM/YYYY-shaped substrings. Explain why a
# match does not establish that a date exists.

# Write your code below:
import re

text = "Due 28/09/2026; revised 02/10/2026; invalid 99/99/2026"

dates = re.findall(r"\d{2}/\d{2}/\d{4}", text)

print(dates)

# The regex only checks the shape DD/MM/YYYY.
# It does not check whether the day and month are actually valid dates.

# ============================================================
# Task 11 — Find email-like tokens
# ============================================================
# From "Contact ada@example.com or bob.smith@nsu.ru", use findall() with
# [A-Za-z0-9._]+@[A-Za-z0-9.]+ to extract candidate addresses. State that
# this is a classroom pattern, not complete email validation.


# Write your code below:
import re

text = "Contact ada@example.com or bob.smith@nsu.ru"

emails = re.findall(r"[A-Za-z0-9._]+@[A-Za-z0-9.]+", text)

print(emails)

# This is a classroom pattern, not complete email validation.

# ============================================================
# Task 12 — Clean and select codes
# ============================================================
# Given values = [" ns-205 ", "AB-2047", "invalid", " xy-3001 "], strip
# and uppercase each value. Keep only valid IDs in the two-letter/four-
# digit format from Task 8. Print the resulting list.

# Write your code below:

import re

values = [" ns-205 ", "AB-2047", "invalid", " xy-3001 "]

cleaned = [value.strip().upper() for value in values]

valid_ids = [value for value in cleaned
             if re.fullmatch(r"[A-Z]{2}-[0-9]{4}", value)]

print(valid_ids)
# ============================================================
# Task 13 — BONUS: Words beginning with a capital
# ============================================================
# From "Alice met Bob in Novosibirsk", use findall() with a simple ASCII
# pattern to obtain words that begin with [A-Z]. Do not use capturing
# groups.

# Write your code below:

import re

text = "Alice met Bob in Novosibirsk"

words = re.findall(r"\b[A-Z][A-Za-z]*\b", text)

print(words)
# ============================================================
# Task 14 — BONUS: Two code formats
# ============================================================
# Accept either AA-123 or AA-1234 for the entire input. Use one regex with
# ?, re.fullmatch(), and test "NS-205", "NS-2047", and "N-205".

# Write your code below:
import re

pattern = r"[A-Z]{2}-[0-9]{3,4}"

print(re.fullmatch(pattern, "NS-205") is not None)
print(re.fullmatch(pattern, "NS-2047") is not None)
print(re.fullmatch(pattern, "N-205") is not None)

