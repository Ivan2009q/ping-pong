from pygame import *

win_width = 700
win_height= 500
display.set_caption("Ping pong")
window = display.set_mode((win_width,win_height))
back= (200,250,250)
window.fill(back)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()