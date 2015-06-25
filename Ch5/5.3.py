"""
Write a function named check_fermat that takes four parameters: a, b, c and n and that checks to see if Fermats theorem holds.
"""

def check_fermat(a, b, c, n):
    if n > 2 and a**n + a**n == c**n:
        print 'Holy smokes, Fermat was wrong!'
    else:
        print 'No, that does not work.'

print check_fermat(1, 2, 3, 5)
print check_fermat(5, 54, 0, 2)

"""
Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermats theorem.
"""

a = int(raw_input('Please enter a value for A. '))
b = int(raw_input('Please enter a value for B. '))
c = int(raw_input('Please enter a value for C. '))
n = int(raw_input('Please enter a value for N. '))

print check_fermat(a, b, c, n)
