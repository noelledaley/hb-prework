""" Exercise 1
Write a function that takes a string as an argument and displays the letters backward, one per line.
"""

def print_backwards(word):
    index = len(word)
    while index > 0:
        print word[index - 1]
        index = index - 1

print_backwards('banjo')

"""
Exercise 2
Modify the program to fix the typos.
"""

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print letter + 'u' + suffix
    else:
        print letter + suffix
