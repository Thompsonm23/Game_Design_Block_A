#Maurice Thompson
#This is a number game made in class
#9/15/21

import os
import random
from time import sleep
import time
from typing import Counter
os.system('cls')
#This is for random numbers
randy = random.randint(1, 100)

print("Welcome to the number guessing game. In this game you will have 10 chances to guess a number between 1 and 100")
time.sleep(2)
answer = input("Do you want to play a game? ")
time.sleep(2)
while ('yes' in answer):
    Counter = 10
    while Counter < 11:
        print("You have this many chances: ", Counter)
        Counter = Counter -1
        guess = int(input("Give me a number: "))
        try:
            guess = int(guess)
            check=True
        except ValueError:
            check=False
        if randy > guess:
            print("That number is too low")
        if randy < guess:
            print("That number is too high")
        if randy == guess:
            print("You are correct!")
            break
        if Counter == 0:
            print("You Failed")
            break
    print("The answer is ", randy)
    time.sleep(2)#Waits a few seconds before printing
    answer = input("Do you want to play again? ")
while ('no' in answer):
    print("Thank you for playing!")
    time.sleep(2)
    print()
    break


