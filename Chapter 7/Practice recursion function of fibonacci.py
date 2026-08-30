# Write a recursive function to print the Fibonacci series up to N terms. 
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)
        
    
print(fibonacci(5))