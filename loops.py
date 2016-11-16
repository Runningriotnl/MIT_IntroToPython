# Loops exercises

# 1.

a = 1.0

for i in range(1, 11):
    print a/i

# 2.

user_input = input("What number do you want to start at: ")

if(user_input < 0):
     user_input = input("Please select a number higher then 0: ")

while(user_input >= 0):
    print user_input
    user_input -= 1

# 3.

base = input("What number would you like to use as base number: ")
exp = input("What should be the exponent: ")

print base ** exp

# 4.

ask_user = input("Please give a number that is divisible by 2: ")

while(ask_user % 2 != 0):
    print "I said divisible by 2!"
    ask_user = input("Try again: ")
    
print "Well thank you, I will put this in my database"
