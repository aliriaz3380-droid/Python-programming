# Password Checker
# Ask the user to enter a password.
# Check whether:
# Password has at least 8 characters
# Contains a number
# Contains an uppercase letter
import string
while True:
    password=input("Enter the password:")
    has_number=False
    has_uppercase=False
    has_lowercase=False
    has_special=False
    if len(password)>=8:
        print("You enter password")
    else:
        print("password must greater then 7 characters")
    for i in password:
        if i.isdigit():
            has_number=True
        if i.isupper():
            has_uppercase=True
        if i.islower():
            has_lowercase=True
        if i in string.punctuation:
            has_special=True   
    if len(password)>=8 and has_number and has_uppercase and has_lowercase and has_special:
        print("Strong password")
        break
    else:
        print("Weak password")
        print("Enter the password again")
    