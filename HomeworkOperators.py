#Maurice Thompson
import os 
os.system('cls')

num= int(input("Whats your number? :"))
giv= num%10
print("Your number is ", giv)

giv2= int(input("What is your second number? :"))
num2= giv2%100
if (num2 > 9):
    print("Your second number is ", num2)
else:
    print("Program Failed")

giv3= int(input("What is your third number? :"))
num3= giv3%1000
if (num3 > 99):
    print("Your third number is ", num3)
else:
    print("Program Fail")