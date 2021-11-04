import pygame as py, os, random, time
from pygame import display
from pygame.constants import MOUSEBUTTONDOWN


os.system ('cls')
py.init()


colors= {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0),'purple':(125,0,125), 'white':(255,255,255) }
color= ['black','red','green','purple','white']
white=(250,250,250)
WIDTH = 600
HEIGHT = 600
win=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Square Chase")
messages=['Settings','Instructions','Level 1','Level 2','Scoreboard','Quit','Back']
ssmessages=['1280,900','400,400','600,600']
#Square Variables
wbox=25
hbox=25
square= py.Rect(10,10, wbox,hbox)

 

#capital letters = constant

#Default font = py.font.SysFont(name, size, bold=False, italic=False)

TITLE_FONT = py.font.SysFont('comicsans', 80)
SETTINGS_FONT= py.font.SysFont('comicsans',30)

def display_message(message):#Used for title size
    py.time.delay(100)
    #text = TITLE_FONT.pygame.font.render(text, antialias, color, background=None)
    text= TITLE_FONT.render(message, 1, white)
    win.blit(text, (WIDTH/2-text.get_width()/2, 10))
    py.display.flip()
    py.time.delay(100)
    #can have height at whatever, if you dont want your text dead center
def display_SmallFont(message, x,y):#Used for the small font setting
    py.time.delay(100)
    #text = TITLE_FONT.pygame.font.render(text, antialias, color, background=None)
    text= SETTINGS_FONT.render(message, 1, white)
    win.blit(text, (x,y))
    py.display.flip()
    py.time.delay(100)
Menu=True
def display_Menu():#Menu Function
    x=25
    y=160
    square.x=x
    square.y=y
    for i in range(0, len(messages)):
        display_message("Menu")
        display_SmallFont("Settings", 50,150)
        display_SmallFont("Instructions", 50,200)
        display_SmallFont("Level 1", 50,250)
        display_SmallFont("Level 2", 50,300)
        display_SmallFont("Scoreboard", 50,350)
        display_SmallFont("Exit", 50, 400)
        display_SmallFont("Back", 50, 450)
        word = messages[i]
        py.draw.rect(win, 'green', square)
        text=SETTINGS_FONT.render(word, 1, white)
        win.blit(text, (WIDTH+wbox+10, y))
        py.display.flip()
        y += 50
        square.y=y

def display_Back():
    display_SmallFont("Back", 50, 450)


run = True
Menu= True
Setting = False
WindowSize= False
Back= True
display_Menu()
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run = False
            py.quit()
    if eve.type==py.MOUSEBUTTONDOWN:
        mouse_pressed=py.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_position=py.mouse.get_pos()
            if Menu:
                if mouse_position[0]>25 and mouse_position[0]<=50 and mouse_position[1]>=459 and mouse_position[1]<=489:
                    win.fill('black')
                    display_Menu()
                    Menu=False
                    Setting=True
                    WindowSize=False
            if Setting: 
                if mouse_position[0]>25 and mouse_position[0]<=50 and mouse_position[1]>=159 and mouse_position[1]<=185:
                    Menu==False
                    Setting=True
                    WindowSize=False
                    win.fill('black')
                    display_message("Settings")
                    display_SmallFont("Window Size", 50,150)
                    display_Back()
                    py.display.set_caption("Settings")
            if WindowSize:
                if mouse_position[0]>25 and mouse_position[0]<=50 and mouse_position[1]>=159 and mouse_position[1]<=185:  
                    Menu=False
                    Setting=False
                    WindowSize=True
                    win.fill('black')
                    display_message("Window Size")
                    py.display.set_caption("Window Size")
                    display_SmallFont("1280 x 900", 50,150)
                    if mouse_position[0]>50 and mouse_position[0]<=175 and mouse_position[1]>=159 and mouse_position[1]<=185:
                        win=py.display.set_mode((1280,900))
py.quit()