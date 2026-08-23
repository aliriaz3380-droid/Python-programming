# ATM Simulator ⭐⭐⭐
# Create:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
print("ATM Simulator")
balance=10000
while True:
    print("1. Check Balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Exit")
    choice=input("Enter your Choice:")
    if choice=="1":
        print("Your Balance is:",balance)
    elif choice=="2":
        deposite=int(input("Enter the amount you want to deposit in balance:"))
        balance=balance+deposite
        print("Balance is added!")
    elif choice=="3":
        withdraw=int(input("Enter the amount you want to withdraw from balance:"))
        if balance>=withdraw:
            balance=balance-withdraw
            print("Your amount is withdraw!")
        else:    
            print("Your amount is insufficient to withdraw.")
    elif choice=="4":
        print("Exit")
        break
    else:
        print("Invalid Choice")
        break