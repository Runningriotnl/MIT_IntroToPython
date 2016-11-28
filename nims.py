# Name: Paul Korver
# Section:
# nims.py

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    while(pile > 0):
        print "There are " + str(pile) + " stones left."

        winner = "Player two"

        player_one_stone = input("Player One, how many stones do you want to take of the pile: ")
        print player_one_stone
        while(player_one_stone > max_stones or player_one_stone < 1 or player_one_stone == ""):
            player_one_stone = input("Please select a value of minimal 1 or maximal " + str(max_stones) + ": ")
            
        pile = pile - player_one_stone

        if(pile < 1):
            return winner + " won!"

        print "There are " + str(pile) + " stones left."

        winner = "Player one"

        player_two_stone = input("Player Two, how many stones do you want to take of the pile: ")
        while(player_two_stone > max_stones or player_two_stone < 1):
            player_two_stone = input("Please select a value of minimal 1 or maximal " + str(max_stones) + ": ")
        pile = pile - player_two_stone

        if(pile < 1):
            return winner + " won!"

    

    ## Basic structure of program (feel free to alter as you please):

#    while [pile is not empty]:
#        while [player 1's answer is not valid]:
#            [ask player 1]
#            [execute player 1's move]
#       
#        while [player 2's answer is not valid]:
#            [ask player 2]
#            [execute player 2's move]
#
#    print "Game over"
