#Word Game
# Maurice Thompson
#10/13/2021
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed  
# play as long as the user has turns or has guessed the word
import os
os.system('cls')
import random
def updateWord(word, guesses):#Function to update letters and spaces/dashes
    for letter in word:
        if letter in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')

def Menu():#menu is used to select array of words
    print("##############################################")
    print("#                   Menu                     #")
    print("#                                            #")
    print("#                [1]Animals                  #")
    print("#                [2]Fruits                   #")
    print("#                [3]Colors                   #")
    print("#                [4]Exit                     #")
    print("#To play the game select 1-3 tp exit select 4#")
    print("##############################################")
    print("This is a word game that gives you a certain amount of geusses to guess a word related to the topic you choose.")
    sel=input("What would you like to do?")
    sel=int(sel)#try and accept
    return sel
Colors = ['blue','red','yellow','green','black','white']
Fruits = ['banana', 'apple', 'strawberry', 'blue berry', 'pear', 'grape',]
Animals = ['dog','cat', 'mouse', 'horse','cow','giraffe','rhino','cheetah','lion']
def theExit(sel):#This is the exit function
    if sel ==4:
        textFile = open('score.txt', 'r')
        whole = textFile.read()
        print(whole)
        textFile.close()
def selWord(sel):
    if sel == 1:
        word= random.choice(Animals)
    if sel == 2:
        word= random.choice(Fruits)
    if sel == 3:
        word= random.choice(Colors)
    return word
    #Create file for scoreboard and return to menu or exit game.



 
name = input('Enter your name. ').title()
maxScore=0
sel= Menu()
print(sel)
turns= 0
while sel ==4:#Exit function
    print("Thank you for playing!")
    theExit(sel)
    break

while sel <4:
    word= selWord(sel)
    word= word.lower()
    wordCount=len(word)
    turns= wordCount+2#Depends on word lenght
    letCount=0#Check if the user ended up guessing the word
    guesses=''
    score=0
    updateWord(word, guesses)

    while turns > 0 and letCount<=wordCount:
        print()
        newguess= input("give me a letter")
        newguess= newguess.lower()#Lower cases code
        if newguess in word:
            guesses+= newguess
            letCount +=1
            print("you guessed right!")
        else:
            turns-= 1
            print("You guessed wrong, you have ", turns, " turns left.")
        updateWord(word, guesses)
    if turns <0 :
        print("You lose, the word was ", word)
        sel=Menu()
    os.system('cls')
    score=10*wordCount+5*turns
    print("Your score is ", score)
    if score> maxScore:
        maxScore=score
        textFile = open("score.txt", "w")
        textFile.close()
        saveScore = (score)
        name = input('Enter your name. ').title()
        saveScore = input('You got a new high score. What was the number? ')
        textFile = open("score.txt", "a")#Opens the score file
        textFile.write("\n" + name + ' has the high score of ' + saveScore + "\n")
  
        print ("\n")
        textFile = open("score.txt", "r")
        whole = textFile.read()
        print (whole)
        textFile.close()
        print
    if score < maxScore:
        print("The high score is: ", maxScore)
    sel=Menu()

        
    