"""
Write a function called do_n takes a function object and a number, n, as arguments, and that calls the given function n times.
"""

def do_n(f, n):
    if n <= 0:
        return
    f()
    do_n(f, n-1)

def print_hi():
    print 'Hi! '

print do_n(print_hi, 5)
