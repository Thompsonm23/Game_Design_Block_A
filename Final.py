#Maurice Thompson
#11/18/21
import os, pygame, time

from pygame import display#Import necessary librarys
pygame.init()
os.system('cls')
bg=pygame.image.load('images\\BG.png')#Bg image
bgwidth,bgheight=bg.get_rect().size
Game1=pygame.image.load('images\\tiles.png')#Load tiles
bgw=pygame.image.load('images\\back-walls.png')
W,H=700,600
win=pygame.display.set_mode((W,H))#Bg size
TITLE_FONT= pygame.font.SysFont('comicsans', 80, bold=False, italic=False)#imported from windowPygameFont#Below are all of the images and music files used within the program
walkleft=[pygame.image.load('images\\tile000 (2).png'),pygame.image.load('images\\tile001 (2).png'),pygame.image.load('images\\tile002 (2).png'),pygame.image.load('images\\tile003 (2).png'),pygame.image.load('images\\tile004 (2).png'),pygame.image.load('images\\tile005 (2).png')]#Walk Left
walkright=[pygame.image.load('images\\tile000.png'),pygame.image.load('images\\tile001.png'),pygame.image.load('images\\tile002.png'),pygame.image.load('images\\tile003.png'),pygame.image.load('images\\tile004.png'),pygame.image.load('images\\tile005.png')]#Walk Right
idle=[pygame.image.load('images\\tile000 (3).png'),pygame.image.load('images\\tile001 (3).png'),pygame.image.load('images\\tile002 (3).png'),pygame.image.load('images\\tile003 (3).png')]
island=pygame.image.load('images\\2.png')
dirt=pygame.image.load('images\\5.png')
pause=pygame.image.load('images\\pause.png')
coin=pygame.image.load('images\\goldCoin5.png')
coinding=pygame.mixer.Sound('images\\coin_ding.wav')
death=pygame.mixer.Sound('images\\scream.wav')
click=pygame.mixer.Sound('images\\Click.wav')
spike=pygame.image.load('images\\spike A.png')
powerup=pygame.image.load('images\\PowerUp.png')
heart=pygame.image.load('images\\heart.png')
ch=pygame.image.load('images\\tileidle.png')
emote=[pygame.image.load('images\\tile007.png'),pygame.image.load('images\\tile008.png'),pygame.image.load('images\\tile009.png'),pygame.image.load('images\\tile010.png'),pygame.image.load('images\\tile011.png'),pygame.image.load('images\\tile012.png')]
pygame.mixer.music.load('images\\music.wav')#Music File
hehe=pygame.mixer.Sound('images\\hehe.wav')
jumpsound=pygame.mixer.Sound('images\\jump.wav')
GameOver=pygame.mixer.Sound('images\\Game Over.wav')
Powerp=pygame.mixer.Sound('images\\Powerp.wav')
G_o=pygame.image.load('images\\G_O.png')
winn=pygame.image.load('images\\win.png')
winns=pygame.mixer.Sound('images\\winns.wav')
CoinStack=pygame.image.load('images\\stackgold.png')
startb=pygame.image.load('images\\startb.png')
back=pygame.image.load('images\\back.png')
menub=pygame.image.load('images\\menu.png')
arrows=pygame.image.load('images\\arrows.png')
MenuMain=pygame.image.load('images\\Mainm.png')
junglemusic=pygame.mixer.Sound('images\\Jungle Music.wav')
pausem=pygame.image.load('images\\pausem.png')
junglewood=pygame.image.load('images\\Jungle wood.png')
MusicB=pygame.image.load('images\\playpause.png')
InsTxt=pygame.image.load('images\\InsText.png')
BgB=pygame.image.load('images\\BgB.png')
ss=pygame.image.load('images\\ss.png')
ssizes=pygame.image.load('images\\Scree Sizes.png')
rect= ch.get_rect()
rectIsland=pygame.Rect((0,320),(120,466))
collide=rect.collidepoint(170,305)
clock = pygame.time.Clock()#For time and tempo
run=True#Set Boolean
jumping=False
jumpcount=10#Jumpcount
rect.x=0
rect.y=280#Starting Position
vel=5#Speed of movement
e=False#Emote
IDl=False#Idle
left=False
right=False
Level1=False#Below are all of the booleans for the menus and levels within the program
Level2=False
livecount=3
walkcount=0#Walkcount
coins=True
Music=True
Pause=False#Pause menu boolean
go=False
pup=True
Gameovr=False
Finish=False
Menu=True
Setting=False
Ins=False
ScreenS=False
Live1,Live2,Live3=True,True,True#Live count
coincounter=0
current_time=0
jumps=0
backb=False
SCORE_FONT = pygame.font.SysFont('comicsans', 80)
myFile= open('score.txt', 'w')
myFile.close()





