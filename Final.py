#Maurice Thompson
#11/18/21
import os, pygame#Import necessary librarys
pygame.init()

bg=pygame.image.load('images\\BG.png')#Bg image
Game1=pygame.image.load('images\\tiles.png')#Load tiles
bgw=pygame.image.load('images\\back-walls.png')
win=pygame.display.set_mode((700,600))#Bg size
walkleft=[pygame.image.load('images\\tile000 (2).png'),pygame.image.load('images\\tile001 (2).png'),pygame.image.load('images\\tile002 (2).png'),pygame.image.load('images\\tile003 (2).png'),pygame.image.load('images\\tile004 (2).png'),pygame.image.load('images\\tile005 (2).png')]#Walk Left
walkright=[pygame.image.load('images\\tile000.png'),pygame.image.load('images\\tile001.png'),pygame.image.load('images\\tile002.png'),pygame.image.load('images\\tile003.png'),pygame.image.load('images\\tile004.png'),pygame.image.load('images\\tile005.png')]#Walk Right
idle=[pygame.image.load('images\\tile000 (3).png'),pygame.image.load('images\\tile001 (3).png'),pygame.image.load('images\\tile002 (3).png'),pygame.image.load('images\\tile003 (3).png')]
ch=pygame.image.load('images\\tileidle.png')
clock = pygame.time.Clock()#For time and tempo
run=True#Set Boolean
jumping=False
jumpcount=10
x=0
y=280
vel=5

left=False
right=False
walkcount=0


def redrawGameWindow():#Used from jump program
    global walkcount
    win.blit(bg, (0,0))#Background
    if walkcount + 1 >= 18:
        walkcount = 0 
    if left:  
        win.blit(walkleft[walkcount//3], (x,y))
        walkcount += 1                          
    elif right:
        win.blit(walkright[walkcount//3], (x,y))
        walkcount += 1
    else:
        win.blit(ch, (x, y))
        walkcount = 0
    pygame.display.update() 

while run:
    clock.tick(18)#Clock tick in incriment of 3
    key=pygame.key.get_pressed()#To get key pressed 
    pygame.time.delay(10)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run=False
    if key[pygame.K_LEFT]: 
        x -= vel
        left = True
        right = False

    elif key[pygame.K_RIGHT]:
        x += vel
        left = False
        right = True
    else: 
        left = False
        right = False
        walkCount = 0
    redrawGameWindow()
    pygame.display.update()
    print(pygame.mouse.get_pos())
    
pygame.quit()
