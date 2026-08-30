# Define a function message(text="Keep Learning!") and call it with and without an argument. 
# with arguments
def withArguments(text):
    return text
text=withArguments("keep Learning!")
print(text,"\n")
print("Now without Arguments.\n")
# without arguments
def withoutArguments(text="keep Learning!"):
    return text
text=withoutArguments()
print(text)
