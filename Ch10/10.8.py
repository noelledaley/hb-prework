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
example2 = [5, 9, 2, 1]
example3 = [1, 2, 3, 4, 4, 5, 6, 6]

print has_duplicates(example)
print has_duplicates(example2)
print has_duplicates(example3)

"""
Part 2: If there are 23 students in your class, what are the chances that two of you have the same birthday? You can estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can generate random birthdays with the randint function in the random module.
"""

import random

number_of_students = 23
trials = 1000

def generate_birthdays():
    birthdays = []  # create empty list of birthdays
    i = 0
    while i < number_of_students:
        date = random.randint(1, 365)  # generate 23 random values between 1 - 265 days, since there are 365 days in a year
        birthdays.append(date)
        i += 1
    return birthdays

def calculate_stats(trials):
    i = 0
    duplicates = 0
    for i in range(trials):
        if has_duplicates(generate_birthdays()):
            duplicates += 1
    print "In %s classrooms with %s students, %s%% had duplicate birthdays" % (trials, number_of_students, (float(duplicates)/trials) * 100)

print calculate_stats(trials)
