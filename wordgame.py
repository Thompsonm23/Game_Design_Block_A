#Maurice Thompson
#Word game collum
import os
os.system('cls')
import random
 
answer = input("Do you want to play a game?")
 
words = ['blue','red','yellow','green','black','white']
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 3
while 'y' in answer:
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)  
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("You Win")
            print("The word is: ", word)
            break
        guess = input("guess a character:")
        guesses += guess

        if guess not in word:        
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You Loose")
    while 'n' in answer:
        print("thank you for playing")