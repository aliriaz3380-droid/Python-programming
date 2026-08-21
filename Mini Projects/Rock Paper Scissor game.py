# Rock Paper Scissors ⭐⭐⭐
# Computer randomly chooses:
# Rock
# Paper
#Scissors
import random
print("Rock Paper Scissor Game")
while True:
    choices=["rock","paper","scissor"]
    computer=random.choice(choices)  
    user=input("Enter Rock,Paper and Scissor:").lower() 
    print("Computer Choice:",computer) 
    if user==computer:
        print("Tie")
    elif user=="rock" and  computer=="scissor":
        print("You win!") 
    elif user=="paper" and computer=="rock":
        print("You win!")
    elif user=="scissor" and computer=="paper":
        print("You win!") 
    else:
        print("Computer win!") 
        break          