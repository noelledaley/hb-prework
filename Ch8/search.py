def find(word, letter):
    index = 0
    while index < len(word):  # scan through the word
        if word[index] == letter:  # when you encounter the letter, return
            return index
        index = index + 1
    return -1

find('noelle', 'e')
