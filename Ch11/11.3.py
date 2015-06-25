"""
Exercise 11.3. Dictionaries have a method called keys that returns the keys of the dictionary, in no particular order, as a list.
Modify print_hist to print the keys and their values in alphabetical order.
"""

def histogram(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = 1 + dictionary.get(letter, 0) # adds letter to dictionary; updates counter if letter already exists in dictionary
    return dictionary

def print_hist(histogram):
    histList = histogram.keys() # creates a list of keys within the dictionary
    histList.sort() # sorts in alphabetical order
    for letter in histList:
        print letter, histogram[letter] # print letter and values

h = histogram('banana')
print_hist(h)
