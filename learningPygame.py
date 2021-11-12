#Maurice Thompson
#10/15/2021
#Learning Display,
#Opening windows,
#Changing size window
#Basic game loop

import os, pygame
import random

from pygame.draw import circle
os.system('cls')
#first thing to do is initialize pygame
pygame.init()
height= 600
width= 600
check=True#Color dictionary
colors= {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0),'purple':(125,0,125), 'white':(255,255,255) }
color= ['black','red','green','purple','white']
ranColor = random.choice(color)


while check:
    # height= input(("Height of the window(10-1000): "))
    # width= input(("width of your window(10-1000): "))
#Try and except
    try:
        height= int(height)
        width= int(height)
        color=str(color)
        check= False
    except ValueError:
        check=True
window=pygame.display.set_mode((width,height))
window.fill('black')
pygame.display.flip() #refresh window with new color
hbox=50
wbox=50
xc= random.randint(25,550)
yc= random.randint(25,550)
radius= hbox/2
speed=5
rect=pygame.Rect(width/2, height/2, wbox, hbox)
# #pygame.draw.rect(window, (150, 200, 20), rect)
# pygame.draw.rect(window, (colors.get('green')), rect)
pygame.draw.circle(window, colors.get('red'), (xc,yc), radius)

pygame.display.flip()
run=True
Jumping=False
jumpCount=10#Boolean to check for jump





#Main loop
while run:
    pygame.time.delay(20)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run=False
    keyPressed = pygame.key.get_pressed()
    if not(Jumping):
        if keyPressed [pygame.K_UP]:
            rect.y -=speed
        if keyPressed [pygame.K_DOWN]:#Keys for controlling the square
            rect.y +=speed
        if keyPressed [pygame.K_SPACE]:
            Jumping=True
    else:
        if jumpCount >=-10:
            if jumpCount < 0:
                rect.y -= jumpCount* abs(jumpCount)*0.5
                jumpCount -= 1
            else:
                jumpCount =10
                Jumping=False
    if keyPressed [pygame.K_RIGHT]:
        rect.x +=speed
    if keyPressed [pygame.K_LEFT]:
        rect.x -=speed
    if keyPressed [pygame.K_w] and yc >0+radius:
        yc -=speed
    if keyPressed [pygame.K_s] and yc < height-radius :#Keys for controlling the square
        yc +=speed
    if keyPressed [pygame.K_d] and xc <width-radius:
        xc +=speed
    if keyPressed [pygame.K_a] and xc >0+radius:
        xc -=speed
    if rect.y <= 0:
        rect.y = height-50
    if rect.y >= height:
        rect.y = 0
    if rect.x <= 0:
        rect.x=width-50
    if rect.x >= width:
        rect.x = 0
#collision and game end
    collide= rect.collidepoint(xc,yc)
    if collide:
        radius= (radius+25)
        rect.x= random.randint(25,550)
        rect.y= random.randint(25,550)
    if radius >= (hbox/2+125):
        run = False
        print("You win!")
    #repeted backround fill
    window.fill('black')
    pygame.display.flip
    pygame.draw.rect(window, (colors.get('green')), rect)
    pygame.draw.circle(window, colors.get('red'), (xc,yc), radius)
    pygame.display.flip()   
  

pygame.quit()
