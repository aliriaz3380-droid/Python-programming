operand1=float(input("Enter the number:"))
operator=input("Enter the operator:")
operand2=float(input("Enter the number:"))
if operator=="+":
    sum=operand1+operand2
    print(round(sum,2))
elif operator=="-":
    minus=operand1-operand2
    print(round(minus,2))
elif operator=="*":
    multiply=operand1*operand2
    print(round(multiply,2))
elif operator=="/":
    division=operand1/operand2
    print(round(division,2))
elif operator=="**":
    square=operand1**operand2
    print(round(square,4))     
else:
    print("Invalid operation")
         


