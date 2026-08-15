#  Write a program to print the multiplication table of any number using a while loop. 
#  i"*"n=i*n
i=int(input("Enter the number to see its table:"))
n=1
while n<=10:
    print(f"{i}*{n}={i*n}")
    n=n+1