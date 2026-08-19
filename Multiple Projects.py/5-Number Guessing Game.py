    # Number Guessing Game ⭐
    # You already made this project. Improve it.
    # Add:
    # Too high / too low hints
    # Number of attempts
    # Option to play again
    # Score
import random
while True:
    num=random.randint(1,10)
    attempts=0
    score=100
    guess=int(input("Enter the number from 1 to 10 to find guess:"))
    while       guess!=num:
                attempts=attempts+1
                if guess< num:
                    print("Too low")
                    score=score-10
                elif guess> num:
                    print("Too high")
                    score=score-10
                guess=int(input("Enter the number again to find guess:"))
    attempts=attempts+1
    print("Congratulation!")  
    print("Attempts=",attempts)
    print("Score=",score) 

                                
    again = input("Do you want to play again? yes/no: ")
    
    if again != "yes":
        break