# Write a function that takes a string as an argument and displays
# the letters backward, one per line.


def backwards(word):
    index = len(word)
    while index > 0:
        print word[index - 1]
        index = index - 1

backwards('hello')
