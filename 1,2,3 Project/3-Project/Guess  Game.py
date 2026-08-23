import random
number=random.randint(1,10)
guess=int(input("Enter a number from 1 to 10 to find guess:"))
while guess!= number:
    print("Wrong Guess! Try again")
    guess=int(input("Guess again."))
print("Congratulation! Ali you Guess the right number.")    