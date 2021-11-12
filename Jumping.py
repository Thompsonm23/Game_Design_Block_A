import os,pygame,random
from pygame import color
from pygame import key
from pygame.constants import BLEND_ALPHA_SDL2
from pygame.draw import circle
os.system('cls')
#first thing to do is to initialize pygame
pygame.init()

height= 500
width=500
boulder=pygame.Rect(width-300,height-200,100,200)
check=True
colors = {'black': (0,0,0), 'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'purple': (153,51,255), 'white': (255,255,255)}
    #this is the long way of making a list from a dictionary
coloringsheet = ['black', 'red', 'blue', 'green', 'purple', 'white'] #this is to make a list of the colors
boulderColor=('blue')
window=pygame.display.set_mode ((height,width))
pygame.draw.rect(window, boulderColor, boulder)
GREEN = (0,255,0)
bg=pygame.image.load("images\\bgSmaller.jpg")
window.blit(bg, (0,0))
FIG=pygame.image.load("images\\standing.png")
window.blit(FIG, (100,100))

#color=coloringsheet.get(str(color))

 

while check:

   

    height =  500

    width = 500

   

    #whatColor = random.choice (coloringsheet)

    #whatColor = input ("what color do you want? ")

 

    #can also do whatColor = list(random.choice (colors)) if you didnt create coloringsheet

    #beginning of window is (0,0) opposite corner is (1000,1000). Origin is not the center

    check=True

   

    try:

        height=int(height)

        width=int(width)

        color=str(color)

        check=False

    except ValueError:

        check = True


window.fill((GREEN))

window

# Every computer runs on RGB

# 255 is max in decimal

# FF is max in hexadecimal

pygame.display.flip() #refresh window with new color

hbox=50

wbox=50

speed=5

x=width/2

y=height/2

rect=pygame.Rect(width/2, height/2, wbox, hbox)

#pygame.draw.rect(window, (150, 200, 20), rect)

pygame.draw.rect(window, (colors.get('white')), rect)

pygame.display.flip()

xc=random.randint(0,450)

yc=random.randint(0,450)

radius = wbox/2

pygame.draw.circle(window,colors.get('purple'), (xc,yc), radius)

Jumping = False

jumpcount = 10

pygame.display.flip()

 

run = True

game = 5

#This is the main loop for the game:

while run:
    pygame.time.delay(10) #1000 miliseconds
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run= False
    #how to get the position of the mouse
    # x,y=pygame.mouse.get_pos()
    # print("("+str(x)+ ","+ str(y)+ ")")
    #the mouse position is the only way to figure out if they are clicking in the right spot
    keypressed= pygame.key.get_pressed()
    if keypressed [pygame.K_RIGHT] and rect.x<800:
        rect.x += speed
    if keypressed [pygame.K_LEFT]:
        rect.x -= speed
    if not(Jumping):
        if keypressed [pygame.K_UP]:
            rect.y -= speed
        if keypressed [pygame.K_DOWN] and rect.y<800:
            rect.y += speed
        # For Jumpming
        if keypressed [pygame.K_SPACE]:
            Jumping = True
    else:
        if jumpcount >= -10:
            rect.y -= jumpcount* abs(jumpcount)*0.5
            # ** = squared
            # abs = absolute value
            jumpcount -= 1
        else:
            jumpcount =10
            Jumping = False
    if keypressed [pygame.K_a] and xc>25:
        xc -= speed
    if keypressed [pygame.K_d] and xc<775:
        xc += speed
    if keypressed [pygame.K_w] and yc>25:
        yc -= speed
    if keypressed [pygame.K_s] and yc<775:
        yc += speed
    point = (xc,yc)
    if radius > 125:
        run = False
        print ()
        print ("CIRCLE \nIS \nTHE \nCHAMPION!!!")
        print ()
    window.blit(bg, (0,0))
    window.blit(FIG, (100,100))
    # pygame.draw,circle(window,colors.get('purple'), (xc,yc), radius)
    pygame.draw.rect(window, (colors.get('white')), rect)
    pygame.draw.rect(window, (boulderColor), boulder)
    pygame.display.flip()
    if rect.y>500:
        rect.y= 0
    if rect.y<0:
        rect.y =500
    if rect.x>500:
        rect.x=0
    if rect.x<0:
        rect.x=450
    #to get the circle to eat the rectangle
pygame.display.set_caption("My game Window")
pygame.quit()