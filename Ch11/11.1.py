"""
Exercise 11.1. Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesnt matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""

englishdict = dict()

fin = open('words.txt')
line = fin.readline()

def eng_words_dict(fin):
    for line in fin:
        word = line.strip()
        englishdict[word] = 'test'
    return englishdict

eng_words_dict(fin)

print 'HELLO' in englishdict
print 'ZYNGA' in englishdict
