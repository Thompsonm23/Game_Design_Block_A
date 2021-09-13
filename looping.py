#Maurice Thompson
#9/07/21
#Learn how to use looping
import os

os.system('cls')
star=int(input("How many stars ")) #type casting
print("stars", star)
line=star
for i in range(line):
    for space in range(i):
        print("   ", end= " ")
    for counter in range(star):
        print(" * ", end=" " )
    
        
    print()
    star-=1 #shortcut for minus 2
    #change whats in string using operators

print("Thank You! ")