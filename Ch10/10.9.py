"""
Exercise 10.9. Write a function called remove_duplicates that takes a list and returns a new list with only the unique elements from the original. Hint: they dont have to be in the same order.
"""

example = [1, 5, 5, 9, 3]
example2 = [3, 5, 10, 2]

def remove_duplicates(t):
    new_list = []
    for i in t:
        if i not in new_list:
            new_list.append(i)
    return new_list

print remove_duplicates(example)
print remove_duplicates(example2)
