# Name: Paul Korver
# Section:
# strings_and_lists.py

# **********  Exercise 2.7 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
    # number_list is a list of numbers

    x = 0
    for num in number_list:
        if(x > 0):
            number_list[x] = number_list[x] + number_list[x-1]
        x = x + 1
    return number_list


# Test Cases
print "cumulative_sum of [4, 3, 6] is:", cumulative_sum([4, 3, 6])
print "cumulative_sum of [1, 2, 3, 4] is:", cumulative_sum([1, 2, 3, 4])

# **********  Exercise 2.8 **********

#def report_card():
    ##### YOUR CODE HERE #####
    

# Test Cases
## In comments, show the output of one run of your function.

# **********  Exercise 2.9 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin
    if(word[0] in VOWELS):
        return word + "hay"
    else : return word[1:] + word[0] + "ay"
    

# Test Cases
print "Pig latin for apple is:",pig_latin("apple")
print "Pig latin for string is:",pig_latin("string")
print "Pig latin for my name is:",pig_latin("Paul")


# **********  Exercise 2.10 **********

cubes = [x**3 for x in range(11)]

def coinflip():
    coinflip = ["ht", "tl"]
    for result in coinflip:
        print result + "ht"
        print result + "tl"

def vowels(word):
    for letter in word:
        if(letter in VOWELS):
            word = word
        else:
            word = word.remove(letter)
    return word

# Test Cases
print cubes
print coinflip()

# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 
