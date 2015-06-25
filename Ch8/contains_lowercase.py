# Exercise 8.11. The following functions are all intended to check whether a
# string contains any lowercase letters, but at least some of them are
# wrong. For each function, describe what the function actually does (assuming
# that the parameter is a string).


def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


# ^ The problem with the above function is that it returns true or false based purely on the 1st letter in the string.
# That is, the loop doesn't finish traversing the word before it returns, which is why line 18 returns False when it is in fact True.


def any_lowercase2(s):
	for c in s:
		if 'c'.islower():
			return 'True'


# ^ Line 20 treats 'c' as a string instead of a parameter, meaning it's checking if 'c' contains a lowercase instead of 'hello'.


def any_lowercase3(s):
	for c in s:
		flag = c.islower()
	return flag


# ^ In the case of WHaT, this function would return False the first time around, then False, then True, but then back to False before exiting the loop. Effectively it checks whether the last letter in a word is lower case.


def any_lowercase4(s):
	flag = False
	for c in s:
		print c
		flag = flag or c.islower()
	return flag


# This function performs as expected. 'flag' is set to False by default and it 
# will remain False for every c in s that fails c.islower(). The first time 
# that comes across a lowercase letter the condition 'flag' becomes:
# False or True which results in 'flag' being set to True. Once 'flag' is 
# reassigned, no lower- or uppercase letter can change 'flag' back to False.


def test_fourx(f):
	print f('hello')
	print f('HELLO')
	print f('hELLo')
	print f('HellO')

test_fourx(any_lowercase4)