# Shopping List
# Create a program where the user can:
# 1. Add item
# 2. Remove item
# 3. View items
# 4. Exit
print("Welcome to ABC Supper Store\n")
item=[]
while True:
        print("1. Add items")
        print("2. Remove items")
        print("3. View items")
        print("4. Exit")
        choice=input("Enter the choice:")
        if choice=="1":
            while True:
                i=input("Enter the item name(type done to finish):")
                if i=="done":
                    break
                item.append(i)
        elif choice=="2":
             while True:
                i=input("Enter the item name to remove or type end to end:")
                if i=="end":
                     break
                item.remove(i) 
                print("item is removed!")       
        elif choice=="3":
             print(item)  
        elif choice=="4":
             print("Exit")
             item.clear()
             print("Add the items again.")  
        else:
             print("invalid choice.")
             break              
                
                
                
                 