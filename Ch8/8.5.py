"""
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print count

Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
"""

def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    print count

count_letter('banana', 'a')
count_letter('banana', 't')

"""
Then Rewrite this function so that instead of traversing the string, it uses the three-parameter version of find from the previous section.
"""

def count2(word, letter, index):
    count = 0
    while index < len(word):
        if word[index] == letter:
            count = count + 1
        index = index + 1
    print count

count2('banana', 'a', 3)
count2('banana', 't', 0)
