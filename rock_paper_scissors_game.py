# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 01:01:11 2020

@author: Yung
"""
from src.rockpaperscissors import game

play = True #set true to run first
gm = game()

while play:
     user_choice = gm.player_input_check()
     user_score, computer_score = gm.who_won(user_choice)
     print(f"Current Score is Player: {user_score} Computer: {computer_score}")
     play = gm.play_again()