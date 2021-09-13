#Maurice Thompson
#9/13/2021
#This is about data types and how strings work
#Program for if you want a specific data type from User
import os
os.system('cls')

userInput=input("Type something ")
print (type(userInput))
try:
    int(userInput)
    check=True
except ValueError:
    check=False

if(check):
    # I will be back
    print()
else:
    print(len(userInput))
for i in userInput:
    print(i)




#Int 4bytes