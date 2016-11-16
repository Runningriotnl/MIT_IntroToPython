A = input("Which month were you born in (number): ")

while(A < 1 or A > 12):
    print "I doubt it"
    A = input("Try again: ")


B = (A < 1 | A > 12)
print B
