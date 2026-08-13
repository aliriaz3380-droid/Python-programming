# Create a dictionary named marks to store marks of 3 subjects. 
# Add the subjects one by one and print the final dictionary.
marks={}
print(type(marks))
marks["sub1"]=input("Enter the name of first subject:")
marks["sub2"]=input("Enter the name of second subject:")
marks["sub3"]=input("Enter the name of third subject:")
print(marks)
print(marks.keys())    # to print keys 
print(marks.values())  # to print values
print(marks.items())   # to print items
print(marks.get("sub1"))  # to print value of mentioned key
marks.update({"City":"T-T Singh","Area":"Punjab"})  # to add dictinary to another dictionary
print(marks)
print(len(marks))
print(marks.pop("sub1"))
print(marks)