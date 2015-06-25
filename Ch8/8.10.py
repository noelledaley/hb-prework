"""
A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.
Use this idiom to write a one-line version of is_palindrome from Exercise 6.
"""
def is_palindrome(word):
    return word == word[::-1]

print is_palindrome('hello')
print is_palindrome('racecar')
