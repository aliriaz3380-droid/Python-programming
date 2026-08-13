# Try to add both integer 9 and float 9.0 to a set and observe what happens.
set1=set()
set1.add(int(input("Enter the integer 9:")))
set1.add(input("Enter the float 9.0:"))
print(set1)
print(len(set1))