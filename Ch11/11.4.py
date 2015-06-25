"""
Exercise 11.4. Modify reverse_lookup so that it builds and returns a list of all keys that map to v, or an empty list if there are none.
"""

eng2span = {'hello':'hola', 'hi':'hola'}
numbers = {'one':'I', 'two':'II', 'three':'III'}

def reverse_lookup(dict, val):
    all_keys = [] # create empty list
    empty_keys = []
    for ky in dict:
        if dict[ky] == val:
            all_keys.append(ky)
    if len(all_keys) > 1:  # only print this list if one of the values occurs more than once
        return all_keys
    return empty_keys

print reverse_lookup(eng2span, 'hola')
print reverse_lookup(numbers, 'I')
