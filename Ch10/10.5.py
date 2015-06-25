"""
Exercise 10.5. Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None.
"""
example = [5, 4, 3, 2, 1]

def chop(l):
    del l[:1]  # deletes 1st element
    del l[-1:]  # deletes last element

print chop(example)
