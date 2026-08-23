# You are required to build a simple personal finance management tool. 
# The program should allow the user to: 
# ● Add an expense with details like date, category, description, and amount. 
# ● View all recorded expenses in a clean format. 
# ● Calculate total spending so far. 
# ● Exit the program gracefully when the user chooses to. 
print("Welcome to Personal Finance App")
expense=[]
while True:
    print("1. Add an expense.")
    print("2. View all expenses.")
    print("3. Calculate total amount spending.")
    print("4. Exit the program.")
    choice=input("Enter your choice:")
    if choice=="1":
        dic={}
        dic["Date"]=input("Enter the date of expense:")
        dic["Category"]=input("Enter the category of expense:")
        dic["Description"]=input("Enter the description of expense:")
        dic["Amount"]=int(input("Enter the amount spend on expense:"))
        expense.append(dic)
       
        
    elif choice=="2":
        for dic in expense:
         print(dic)
    elif choice=="3":
        total=0
        for dic in expense:
            total=total+dic["Amount"]
        print(total)
    elif choice=="4":
        print("Exit")
        break
    else:
        print("Invalid Choice.")
        break            