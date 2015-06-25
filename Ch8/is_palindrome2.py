# Exercise 8.10. write a one-line version of is_palindrome

import pdb


def is_palindrome(word):
    i = 0
    j = len(word) - 1

    while i<j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j - 1
    return True

print is_palindrome('racecar')
print is_palindrome('hello')
