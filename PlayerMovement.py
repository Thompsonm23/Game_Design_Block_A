#Maurice Thompson
#11/10/2021
import os, pygame as py
py.init()

os.system('cls')

bg=py.image.load("images\\bg.jpg")
FIG1=py.image.load("images\\standing.png")
window=py.display.set_mode((500,480))
walkRight = [py.image.load('images\\R1.png'), py.image.load('images\\R2.png'), py.image.load('images\\R3.png'), py.image.load('images\\R4.png'), py.image.load('images\\R5.png'), py.image.load('images\\R6.png'), py.image.load('images\\R7.png'), py.image.load('images\\R8.png'), py.image.load('images\\R9.png')]
walkLeft = [py.image.load('images\\L1.png'), py.image.load('images\\L2.png'), py.image.load('images\\L3.png'), py.image.load('images\\L4.png'), py.image.load('images\\L5.png'), py.image.load('images\\L6.png'), py.image.load('images\\L7.png'), py.image.load('images\\L8.png'), py.image.load('images\\L9.png')]
speed=5
x=50
y=400
width=40
height=60
speed=5
jump=False
jumpcount=10
left=False
right=False
walkCount=10
clock = py.time.Clock()
def reGameWindow():
    global walkCount
    
    window.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  
        window.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        window.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        window.blit(FIG1, (x, y))
        walkCount = 0
        
    py.display.update() 
run=True
while run:
    clock.tick(27)
    py.time.delay(10)
    for case in py.event.get():
        if case.type == py.QUIT:
            run=False
    keypressed= py.key.get_pressed()
    if keypressed [py.K_LEFT] and x> speed:
        x -= speed
        left=True
        right=False
    elif keypressed [py.K_RIGHT] and x< 500 - speed - width:
        x += speed
        left=False
        right=True
    if not(jump):
        if keypressed [py.K_SPACE]:
            jump=True
            right=False
            Left=False
            walkCount=0
    else:
        if jumpcount >= -10:
            y -= (jumpcount *abs(jumpcount))*.5
            jumpcount-=1
        else:
            jumpcount = 10
            jump=False

    window.blit(bg, (0,0))
    py.display.flip()
py.display.set_caption("Player Movement")
py.quit()
