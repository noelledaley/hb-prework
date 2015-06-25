"""
Write a function named is_triangle that takes three integers as arguments, and that prints either Yes or No depending on whether you can or cannot form a triangle from sticks with the given lengths.
"""

def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print 'No, you cannot make a triangle'
    else:
        print 'Yes, you can make a triangle'

print is_triangle(3, 4, 5)
print is_triangle(10, 2, 3)

"""
Write a function that prompts the user to input three stick lengths, converts them to integers, and uses is_triangle to check whether sticks with the given lengths can form a triangle.
"""

a = int(raw_input('Please enter a value for A: '))
b = int(raw_input('Please enter a value for B: '))
c = int(raw_input('Please enter a value for C: '))

print is_triangle(a, b, c)
