from pygame import *
font.init()
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

speed_x = 3
speed_y = 3



win_width = 700
win_height= 500
display.set_caption("Ping pong")
window = display.set_mode((win_width,win_height))
racket_L = Racket('platform.png',  10,210,5,10,80)
racket_R = Racket('platform.png',  685,210,5,10,80)
ball = GameSprite('ball.png',  325,225,5,50,50)
back= (200,250,250)
window.fill(back)
clock= time.Clock()
FPS=60
game = True
finish = False
font_1 = font.Font(None,35)
lose1= font_1.render("первый проиграл!",True,(255,0,0))
lose2= font_1.render("второй проиграл!",True,(255,0,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        ball.rect.x+= speed_x
        ball.rect.y+= speed_y
        if ball.rect.y<0 or ball.rect.y>450:
            speed_y*=-1
        if sprite.collide_rect(ball,racket_L) or sprite.collide_rect(ball,racket_R):
            speed_x*= -1   
        window.fill(back)
        racket_L.update_l()
        racket_L.reset()
        racket_R.update_r()
        racket_R.reset()
        ball.reset()
        if ball.rect.x< 0: 
            finish = True 
            window.blit(lose1,(200,200)) 
             
        if ball.rect.x> 700-50: 
            finish = True 
            window.blit(lose2,(200,200))  
    display.update()
    clock.tick(FPS)