# Print the multiplication table of a number using a loop. 
n=int(input("Enter the number to see it,s Table:"))
for i in range(1,11,1):
    print(f"{n}*{i}={n*i}")