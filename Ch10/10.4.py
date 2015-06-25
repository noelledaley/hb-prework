"""
Exercise 10.4. Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. So middle([1,2,3,4]) should return [2,3].
"""

example = [5, 4, 3, 2, 1]

def select_middle(l):
    return l[1:-1]

print select_middle(example)

# Alternate

def select_middle2(l):
    middle_list = []
    i = 1
    while i <= len(l) - 2:
            middle_list.append(l[i])
            i += 1
    return middle_list

print select_middle2(example)
