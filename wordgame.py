#Maurice Thompson
#Word game collum
import os
os.system('cls')
import random

def Menu():
    print("##############################################")
    print("#                   Menu                     #")
    print("#                                            #")
    print("#                [1]Animals                  #")
    print("#                [2]Fruits                   #")
    print("#                [3]Colors                   #")
    print("#                [4]Exit                     #")
    print("#To play the game select 1-3 tp exit select 4#")
    print("##############################################")
    sel=input("What would you like to do?")
    sel=int(sel)
    return sel
Colors = ['blue','red','yellow','green','black','white']
Fruits = ['banana', 'apple', 'strawberry', 'blue berry', 'pear', 'grape',]
Animals = ['dog','cat', 'mouse', 'horse','cow','giraffe','rhino','cheetah','lion']
def selWord(sel):
    if sel == 1:
        word= random.choice(Animals)
    if sel == 2:
        word= random.choice(Fruits)
    if sel == 3:
        word= random.choice(Colors)
    return word
 
answer = input("Do you want to play a game?")
while 'y' in answer:
    print("Guess the characters")
    guesses = ''
    turns = 3
    while 'y' in answer:
        while turns > 0:
            failed = 0
            for char in selWord:
                if char in guesses:
                    print(char)  
                else:
                    print("_")
                    failed += 1
            if failed == 0:
                print("You Win")
                print("The word is: ", selWord)
                break
            guess = input("guess a character:")
            guesses += guess

            if guess not in selWord:        
                turns -= 1
                print("Wrong")
                print("You have", + turns, 'more guesses')
                if turns == 0:
                    print("You Loose")
        while 'n' in answer:
            print("thank you for playing")