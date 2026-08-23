list1=["apple","mango","orange","banana"]
print(type(list1),"\n",list1)
# geting values from user input
list2=[]
print(type(list2))
food1=input("Enter the value at item 1:")
food2=input("Enter the value at item 2:")
food3=input("Enter the value at item 3:")
food4=input("Enter the value at item 4:")
list2=[food1,food2,food3,food4]
print(list2)
print(list2[0::])
list2.insert(4,"orange")
print(list2)
list2.remove("apple")
print(list2)
list2.pop(2)
print(list2)