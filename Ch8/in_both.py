# the following function prints all the letters from word1 that 
# also appear in word2:

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print letter

in_both('noelle', 'elephant')
