# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:59:28 2020

@author: Yung
"""
import random

#variable initialization
choices = ["rock", "paper", "scissors"] #valid input/choices
play_again_yes = ["yes","y"]
player_score = 0
computer_score = 0
play_again = play_again_yes[0]

#asks user for input until it's valid
#return the input
def player_input_check():
    player_input = input("Rock, Paper, or Scissors? ").lower() #filter input to lowercase
    while player_input not in choices: #while input not valid
        print("That is not a valid input!") #yell at user
        player_input = input("Rock, Paper, or Scissors? ").lower() #get input agin

    return player_input

# receives player input and scores
# makes computer choice
# compare and print result. Calculate and return scores. 
def who_won(p_choice, p_score, c_score):
    print("\n") #white space for formatting
    print("Your choice: ", p_choice.title()) #print out input
    computer_choice = random.choice(choices)
    print("Computer's choice: ", computer_choice.title())
    #logic comparison
    if computer_choice == p_choice: #draw condition
        print("It's a draw!")
    elif computer_choice == "rock" and p_choice == "paper":
        print("You win!")
        p_score += 1
    elif computer_choice == "rock" and p_choice == "scissors":
        print("Computer wins!")
        c_score += 1
    elif computer_choice == "paper" and p_choice == "scissors":
        print("You win!")
        p_score += 1
    elif computer_choice == "paper" and p_choice == "rock":
        print("Computer wins!")
        c_score += 1
    elif computer_choice == "scissors" and p_choice == "paper":
        print("Computer wins!")
        c_score += 1
    elif computer_choice == "scissors" and p_choice == "rock":
        print("You win!")
        p_score += 1
        
    return p_score, c_score
    
while play_again in play_again_yes: #if the choice is a yes or y
    #call player's choice
    player_choice = player_input_check()
    
    #get scores
    player_score, computer_score = who_won(player_choice, 
                                           player_score, computer_score)
    
    #print result
    print("\n") #white space for formatting
    print(f"Current Score is Player: {player_score} Computer: {computer_score}")
    print("Play Again? (Y/N)")
    #check for playing again
    play_again = input().lower()
    print("\n") #white space for formatting