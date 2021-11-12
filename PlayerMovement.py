#Maurice Thompson
#11/10/2021
import os, pygame as py

os.system('cls')
height=500
width=500
bg=py.image.load("images\\bg.jpg")
FIG1=py.image.load("images\\standing.png")
window=py.display.set_mode((height,width))
speed=5
run=True
while run:
    py.time.delay(10)
    for case in py.event.get():
        if case.type == py.QUIT:
            run=False
    keypressed= py.key.get_pressed()
    if keypressed [py.K_RIGHT]:
        speed+= FIG1.y

    window.blit(bg, (0,0))
    py.display.flip()
py.display.set_caption("Player Movement")
py.quit()
