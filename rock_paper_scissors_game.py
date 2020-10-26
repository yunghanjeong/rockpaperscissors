# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 01:01:11 2020

@author: Yung
"""
from src.rockpaperscissors import game

play = True #set true to run first
gm = game() #initialize the game

while play:
    user_score, computer_score = gm.who_won() # play and get score
    print(f"Current Score is Player: {user_score} Computer: {computer_score}") #print score
    play = gm.play_again() #check for replay