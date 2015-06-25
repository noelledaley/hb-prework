number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]


# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    new_list = []
    for num in number_list:
        if num % 2 != 0:
            new_list.append(num)
    return new_list


# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    new_list2 = []
    for num in number_list:
        if num % 2 == 0:
            new_list2.append(num)
    return new_list2


# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):
    four_ormore = []
    for word in word_list:
        if len(word) > 4:
            four_ormore.append(word)
    return four_ormore


# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    find_small = number_list.sort()
    return number_list[0]


# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    find_large = number_list.sort()
    return number_list[len(number_list) - 1]


# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    half_list = []
    for num in number_list:
        num = num / 2.0
        half_list.append(num)
    return half_list



# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    str_lengths = []
    for word in word_list:
        str_lengths.append(len(word))
    return []


# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    sum = 0
    for num in number_list:
        sum = sum + num
    return sum


# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    total = 0
    for num in number_list:
        total = total * num
    return 0


# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    phrase = ""
    for word in word_list:
        phrase = phrase + " " + word
    return phrase


# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    # import pdb; pdb.set_trace()
    avg = sum_numbers(number_list) / len(number_list)
    return avg

print average(number_list)
