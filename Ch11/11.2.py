"""
Exercise 11.2. Dictionaries have a method called get that takes a key and a default value. If the key appears in the dictionary, get returns the corresponding value; otherwise it returns the default value.

Use get to write histogram more concisely. You should be able to eliminate the if statement.
"""

def histogram(s):
    d = dict()
    for c in s:
        # dict.get(key to be searched, default=None value to return if key isn't found)
        d[c] = 1 + d.get(c, 0)  # adds new character to dictionary, or if the character already exists, updates counter
    return d

print histogram('banana')
