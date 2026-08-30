# Create a function login(username, password="1234") that prints the credentials. 
def login(username,password="1234"):
    return username,password
username,password=login(username="Ali Riaz")
print(f"username={username},password={password}")