def MenuM():#Function used for the menu images
    pygame.display.set_caption("Jungle Rush")
    win.blit(bg, (0,0))
    win.blit(MenuMain, (100,0))
def Back():#Image for back button
    win.blit(back, (20,520))

def Lev1():#Platforms for level 1 and Obstacles
    pygame.display.set_caption("Level 1")
    win.blit(pause, (0,0))
    win.blit(spike, (125,520))
    win.blit(spike, (150,520))
    win.blit(spike, (335,520))
    win.blit(spike, (380,520))
    win.blit(spike, (575,520))
    if Live1:#Pictures of hearts in top left corner
        win.blit(heart, (100,0))
    if Live2:
        win.blit(heart, (175,0))
    if Live3:
        win.blit(heart, (250,0))
    win.blit(island, (0,320))
    win.blit(dirt, (0,440))
    win.blit(dirt,(0,560))
    win.blit(dirt,(120,560))
    win.blit(island, (215,320))
    win.blit(dirt, (215,440))
    win.blit(dirt, (215,560))
    win.blit(dirt,(335,560))
    win.blit(island, (445,320))
    win.blit(dirt, (445,440))
    win.blit(dirt, (445,560))
    win.blit(dirt,(565,560))
    win.blit(island, (645,320))
    win.blit(dirt, (645,440))
    win.blit(dirt, (645,560))
    if coins:#Images of coins with boolean so that it disapears when collided
        win.blit(coin, (490, 200))
    pygame.display.update()
def Lev2():#Images for background and platforms for level 2 
    pygame.display.set_caption("Level 2")
    win.blit(pause, (0,0))
    if Live1:
        win.blit(heart, (100,0))
    if Live2:
        win.blit(heart, (175,0))
    if Live3:
        win.blit(heart, (250,0))
    win.blit(spike, (120,520))
    win.blit(spike, (300,520))
    win.blit(spike, (350,520))
    win.blit(spike, (400,520))
    win.blit(spike, (450,520))
    win.blit(island, (0,320))
    win.blit(dirt, (0,440))
    win.blit(dirt,(0,560))
    win.blit(island, (180,320))
    win.blit(dirt,(180,440))
    win.blit(dirt,(180,560))
    win.blit(island, (500,320))
    win.blit(dirt,(500,440))
    win.blit(dirt,(500,560))
    win.blit(island, (600,320))
    win.blit(dirt,(600,440))
    win.blit(dirt,(600,560))
    win.blit(dirt,(100,560))
    win.blit(dirt,(380,560))
    win.blit(dirt,(280,560))
    if coins:
        win.blit(coin, (350, 200))
    if pup:#Power up image with Boolean
        win.blit(powerup, (220, 225))
    pygame.display.update()
def updateFile():#This is used for the high score 
    f = open('score.txt','r') 
    file = f.readlines()
    last = int(file[0]) 

    if last > int(score): 
        f.close()
        file = open('score.txt', 'w') 
        file.write(str(score))
        file.close() 

        return score
               
    return last
def GameOv():#Game Over function with sound and images
    win.fill((0,0,0))
    win.blit(G_o, (100,25))
    win.blit(startb,(200,400))
    win.blit(menub, (400,405))
    pygame.display.set_caption("Game Over")#Caption for the window
    pygame.mixer.music.pause()
    pygame.mixer.Sound.play(GameOver)
    pygame.display.update()
