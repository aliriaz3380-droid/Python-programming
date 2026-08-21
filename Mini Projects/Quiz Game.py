# Quiz Game ⭐⭐⭐
# Store questions and answers and calculate the score.
# Q1. What is the capital of Pakistan?
# 1. Lahore
# 2. Islamabad
# 3. Karachi
# Your answer: 2
# Correct!
# Score: 1/1
print("Welcome to Quiz Game!")
score=0
print("Q1. What is the capital of Pakistan?")
print("1. Lahore")
print("2. Islamabad")
print("3. Karachi")
choice=input("Enter your choice:")
if choice=="2":
    score=score+1
    print("Correct!")
elif choice=="1" or choice=="3":
    print("Not Correct.")
print("Q2. What is the largest Province of Pakistan?")
print("1. Punjab")
print("2. Sindh")
print("3. Balochistan")
choice=input("Enter your Choice:")
if choice=="3":
    score=score+1
    print("Correct!")
elif choice=="1" or choice=="2":
    print("Not Correct")
print(f"Your Score is {score}/2")    