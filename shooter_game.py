#Создай собственный Шутер!
from email.headerregistry import Group
from tokenize import group



from pygame import *
from random import randrange

window = display.set_mode((700,500))
display.set_caption("shooter")

mixer.init()
font.init()


bg = transform.scale(image.load("galaxy.jpg") , (700 , 500))

fonter = font.SysFont('Arial' , 30)
big_fonter = font.SysFont('Arial' , 50)


ticker = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self , player_image ,player_x , player_y , player_speed , sx , sy , mt):
        super().__init__()

        self.image = image.load(player_image)
        self.image = transform.scale( self.image , (sx,sy))

        self.speed = player_speed

        self.rect = self.image.get_rect()


        self.rect.x = player_x
        self.rect.y = player_y
        self.mt = mt
    def draw(self):
        window.blit(self.image , (self.rect.x , self.rect.y))
        
    def move(self, x , y):
        self.rect.x += x * self.speed
        self.rect.y += y * self.speed
    def update(self):
        if self.mt == 1:
            self.rect.y += self.speed
            if self.rect.y > 530:
                self.rect.x , self.rect.y = randrange(0 , 670) , 0
                global miss
                miss += 1
        elif self.mt == 2:
            self.rect.y -= self.speed
           





rocket = GameSprite("rocket1.png" , 325 , 430 , 10 , 65 , 70 , 0 )



bullet = GameSprite("bullet.png" , 325 , 430 , 10 , 25 , 20 ,2)
bullet1 = GameSprite("bullet.png" , 325 , 430 , 10 , 25 , 15 ,2)

visible = False
visible1 = None

Enemys = sprite.Group()



miss = 0
score = 0

alive = 0

winner = big_fonter.render('You Win! ' , True , (100,255,100))
loser = big_fonter.render('You Lose! ' , True , (255,100,100))


for b in range (5):
    mosn = GameSprite("ufo.png" ,randrange(0 , 650)  , 0 , randrange(1 , 2) , 50 , 30 , 1)
    Enemys.add(mosn)

while True:
    scoretxt = fonter.render('score: ' + str(score) , True , (255,255,255))
    loses = fonter.render('lost: ' + str(miss) , True , (255,255,255))

    Enemys.update()
    bullet.update()
    bullet1.update()
    
    
    
        
    window.blit(bg , (0,0))
    rocket.draw()
    for events in event.get():
        if events.type == QUIT:
            quit()
    if key.get_pressed()[K_LEFT] and rocket.rect.x > 10 and alive == 0:
        rocket.move(-1 , 0)
    if key.get_pressed()[K_RIGHT] and rocket.rect.x < 635 and alive == 0:
        rocket.move(1 , 0)
    if key.get_pressed()[K_UP] and alive == 0 :
        if visible == False:
            bullet = GameSprite("bullet.png" , rocket.rect.x , rocket.rect.y , 10 , 25 , 20 ,2)
            visible = True
        if visible1 == False:
            
            bullet1 = GameSprite("bullet.png" , rocket.rect.x , rocket.rect.y , 10 , 25 , 15 ,2)
            visible1 = True
    if bullet.rect.y < -30:
        visible = False
    if bullet1.rect.y < -30 and visible1:
        visible1 = False
    sprites_list = sprite.spritecollide(bullet , Enemys , False) +sprite.spritecollide(bullet1 , Enemys , False)


    if sprite.spritecollide(rocket , Enemys , False) or miss > 5:
        alive = 1

    if sprites_list:
        
        visible = False
    for enh in range(0,len(sprites_list)):
        if score == 20:
            rocket.image = image.load("rocket2.png")
            rocket.image = transform.scale( rocket.image , (65,70))
            visible1 = False
            mosn = GameSprite("ufo.png" ,randrange(0 , 650)  , 0 , randrange(1 , 3) , 50 , 30 , 1)
            Enemys.add(mosn)
        score += 1
        sprites_list[enh].rect.y = 0
        sprites_list[enh].rect.x = randrange(0 , 650)
    Enemys.draw(window)
    bullet.draw()
    bullet1.draw()
    if alive == 1:
        window.blit(loser , (260,250))
    if score > 40:
        window.blit(winner , (260,250))
        alive = 2

    window.blit(scoretxt , (0,0))
    window.blit(loses , (0,32))
        
    display.update()
    ticker.tick(60)
