# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 23:24:12 2020

@author: Yung
"""
import random

class game:
    def __init__(self):
        #variable initialization
        self.choices = ["rock", "paper", "scissors"] #valid input/choices
        self.yes = ["yes", "y"]
        self.no = ["no", "n"]
        self.player_score = 0
        self.computer_score = 0
    
    # This functions prompts user for the choice and validates input
    # Input: none
    # Output: User's seleciton of rock, paper, or scissors
    def player_input_check(self):
        player_input = input("Rock, Paper, or Scissors? ").lower() #filter input to lowercase
        while player_input not in self.choices: #while input not valid
            print("That is not a valid input!") #yell at user
            player_input = input("Rock, Paper, or Scissors?").lower() #get input agin
        return player_input
    
    # This function receives player choice, selects random choice and scores the result
    # Input: player choice from player_input_check    
    # Output: player score and computer score
    def who_won(self, p_choice):
        print("\n") #white space for formatting
        print("Your choice: ", p_choice.title()) #print out input
        computer_choice = random.choice(self.choices)
        print("Computer's choice: ", computer_choice.title())
        #logic comparison
        if computer_choice == p_choice: #draw condition
            print("It's a draw!")
        elif computer_choice == "rock" and p_choice == "paper":
            print("You win!")
            self.player_score += 1
        elif computer_choice == "rock" and p_choice == "scissors":
            print("Computer wins!")
            self.computer_score += 1
        elif computer_choice == "paper" and p_choice == "scissors":
            print("You win!")
            self.player_score += 1
        elif computer_choice == "paper" and p_choice == "rock":
            print("Computer wins!")
            self.computer_score += 1
        elif computer_choice == "scissors" and p_choice == "paper":
            print("Computer wins!")
            self.computer_score += 1
        elif computer_choice == "scissors" and p_choice == "rock":
            print("You win!")
            self.player_score += 1
        return self.player_score, self.computer_score
    
    def play_again(self):
        again = input("Play Again? (Y/N) ").lower()
        while again not in (self.yes + self.no): #while input not valid
            print("That is not a valid input!") #yell at user
            again = input("Play Again? (Y/N) ").lower()
        if again in self.yes:
            return True
        else:
            return False

    
    