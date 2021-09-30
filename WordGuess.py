#Maurice Thompson
#9/27/2021
#This is a guessing game using arrays


import random
import os
os.system('cls')
 
words = ['red', 'green', 'yellow', 'blue', 'black', 'white']
 
 
print("This is a word guessing game. You have 3 chances to guess a color.")
print("Guess the word, you have 3 chances.")
answer = input("Do you want to play a game?")
 
while ('yes' in answer):
    word = random.choice(words)
    Counter = 3
    while Counter < 4:
        print("You have this many chances: ", Counter)
        guess = str(input("Guess a word: "))
        if guess not in word:
            Counter -= 1
            print("wrong")
        if word == guess:
            print("You are correct!")
            break
        if Counter == 0:
            print("You Failed")
            break
    print("The answer is ", word)
    answer = input("Do you want to play again? ")
while ('no' in answer):
    print("Thank you for playing!")

    print()
    break