# Write code to open a file named mydata.txt in read mode. 
with open("mytest.txt","r") as file:
    datafile=file.read()
    print(datafile)