def Winner():#Finish screen once you reach the end
    win.fill((0,0,0))
    win.blit(winn, (165,25))
    win.blit(startb, (200,400))
    win.blit(menub, (400,405))
    score=jumps+coincounter#Scoring system
    if Live2==False:
        score+=5
    if Live3==False:
        score+=5
    myFile= open('score.txt', 'w')
    myFile.write(str(score))
    myFile.close()
    largeFont = pygame.font.SysFont('comicsans', 80)
    lastScore = largeFont.render('Best Score: ' + str(updateFile()),1,(255,255,255))
    win.blit(lastScore, (W/2 - lastScore.get_width()/2,150))
    My_Score= SCORE_FONT.render(str(score), True, (250,250,250))
    win.blit(My_Score, (W/2.25,75 ))
    # myFile= open('score.txt', 'w')
    # myFile.write(str(score))
    # myFile.close()

    pygame.display.set_caption("Winner")
    pygame.mixer.Sound.play(winns)
    pygame.mixer.music.pause()
def Pausem():#In game pause menu with replay feture and main menu ability
    win.blit(bg, (0,0))
    win.blit(pausem, (130,50))
    pygame.display.set_caption("Paused")
    pygame.display.update()
def Instructions():#Images for the instruction menu
    win.blit(bg, (0,0))
    win.blit(junglewood, (25,40))
    win.blit(arrows, (225,160))
    win.blit(InsTxt, (215,225))
    pygame.display.set_caption("Instructions")
    Back()
    pygame.display.update()
def Settings():#Settings menu with buttons for screen size, background, and play/pause music
    win.blit(bg, (0,0))
    win.blit(junglewood, (25,40))
    win.blit(MusicB, (300,200))
    win.blit(BgB, (292,275))
    win.blit(ss, (200,225))
    pygame.display.set_caption("Settings")
    Back()
    pygame.display.update()
def ScreenSize():#Used for screen size button
    win.blit(bg, (0,0))
    win.blit(junglewood, (25,40))
    win.blit(ssizes, (270,175))
    Back()
    pygame.display.set_caption("Screen Size")
    pygame.display.update()
def Lev1fall():#Level 1 Collision
    if rect.x>=127 and rect.x<=190 and rect.y>=279 or rect.x>=343 and rect.x<=426 and rect.y>=279 or rect.x>=573 and rect.x<=625 and rect.y>=279 or rect.y>=300:#Fall
        rect.y -= (jumpcount* abs(jumpcount)*0.25)-50
        rect.x+=0
        rect.x-=0
        livecount-1
    if rect.x<=127 and rect.x>=190 and rect.y>=310:
        rect.x=0
        rect.y=280
    if rect.y>=529:
        rect.x=0
        rect.y=280
    if rect.x<=127 and rect.x>=190 and rect.y<=278 or rect.x<=343 and rect.x>=426 and rect.y<=278 or rect.x<=573 and rect.x>=625 and rect.y<=278:
        rect.x=0
        rect.y=280
def Lev2fall():#Level 2 collision
    if rect.x>=127 and rect.x<=160 and rect.y>279 or rect.x>=310 and rect.x<=480 and rect.y>=279 or rect.y>=300:
        rect.y -= (jumpcount* abs(jumpcount)*0.25)-50
        rect.x+=0
        rect.x-=0
        livecount-1
    if rect.y>=529:
        rect.x=0
        rect.y=280
#     if 
if Pause:#Bellow are the booleans for all menus and buttons. Makes it easy for if something is true all the other things are false
    Level1=False
    Level2=False
    Gameovr=False
    Finish=False
    Menu=False
if Level1:
    Level2=False
    Pause=False
    Gameovr=False
    Finish=False
    Menu=False
if Gameovr:
    Level1=False
    Level2=False
    Pause=False
    Finish=False
    Menu=False
if Finish:
    Level1=False
    Level2=False
    Pause=False
    Gameovr=False
    Menu=False
if Menu:
    Level1=False
    Level2=False
    Pause=False
    Finish=False
    GameOvr=False
if Ins:
    Level1=False
    Level2=False
    Pause=False
    Finish=False
    GameOvr=False
    Menu=False
    backb=True
