#Maurice Thompson
#10/7/21
#Open, write to, read from, append to, close() a file.
import os, time
#To create a file you must declare an object so we can open a file
#when you open a file you need to use 'w'
myFile= open('score.txt', 'w')
myFile.write("hello ther, my name is maurice \t what is yours")
myFile.close()

myFile= open('score.txt', 'w')
myFile.write("and now we will play a game")
myFile.close()

fileMy=open('score.txt', 'r')
print(fileMy.read())
fileMy.close()
anotherFile= open('score.txt', 'a')
anotherFile.write(" The highest score: \t" + str(score))