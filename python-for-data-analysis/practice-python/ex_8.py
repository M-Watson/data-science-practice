'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''
import random

def win_check(hand1,hand2):
    result = 'tie'
    if hand1 == 'rock':
        if hand2 == 'scissors':
            result = 'hand1'
        elif hand2 == 'paper':
            result = 'hand2'

    elif hand1 == 'paper':
        if hand2 == 'scissors':
            result = 'hand2'
        elif hand2 == 'rock':
            result = 'hand1'

    if hand1 == 'scissors':
        if hand2 == 'paper':
            result = 'hand1'
        elif hand2 == 'rock':
            result = 'hand2'
    return(result)

playing = True

while playing == True:

    player_count = input('Would you like to play one or two player (1 or 2) ?')


    if player_count == '1':
        player_1 = input('Player 1:\n\t Rock, paper, or scissors?  ')
        print("\nThank you player 1\n")

        choice_list = ['rock','paper','scissors']
        choice_num = random.randint(0,2)
        player_2 = choice_list[choice_num]
        player_2_output = print('Player 2:\n\t Rock, paper, or scissors?\nPlayer 2 chose: {}   '.format(player_2))
        print("\nThank you player 2\n")
        print("And the winner is....")
    elif player_count == '2':
        player_1 = input('Player 1:\n\t Rock, paper, or scissors?  ')
        print("\nThank you player 1\n")
        player_2 = input('Player 2:\n\t Rock, paper, or scissors?  ')
        print("\nThank you player 2\n")
        print("And the winner is....")

    winner = win_check(player_1.lower(),player_2.lower())

    if winner == 'hand1':
        print("Player 1 wins with {} over {}!!".format(player_1.lower(),player_2.lower()))
    elif winner =='hand2':
        print("Player 2 wins with {} over {}!!".format(player_2.lower(),player_1.lower()))
    else:
        print("It is a tie, both players chose {}...".format(player_1.lower()))


    again = input('Would you like to play again? (y/n)')
    if again.lower() == 'y' or again.lower() == 'yes':
        playing = True
    elif again.lower() == 'n' or again.lower() == 'no':
        print("\n\t...Thank you, good bye...")
        playing = False
