"""
Exercise 10.7. Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram that takes two strings and returns True if they are anagrams.
"""

def is_anagram(string1, string2):
    letters1 = list(string1)  # convert both strings to lists
    letters2 = list(string2)
    return sorted(letters1) == sorted(letters2)  # sort & compare

print is_anagram('new relic', 'lew cirne')
print is_anagram('banjo', 'guitar')
