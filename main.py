from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Racket(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed





win_width = 700
win_height= 500
display.set_caption("Ping pong")
window = display.set_mode((win_width,win_height))
racket_L = Racket('platform.png',  10,210,5,10,80)
racket_R = Racket('platform.png',  685,210,5,10,80)
back= (200,250,250)
window.fill(back)
clock= time.Clock()
FPS=60
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(back)
    racket_L.update_l()
    racket_L.reset()
    racket_R.update_r()
    racket_R.reset()
    display.update()
    clock.tick(FPS)