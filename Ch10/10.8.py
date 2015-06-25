"""
Exercise 10.8 Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.
"""

def has_duplicates(t):
    new_list = []
    for i in t:
        if i in new_list:
            return True
        new_list.append(i)
    return False


example = [1, 2, 2, 5]
example2 = [5, 3, 2, 1]
example3 = [1, 2, 3, 4, 4, 5, 6, 6]

print has_duplicates(example)
print has_duplicates(example2)
print has_duplicates(example3)

"""
Part 2: If there are 23 students in your class, what are the chances that two of you have the same birthday? You can estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can generate random birthdays with the randint function in the random module.
"""

import random

def generate_birthdays():
    birthdays = []  # create empty list of birthdays
    i = 0
    while i < 265:
        # import pdb; pdb.set_trace()

        date = random.randint(1, 265)  # generate 20 random values between 1 - 265 days, since there are 265 days in a year
        birthdays.append(date)
        i += 1
    return birthdays

birthdays = generate_birthdays()
count = 0
total = 0

for i in birthdays:
    if i in birthdays:
        count += 1
        total += 1
    else:
        total += 1

print (float(count) / float(total)) * 100.0
