# Simple if elif else rock paper siccors program

player_one = raw_input("Player one please choose: ")
player_two = raw_input("Player two please choose: ")

if(player_one != "Stone" and player_one != "Scissors" and player_one != "Paper"):
    player_one = raw_input("Player one please choose: Stone, Scissors or Paper: ")
   
if(player_two != "Stone" and player_two != "Scissors" and player_two != "Paper"):
    player_two = raw_input("Player two lease choose: Stone, Scissors or Paper: ")

if(player_one == "Stone"):
    if(player_two == "Stone"):
        print "It's a tie."
    elif(player_two == "Scissors"):
            print "Player one wins!"
    else: print "Player two wins!"

if(player_one == "Scissors"):
    if(player_two == "Stone"):
        print "Player two wins!"
    elif(player_two == "Scissors"):
        print "It's a tie."
    else: print "Player one wins!"

if(player_one == "Paper"):
    if(player_two == "Stone"):
        print "Player one wins!"
    elif(player_two == "Scissors"):
        print "Player two wins!"
    else: print "It's a tie."

