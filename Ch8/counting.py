#  The following program counts the number of times the letter
#  a appears in a string:


def count(word, letter):
    count = 0
    for i in word:
        if i == letter:
            count = count + 1
    return count


count('noelle', 'l')
count('alphabet', 'z')

# Rewrite this function so that instead of traversing the string,
# it uses the three- parameter version of find from the previous section


def find_count(word, letter, i):
    count = 0
    while i < len(word):
        if word[i] == letter:
            count = count + 1
        i = i + 1
    return count

find_count('elephante', 'e', 1)
