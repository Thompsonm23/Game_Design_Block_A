#Maurice Thompson
#Word game collum
import os
os.system('cls')
import random
def updateWord(word, guesses):
    for letter in word:
        if letter in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')

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
 
answer = input("What is your name?")
maxScore=0
sel= Menu()
print(sel)
turns= 0
while sel !=4:
    word= selWord(sel)
    word= word.lower()
    wordCount=len(word)
    turns= wordCount+2
    letCount=0
    guesses=''
    score=0
    updateWord(word, guesses)

    while turns > 0 and letCount<=wordCount:
        print()
        newguess= input("give me a letter")
        newguess= newguess.lower()
        if newguess in word:
            guesses+= newguess
            letCount +=1
            print("you guessed right!")
        else:
            turns-= 1
            print("You guessed wrong, you have ", turns, " turns left.")
        updateWord(word, guesses)
    if turns <0 :
        print("You lose")
        sel=Menu()
    os.system('cls')
    score=10*wordCount+5*turns
    print("Your score is ", score)
    if score> maxScore:
        maxScore=score
    saveScore = (score)
    name = input('Enter your name. ').title()
    saveScore = input('Enter your score. ')
    textFile = open("score.txt", "a")
    textFile.write("\n" + name + ' has a score of ' + saveScore + "\n")
  
    print ("\n")
    textFile = open("score.txt", "r")
    whole = textFile.read()
    print (whole)
    textFile.close()
    print
    sel=Menu()
