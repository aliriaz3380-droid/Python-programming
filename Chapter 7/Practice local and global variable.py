# Write a program with a local variable score inside a function and a global one outside. 
x=30
def variable():
    x=20
    print("This is the local variable value=",x)
   
variable()
print("This is the global variable value=",x)
