"""
Modify find so that it has a third parameter, the index in word where it should start looking.
"""

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print find('banjo', 'n', 1)
print find('banjo', 'n', 4)
print find('treehouse', 'n', 1)
print find('banana', 'n', 1)
