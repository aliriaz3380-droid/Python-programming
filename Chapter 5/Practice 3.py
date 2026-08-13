# not given in notes
# when set is not given and taking input from user
food=set()
print(type(food))
food.add(input("Enter the first food name:"))
food.add(input("Enter the second food name:"))
food.add(input("Enter the third food name:"))
food.add(input("Enter the fourth food name:"))
food.add(input("Enter the fifth food name:"))
print(food)

# when set is given
fruit={"apple","banana","mango","orange","pineapple"}
print(fruit)
fruit.add("ilichi")   # to add value to set
print(fruit)
fruit.remove("ilichi")  # to remove specific value from set
print(fruit)
fruit.pop()   # to delet arbitrary value from set
print(fruit)