if Setting:
    Level1=False
    Level2=False
    Pause=False
    Ins=False
    Finish=False
    GameOvr=False
    Menu=False
    backb=True
if ScreenS:
    Level1=False
    Level2=False
    Pause=False
    Ins=False
    Finish=False
    GameOvr=False
    Menu=False
    Setting=False
    backb=True
if Music:
    pygame.mixer.music.play(5)
if Music==False:
    pygame.mixer.music.stop()

def redrawGameWindow1():#Used from jump program and animations
    global walkcount
    win.blit(bg, (0,0))#Background
    Lev1()
    if walkcount + 1 >= 18:
        walkcount = 0 
    if left:  
        win.blit(walkleft[walkcount//3], (rect.x,rect.y))
        walkcount += 1                          
    elif right:
        win.blit(walkright[walkcount//3], (rect.x,rect.y))
        walkcount += 1
    elif IDl:
        win.blit(ch, (rect.x, rect.y))
        walkcount = 0
    if e:
        win.blit(emote[walkcount//3], (rect.x,rect.y))
        walkcount=0
    
    pygame.display.update() 
def redrawGameWindow2():#Used from jump program
    global walkcount
    win.blit(bg, (0,0))#Background
    Lev2()
    if walkcount + 1 >= 18:
        walkcount = 0 
    if left:  
        win.blit(walkleft[walkcount//3], (rect.x,rect.y))
        walkcount += 1                          
    elif right:
        win.blit(walkright[walkcount//3], (rect.x,rect.y))
        walkcount += 1
    elif IDl:
        win.blit(ch, (rect.x, rect.y))
        walkcount = 0
    if e:
        win.blit(emote[walkcount//3], (rect.x,rect.y))
        walkcount=0
    pygame.display.update() 
while run:#Main run loop for game containing all key components
    clock.tick(30)#Clock tick in incriment of 3
    key=pygame.key.get_pressed()#To get key pressed 
    pygame.time.delay(10)
    if Menu:#Main Menu
        Pause=False
        MenuM()
        pygame.display.update()
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run=False
    current_time = pygame.time.get_ticks()
    if key[pygame.K_LEFT]:#Controls
        rect.x-=vel 
        left = True
        right = False


    elif key[pygame.K_RIGHT]:
        rect.x += vel
        left = False
        right = True

    else: 
        left = False
        right = False
        e=False
        IDl=True
        walkCount = 0
    if not(jumping):#Jumping with sound
        if key[pygame.K_SPACE] and rect.y<=280 and rect.x>=2:
            pygame.mixer.Sound.play(jumpsound)
            jumping = True
            left = False
            right = False
            e=False
            walkCount = 0
            jumps+=1
    else:#Jump count and jumping height
        if jumpcount >= -10:
            rect.y -= (jumpcount* abs(jumpcount)*0.25)-.5
            jumpcount -= 1
        else:
            jumpcount =10
            jumping = False
    if key[pygame.K_e]:
        e=True
        IDl=False
        pygame.mixer.Sound.play(hehe)
    if key[pygame.K_MINUS]:
        Level1=True
        Level2=False
    if pup:
        vel=5
    if Pause:#Boolean for pause menu
        win.fill((0,0,0))
        Pausem()
    if Level1:#Level1 for if its true, live count, power pup, uses redrawgamewindow1() and Lev1fall()
        redrawGameWindow1()
        Lev1fall()
        pup=True
        Pause=False
        Gameovr=False
        if rect.x>=470 and rect.x<=500 and rect.y<=240 and coins==True:#Coin collecting method
            coins=False
            coincounter-=2
            pygame.mixer.Sound.play(coinding)
        if rect.y>=500:#Death and Sound with livecount change
            livecount-=1
            pygame.mixer.Sound.play(death)
        if livecount==3:
            Live1,Live2,Live3=True,True,True
        if livecount==2:
            score=+5
            Live1=True
            Live2=True
            Live3=False
        if livecount==1:
            score=+5
            Live1=True
            Live2=False
            Live3=False
        if livecount==0:
            Live1=False
            Live2=False
            Live3=False
            Level1=False
            Level2=False
            GameOv()
            Gameovr=True
    if Level1 and rect.x==0:
        current_time=pygame.time.get_ticks()

    if Level2:#All stuff necessary for level 2 to work
        redrawGameWindow2()
        Lev2fall()
        if rect.x>=180 and rect.x<=250 and rect.y>=225 and rect.y<=240 and pup==True:
            pup=False
            pygame.mixer.Sound.play(Powerp)
        if rect.x>=370 and rect.x<=395 and rect.y<=240 and coins==True:
            coins=False
            coincounter-=1
            pygame.mixer.Sound.play(coinding)          
        if pup==False:#Power up change in speed
            vel=10
        if rect.y>=500:#Death and Sound with livecount change
            livecount-=1
            pygame.mixer.Sound.play(death)
        if livecount==3:
            Live1,Live2,Live3=True,True,True
        if livecount==2:
            Live1=True
            Live2=True
            Live3=False
        if livecount==1:
            Live1=True
            Live2=False
            Live3=False
        if livecount==0:
            Live1=False
            Live2=False
            Live3=False
            Level1=False
            Level2=False
            pup=True
            GameOv()#Function for if you loose all lives the game over menu appears
            Gameovr=True
    if rect.x==680 and Level1:#This teleports you to level 2 once you reach a certain spot
        rect.x=0
        Level1=False
        Level2=True
        coins=True
        pup=True
    if rect.x>=680 and Level2:#Finish line
        Level2=False
        Level1=False
        Pause=False
        Gameovr=False
        Finish=True
        coins=True
        pup=True
        Winner()
        pygame.display.update()

    if case.type==pygame.MOUSEBUTTONDOWN:#All controls for button in menu, pause menu, and both the game over and finish menu
        mouse_pressed=pygame.mouse.get_pressed()
        mouse_position=pygame.mouse.get_pos()
        if mouse_pressed[0] and Level1 or mouse_pressed[0] and Level2:#Corner pause button working
            if mouse_position[0]>20 and mouse_position[0]<=77 and mouse_position[1]>=0 and mouse_position[1]<=63:
                Level1=False
                Level2=False
                Gameovr=False
                backb=False
                Pause=True
                Finish=False
                pygame.display.update()
        if mouse_pressed[0] and Gameovr or mouse_pressed[0] and Finish:#Menu and start button on game over and finish screen
            pygame.mixer.Sound.play(click)
            if mouse_position[0]>211 and mouse_position[0]<=291 and mouse_position[1]>=413 and mouse_position[1]<=442:
                livecount=3
                coincounter=0
                jumps=0
                rect.x=0
                Finish=False
                Gameovr=False
                Pause=False
                coins=True
                Level1=True
                Level2=False
                pup=True
                current_time=0
                Lev1()
                pygame.mixer.Sound.stop(winns)
                pygame.mixer.Sound.stop(GameOver)
                if Music==True:
                    pygame.mixer.music.play(5)
                pygame.display.update()
            if mouse_position[0]>410 and mouse_position[0]<=475 and mouse_position[1]>=410 and mouse_position[1]<=445:
                pygame.mixer.Sound.stop(winns)
                pygame.mixer.Sound.stop(GameOver)
                if Music==True:
                    pygame.mixer.music.play(5)
        if mouse_pressed[0] and Pause:#This is the pause menu
            pygame.mixer.Sound.play(click)
            if mouse_position[0]>=195 and mouse_position[0]<=480 and  mouse_position[1]>=100 and mouse_position[1]<=182:#Resume
                Level1=True
                Finish=False
                Gameovr=False
                Pause=False
                Lev1()
            if mouse_position[0]>=195 and mouse_position[0]<=480 and  mouse_position[1]>=290 and mouse_position[1]<=370:#Restart game
                livecount=3
                coincounter=0
                jumps=0
                rect.x=0
                Finish=False
                Gameovr=False
                Pause=False
                coins=True
                Level1=True
                Level2=False
                Menu=False
                pup=True
                current_time=0
                Lev1()
                pygame.display.update()
        if mouse_pressed[0] and Gameovr or mouse_pressed[0] and Finish or mouse_pressed[0] and Pause:#Menu from Finish, Game Over, and pause
            pygame.mixer.Sound.play(click)
            if mouse_position[0]>195 and mouse_position[0]<=480 and mouse_position[1]>=385 and mouse_position[1]<=465:
                pygame.mixer.Sound.stop(GameOver)
                pygame.mixer.Sound.stop(winns)
                if Music==True:
                    pygame.mixer.music.play(5)
                Menu=True
        if mouse_pressed[0] and Menu:#Buttons for menu screen (Restart, Help, Settings, Exit)
            pygame.mixer.Sound.play(click)
            if mouse_position[0]>240 and mouse_position[0]<=465 and mouse_position[1]>=338 and mouse_position[1]<=392:
                pygame.quit()
            if mouse_position[0]>240 and mouse_position[0]<=465 and mouse_position[1]>=172 and mouse_position[1]<=208:
                livecount=3
                coincounter=0
                jumps=0
                rect.x=0
                Finish=False
                Gameovr=False
                Pause=False
                coins=True
                Level1=True
                Level2=False
                Menu=False
                pup=True
                current_time=0
                Lev1()
                pygame.mixer.Sound.stop(junglemusic)
                pygame.display.update()
            if mouse_position[0]>240 and mouse_position[0]<=465 and mouse_position[1]>=300 and mouse_position[1]<=335:
                Ins=True
                Menu=False
                Music=False
                Instructions()
        if mouse_pressed[0] and Ins or mouse_pressed[0] and Setting:
            if mouse_position[0]>20 and mouse_position[0]<=81 and mouse_position[1]>=520 and mouse_position[1]<=583:
                Ins=False
                Menu=True
                MenuM()
        if mouse_pressed[0] and Menu:
            if mouse_position[0]>240 and mouse_position[0]<=465 and mouse_position[1]>=237 and mouse_position[1]<=273:
                Menu=False
                Setting=True
                Settings()
        if mouse_pressed[0] and Setting and Menu==False:#This is the settings button with functions
            pygame.mixer.Sound.play(click)
            if mouse_position[0]>300 and mouse_position[0]<=350 and mouse_position[1]>=200 and mouse_position[1]<=250:
                Music=True
                pygame.mixer.music.play(5)
            if mouse_position[0]>360 and mouse_position[0]<=408 and mouse_position[1]>=200 and mouse_position[1]<=250:
                Music=False
                pygame.mixer.music.stop()
            if mouse_position[0]>297 and mouse_position[0]<=342 and mouse_position[1]>=280 and mouse_position[1]<=333:
                bg=pygame.image.load('images\\BG.png')
            if mouse_position[0]>371 and mouse_position[0]<=415 and mouse_position[1]>=280 and mouse_position[1]<=333:
                bg=pygame.image.load('images\\Forest.jpg')
            if mouse_position[0]>210 and mouse_position[0]<=253 and mouse_position[1]>=225 and mouse_position[1]<=290:
                ScreenS=True
                Setting=False
                ScreenSize()
        if mouse_pressed[0] and ScreenS and Setting==False:#Screen size menu
            if mouse_position[0]>20 and mouse_position[0]<=81 and mouse_position[1]>=520 and mouse_position[1]<=583:
                Setting=True
                Menu=False
                Settings()
        if mouse_pressed[0] and ScreenS and Setting==False:
            if mouse_position[0]>270 and mouse_position[0]<=430 and mouse_position[1]>=190 and mouse_position[1]<=217:
                W=700
                H=600
                win=pygame.display.set_mode((W,H))
            if mouse_position[0]>270 and mouse_position[0]<=430 and mouse_position[1]>=233 and mouse_position[1]<=257:
                W=800
                H=700
                win=pygame.display.set_mode((W,H))
            if mouse_position[0]>270 and mouse_position[0]<=430 and mouse_position[1]>=275 and mouse_position[1]<=304:
                W=900
                H=800
                win=pygame.display.set_mode((W,H))
    # print(pygame.mouse.get_pos())
    # print(score)
    # print(rect.y)
    # print(current_time/1000)
pygame.quit()
