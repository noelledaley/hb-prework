# The following function takes a dicitonary and inverts the keys and values.

def invert_dict(d):
    inverse = ()  # create empty list
    for key in d:  # traverse through keys in dictionary
        val = d[key]  # create a new variable for each key storing the key's value
        if val not in inverse:
            inverse[val] = [key]  # if the value isn't already in inverse, add a new item as a singular list
        else:
            inverse[val].append(key) # if the value is already in inverse, add the key to the list of keys that point to the value
    return inverse
