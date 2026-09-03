# Rule based AI chat bot
import datetime
time=datetime.datetime.now()
hour=time.hour
name=input("Tell me your name:")
if hour>=1 and hour<12:
    print("Good Morning",name)
elif hour>=12 and hour<13:
    print("Good after noon",name)
elif hour>=13 and hour<15:
    print("Good noon",name)
elif hour>=15 and hour<17:
    print("Good evening",name)
else:
    print("Good night",name)        
dic={"hello":"Hi! How are you","how are you":"I am fine","who are you":"I am Rule based AI chat bot",
     "where you live":"I live in computers, laptops and mobiles",
     "motivate me":"Keep going and work hard one day you will be successfull",
     "tell me about python":"You can learn it and develop websites,AI/ML projects and many more",
     }

def chatbot(userinput):
    userinput=userinput.lower()
    for eachkey in dic:
        if eachkey in userinput:
            return dic[eachkey]
    return "Mja is ka ni pta juld hee ya b seekh kr ap ko bta doo ga"
while True:
   userinput=input("Ask any question:")
   if "bye" in userinput.lower():
    print("Good bye")
    break 
   result=chatbot(userinput)
   print("Chatbot response:",result)  