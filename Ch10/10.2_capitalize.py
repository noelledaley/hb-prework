# Write a function that capitalizes the first letter of every word in a list.

words = ['hi', 'hey', 'hello']

def capitalize_all(t):
    new = []
    for s in t:
        new.append(s.capitalize())
    return new

print capitalize_all(words)

"""
Exercise 10.2. Use capitalize_all to write a function named capitalize_nested that takes a nested list of strings and returns a new nested list with all strings capitalized.
"""
