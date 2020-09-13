#!/home/mamaah/development/RPS/bin/python3
import random
# print game_name and game_rules
while True:
    print('welcome to rock paper scissors')
    print('rock beats scissors')
    print('scissors beats paper')
    print('paper beats rock')
    # define choice
    choices = ['rock', 'paper', 'scissors']
    # store computer's choice as a variable 
    computer_choice = random.choice(choices)
    # get user input
    user_choice = input('please enter your choice: rock, paper or scissors?')
    # determine winner
    # if user_choice == computer_choice:
        # it is a tie!
    if user_choice == computer_choice:
        print("it is a Tie!")
    # if user_choice == rock and computer_choice == scissors:
        # user_choice wins
    elif user_choice == "rock" and computer_choice == "scissors":
            print("you win!")
    # if user_choice == scissors and computer_choice == paper:
        # user_choice wins
    elif user_choice == "scissors" and computer_choice == "paper":
            print("you win")
    # if user_choice == paper and computer_choice == rock:
        # user_choice wins
    elif user_choice == "paper" and computer_choice == "rock":
            print("you win")
    # else:
        # computer_choice wins
    else:
        print("computer wins")
    play_again = input('Do you want to play again, enter Y or N: ')
    if play_again.upper() == 'N':
        break
    # say rock paper scissors shoot
    # release the rock paper or scissors