# To find the factorial of a number
n=int(input("Enter the number to find the factorial:"))
def fac(n):
    if n==0:
         return 1
    return n*fac(n-1)
                       
result=fac(n)
print(result) 


# To print the name at given number of time

n=int(input("Tell me how many times you want to print name:"))
nic=input("Write the Name you want to print:")

def name(n):
    if n==0:
        return ""
    print(nic)
    return name(n-1)
result=name(n)
print(result)


# To find the power of given number
n=int(input("Tell the number to find it's power:"))
p=int(input("Tell the power:"))
def power(n,p):
    if p==0:
        return 1
    else:
        return n*power(n,p-1)
    
result=power(n,p)
print(result)


# Enter the number to find either it is prime or not
n=int(input("Enter the number to check either it is prime or not:"))
def prime(n,i):
    if i==1:
        return "Prime Number"
    if n%i==0:
        return "Not a Prime number"
    return prime(n,i-1)
if n<2:
        result="Not a Prime number"
else:        
    result=prime(n,n-1)
print(result)


# To count the number of digit in a number
n=int(input("Enter the number to find its digit"))
def count(n):
    if n<10:
        return 1
    return 1+count(n//10)
if n<0:
    n=-n
result=count(n)
print(result)    


# Fibonacci rule to find the term
n=int(input("Enter the number to find term:"))
def febo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return febo(n-2)+febo(n-1)
for i in range(1,n+1):
    result=febo(i)
    print(result)


 # sum of n numbers
n=int(input("Enter the number to find the sum:"))
def sum(n):
    if n==0:
       return 0
    return n+sum(n-1)
result=sum(n)
print(result)   