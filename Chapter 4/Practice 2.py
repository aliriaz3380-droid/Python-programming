food=[]
food1=input("Enter the first food name:")
food2=input("Enter the second food name:")
food3=input("Enter the third food name:")
food=[food1,food2,food3]
print("food=",food)

#  Because your list contains strings, max() does not find the biggest food by size or price.
#  It compares the words alphabetically based on their characters.

# Capital letters (A-Z) ki Unicode values lowercase letters (a-z) sa kum hoti ha

print("Total items=",len(food))      # to find the length of list
print(max(food))        # to find the maximum string in list
print(min(food))        # to find the minimum string in list
food.append("ilachi")   # to write string at the end of list
print(food)
food.insert(1,"pineapple")    # to insert string at mention index
print(food)
food.pop(0)     # to elemenate a string from mention index
print(food)
food.sort()
print(food)
food.reverse()
print(food)
