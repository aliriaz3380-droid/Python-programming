#  Write a program that prints the multiplication table of any number entered by 
#  the user using a for loop.
n=int(input("Enter the number you want to see it's table:"))
for i in range(1,11,1):
    print(f"{n}*{i}={n*i}")