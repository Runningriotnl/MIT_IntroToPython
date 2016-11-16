# Name: Paul Korver
# Section:
# hw2.py

import math

##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 ********** 

def f1(x):
    print x + 1

def f2(x):
    return x + 1

# **********  Exercise 2.1 ********** 

# Define your function here

# Simple if elif else rock paper siccors program

def rps(player_one, player_two):
#    player_one = raw_input("Player one please choose: ")
#    player_two = raw_input("Player two please choose: ")

    while(player_one != "Stone" and player_one != "Scissors" and player_one != "Paper"):
        player_one = raw_input("Player one please choose: Stone, Scissors or Paper: ")
   
    while(player_two != "Stone" and player_two != "Scissors" and player_two != "Paper"):
        player_two = raw_input("Player two lease choose: Stone, Scissors or Paper: ")

    if(player_one == "Stone"):
        if(player_two == "Stone"):
            return "It's a tie."
        elif(player_two == "Scissors"):
            return "Player one wins!"
        else: return "Player two wins!"

    if(player_one == "Scissors"):
        if(player_two == "Stone"):
            return "Player two wins!"
        elif(player_two == "Scissors"):
            return "It's a tie."
        else: return "Player one wins!"

    if(player_one == "Paper"):
        if(player_two == "Stone"):
            return "Player one wins!"
        elif(player_two == "Scissors"):
            return "Player two wins!"
        else: return "It's a tie."


# Test Cases for Exercise 2.1

print rps("Paper", "Stone") # This should return "Player one wins!"
print rps("Stone", "Stone") # This should return "It's a tie."
#rps("Rock", "Scissors") # This should return "Player one please choose: Stone, Scissors or Paper:"


# ********** Exercise 2.2 ********** 

# Define is_divisible function here

def is_divisible(m, n):

    if(m == 0 or n == 0):
        return "Please avoid using 0"
        

    if(m % n != 0):
        return False
    else: return True

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
print is_divisible(42, 0)  # What should this return?


# Define not_equal function here

def not_equal(a, b):

    if(a == b):
        return False
    else: return True

# Test cases for not_equal

print not_equal(4, 5)
print not_equal(9, 9)
print not_equal(10, -10)

# ********** Exercise 2.3 ********** 

## 1 - multadd function
def multadd(A, B, C):

    return A * B + C

## 2 - Equations
##### YOUR CODE HERE #####


# Test Cases
# angle_test =
# print "sin(pi/4) + cos(pi/4)/2 is:"
# print angle_test

# ceiling_test =
# print "ceiling(276/19) + 2 log_7(12) is:"
# print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####


# Test Cases
# x = 5
# print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####

# Test Cases
##### YOUR CODE HERE #####

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####

# Test Cases
##### YOUR CODE HERE #####                            


# ********** Exercise 2.5 **********

# code for roots function
##### YOUR CODE HERE #####   

# Test Cases
##### YOUR CODE HERE #####   
