import random 

#computer chooses their pick
computer_choice = random.choice(["rock", "paper", "scissors"])
print("rock, paper, or scissors ?")
#player input
my_choice = input()

#print out player and computer choice
print("Your Choice ", my_choice)
print("Computer Choice ", computer_choice)

#did you win?
if computer_choice == my_choice:
    print("It's a draw!")
elif computer_choice == "rock" and my_choice == "paper":
    print("You win!")
elif computer_choice == "rock" and my_choice == "scissors":
    print("I win!")
elif computer_choice == "scissors" and my_choice == "paper":
    print("I win!")
elif computer_choice == "scissors" and my_choice == "rock":
    print("You win!")
elif computer_choice == "paper" and my_choice == "rock":
    print("I win!")
elif computer_choice == "paper" and my_choice == "scissors":
    print("You win!")