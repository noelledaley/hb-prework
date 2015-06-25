"""
The following functions are all intended to check whether a string contains any lowercase letters, but at least some of them are wrong. For each function, describe what the function actually does (assuming that the parameter is a string).
"""
# Number 1
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False  # This loop returns before traversing all characters resulting in false negatives
            # eg 'HELLo' returns False because the first letter is uppercase.

# Number 2
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():  # Checks if the string 'c' is lowercase, instead of the variable c
            return 'True'
        else:
            return 'False'

# Number 3
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag  # This will return whether the last letter in a string is lowercase.

# Number 4
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()  # This function performs as expected. 'flag' is set to False by default and it
# will remain False for every c in s that fails c.islower(). The first time
# that comes across a lowercase letter the condition 'flag' becomes:
# False or True which results in 'flag' being set to True. Once 'flag' is
# reassigned, no lower- or uppercase letter can change 'flag' back to False.
    return flag

# Number 5
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print any_lowercase5('hEllo')
print any_lowercase5('HEllo')
print any_lowercase5('hellO')
print any_lowercase5('HELLO')
