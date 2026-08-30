# Create a program using global keyword to modify a variable from inside a function.
def func():
    global x
    x=20
    print("The value of x is=",x)
func()
print("The value of x outside a function is=",x)