import random

def rps(player_one):

    ai_choice = random.randrange(1, 4)

    if(ai_choice == 1):
        player_two = "Stone"

    if(ai_choice == 2):
        player_two = "Scissors"

    if(ai_choice == 3):
        player_two = "Paper"

    while(player_one != "Stone" and player_one != "Scissors" and player_one != "Paper"):
        player_one = raw_input("Player one please choose: Stone, Scissors or Paper: ")

    print "Your opponent choose: " + player_two

    if(player_one == "Stone"):
        if(player_two == "Stone"):
            return "It's a tie."
        elif(player_two == "Scissors"):
            return "You win!"
        else: return "You lose!"

    if(player_one == "Scissors"):
        if(player_two == "Stone"):
            return "You lose!"
        elif(player_two == "Scissors"):
            return "It's a tie."
        else: return "You win!"

    if(player_one == "Paper"):
        if(player_two == "Stone"):
            return "You win!"
        elif(player_two == "Scissors"):
            return "You lose!"
        else: return "It's a tie."


