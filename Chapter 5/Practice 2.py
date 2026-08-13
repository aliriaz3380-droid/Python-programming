# You are given a list of programming languages: 
# ["Python", "Java", "C++", "Python", "Java", "C"] 
# Convert it into a set and print how many unique languages Divya knows.

programmingList=["Python", "Java", "C++", "Python", "Java", "C"] 
print(type(programmingList))
# convert it to set
programmingset=set(programmingList)
print(programmingset)
emptyset=set()
print(type(emptyset))
print("How many unique languages Divya knows:",len(programmingset))