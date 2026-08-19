# Shopping List
# Create a program where the user can:
# 1. Add item
# 2. Remove item
# 3. View items
# 4. Exit

print("Welcome to ABC Shopping Center")

list1=[]
while True:
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("4. Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        n=int(input("How many items you want to add:"))
        print(f"I want {n} items")
        for item in range(n):
            item=input("Enter the item Name:")
            list1.append(item)
        print(f"Your items are {list1}") 
    elif choice=="2":
            item=input("Enter the item name to remove:") 
            if item in list1:
              list1.remove(item)
              print("item removed!")
            else:
                 print("item not found:")    
    elif choice=="3" :
            print(list1)  
                
    elif choice=="4":
            print("Exit")
            list1.clear()
            print("Add the items again.")
    else:
        print("invalid choice")    
        break
    