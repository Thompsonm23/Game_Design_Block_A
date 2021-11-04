#Maurice Thompson
#10/25/21
#We are making a program that displays the font and blit
import pygame as py, os, random, time

from pygame.display import set_mode 
os.system('cls')

py.init()
BLACK=(0,0,0)
WHITE=(250,250,250)
WIDTH= 600
HEIGHT=600
window=py.display,set_mode((WIDTH,HEIGHT))
py.display.set_caption("Settings Window")


TITLE_FONT= py.font.SysFont('comicsans', 80, bold=False, italic=False)#Title font
def display_message(message):#Font placement
    py.time.delay(100)
    text=TITLE_FONT.render(message, 1, WHITE)
    # window.blit(text,(WIDTH/2- text.get_width()/2, HEIGHT/2- text.get_height()/2))
    window.blit(text, (WIDTH/2-text.get_width()/2, HEIGHT/2-))
    py.display.update()
    py.time.delay(100)


run=True
#Main Loop
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run=False
            py.quit()
    display_message("Settings")
    window.fill(0,0,0)
    display_message("oops")
    py.time.delay(300)
    window.fill(0,0,0)
    display_message("AHHH")
py.quit
