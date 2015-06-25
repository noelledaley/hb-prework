"""
Exercise 11.9 Use a dictionary to write a faster, simpler version of has_duplicates.
"""

ages = {25: "rosa", 23: "noelle", 25: "paul"}
ages2 = {"rosa": 25, "noelle": 23, "brittany": 24}

def has_duplicates(d):
    newdict= {}
    for ky in d:
        if ky in newdict:
            return True # return True if the key is already in the dictionary
        newdict[ky] = True # otherwise, add key to dictionary
    return False # return False if no duplicates are found

print has_duplicates(ages)
print has_duplicates(ages2)
