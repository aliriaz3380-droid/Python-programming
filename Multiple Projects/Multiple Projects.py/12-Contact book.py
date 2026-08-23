# Contact Book ⭐
# Use a dictionary:
# Allow the user to:
# 1. Add contact
# 2. Search contact
# 3. Delete contact
# 4. Show all contacts
# 5. Exit
print("My Contact Book")
contact={}
while True:
    print("1. Add Contact:")
    print("2. Search Contact:")
    print("3. Delet Contact:")
    print("4. Show all Contacts:")
    choice=input("Enter your Choice:")
    if choice=="1":
       
            name=input("Enter the Name:")
            phone=input("Enter the Phone Number:")
            contact[name]=phone
            print("Contact is added!")
    elif choice=="2":
          name=input("Enter the Name to search:")
          if name in contact:
                print("Phone Number:",contact[name])
    elif choice=="3":
          name=input("Enter the Name to delet:")
          if name in contact:
                contact.pop(name) 
                print("Contact is deleted!")           
                
    elif choice=="4":
          print(contact)        
    else:
          print("Invalid Choice.")
          break        