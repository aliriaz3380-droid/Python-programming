# Write a recursive function that prints numbers from 1 to N.
def number(n):
    if n==0:
        return 
    else: 
        result=number(n-1)
        print(n)
        return result
   
    
    
number(10)
