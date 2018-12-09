# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 17:04:15 2018

@author: bruno
"""

import sys, pygame
import random
#import time

pygame.init()

size = width, height = 500, 700

black = 0, 0, 0

pygame.mixer.music.load("mario.MP3")
pygame.mixer.music.play(-1)
bullet_sound  = pygame.mixer.Sound("TIRO.wav")
level_sound  = pygame.mixer.Sound("level_up.wav")

pontos=0

class Tiro(pygame.sprite.Sprite):
    def __init__(self,cordenada):
        pygame.sprite.Sprite.__init__(self)
        self.speedup = [0,-5]
        imagem_tiro = pygame.image.load("tiro.png")
    
        self.image=pygame.transform.scale(imagem_tiro, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x=cordenada[0]
        self.rect.y=cordenada[1]
    def update(self):
        if self.rect.y> -250:
            self.rect = self.rect.move(self.speedup) 


class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.tiro_grupo=pygame.sprite.Group()
        self.speedR = [3,0]
        self.speedL = [-3,0]
        self.speedU = [0,-3]
        self.speedD = [0,3]
        iimage = pygame.image.load("galaga_nave.png")
        self.image=pygame.transform.scale(iimage, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 295
        self.rect.y = 550  
        
    def move_direita(self):
        if self.rect.right < width:
            self.rect = self.rect.move(self.speedR)
    def move_cima(self):
        if self.rect.top > 0:
            self.rect = self.rect.move(self.speedU)
    def move_baixo(self):
        if self.rect.bottom < height:
            self.rect = self.rect.move(self.speedD)
    def move_esquerda(self):   
        if self.rect.left > 0:
            self.rect = self.rect.move(self.speedL)
    def atira(self):   

        tiro=Tiro([self.rect[0]+12,self.rect[1]-15])
        self.tiro_grupo.add(tiro)
        
class Inimigo(pygame.sprite.Sprite):        
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed =[random.randint(0,2),2 ]
        self.image=pygame.transform.scale(pygame.image.load("Enemy.png"), (39, 39))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width-35)
        self.rect.y = -40
        
    def update(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left == 0 or self.rect.right == width:
            self.rect[1] += 20
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]


clock = pygame.time.Clock()   
FPS=120
tempo = pygame.time.Clock()   

screen = pygame.display.set_mode(size)

fonte=pygame.font.SysFont('comicsans',30,True,True)
BackGround = pygame.image.load('Fundo.png') 

loop_tiro=0
loop_inimigo=0


nave = Nave()
nave_grupo=pygame.sprite.Group()
nave_grupo.add(nave)

inimigo=Inimigo()
inimigo_grupo=pygame.sprite.Group()
inimigo_grupo.add(inimigo)
nivel1, nivel2, nivel3, nivel4, nivel5= 200, 100, 60, 45, 30
level=nivel1
nivel='Nivel 1'
fonte2=pygame.font.SysFont(nivel,30,True,True)

end_it=False
while (end_it==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()       
            pygame.display.quit()
            sys.exit()
    
    myfont=pygame.font.SysFont("Britannic Bold", 100)
    myfonty=pygame.font.SysFont("Arial Bold", 45)
    titulo = myfont.render("Galagazinho", 1, (255, 255, 0))
    Sub_titulo = myfonty.render("Pressione barra para começar", 1, (255, 255, 255))
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_SPACE]:
            end_it=True
    screen.blit(BackGround,(0,0))
    screen.blit(titulo,(30,220))
    screen.blit(Sub_titulo,(30,340))
    pygame.display.flip()
    screen.fill(black)
    

while 1:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()       
            pygame.display.quit()
            sys.exit()
    keys=pygame.key.get_pressed()
    
    if pontos == 100 or pontos == 300 or pontos == 1000 or pontos == 1500 :
         level_sound.play()
    if pontos >= 100 :
        level=nivel2
        nivel='Nivel 2'
    if pontos >= 300 :
        level=nivel3
        nivel='Nivel 3'
    if pontos >= 1000 :
        level=nivel4
        nivel='Nivel 4'
    if pontos >= 1500 :
        level=nivel5
        nivel='Nivel 5'
    if pontos >= 1500 :
        level=nivel5
        nivel='Vai morrer!!!'
    
    if loop_inimigo == 0 and nivel == 'Vai morrer!!!':
        inimigo=Inimigo()
        inimigo_grupo.add(inimigo)
        inimigo=Inimigo()
        inimigo_grupo.add(inimigo)
        inimigo=Inimigo()
        inimigo_grupo.add(inimigo)
        inimigo=Inimigo()
        inimigo_grupo.add(inimigo)
        loop_inimigo+=1
    if loop_inimigo > 0 and nivel == 'Vai morrer!!!':
        loop_inimigo +=1
    if loop_inimigo > 20 and nivel == 'Vai morrer!!!':
        loop_inimigo = 0
        

    if loop_inimigo == 0 and nivel != 'Vai morrer!!!':
        inimigo=Inimigo()
        inimigo_grupo.add(inimigo)
        loop_inimigo+=1
    if loop_inimigo > 0 and nivel != 'Vai morrer!!!':
        loop_inimigo +=1
    if loop_inimigo > level and nivel != 'Vai morrer!!!' :
        loop_inimigo = 0
        
    if loop_tiro > 0 and nivel == 'Vai morrer!!!':
        loop_tiro +=3
    if loop_tiro > 25 and nivel == 'Vai morrer!!!':
        loop_tiro = 0
        
    if loop_tiro > 0 and nivel != 'Vai morrer!!!':
        loop_tiro +=1
    if loop_tiro > 30 and nivel != 'Vai morrer!!!':
        loop_tiro = 0
        
    if keys[pygame.K_LEFT]:
        nave.move_esquerda()
    if keys[pygame.K_RIGHT]:
        nave.move_direita()
    if keys[pygame.K_UP]:
        nave.move_cima()
    if keys[pygame.K_DOWN]:
        nave.move_baixo()
    if keys[pygame.K_SPACE] and loop_tiro == 0:
        nave.atira()
        loop_tiro += 1
        bullet_sound.play()
#        pontos-=1 
 
             
        
    if pygame.sprite.groupcollide(inimigo_grupo,nave.tiro_grupo ,True,True):
        pontos+=10
    
    if pygame.sprite.groupcollide(inimigo_grupo ,nave_grupo,True,True):
        pygame.mixer.music.stop()
        pygame.display.quit()
        sys.exit()
    text=fonte.render('Pontos:'+ str(pontos), 1,(255,255,0))    
    text2=fonte.render(nivel, 1,(255,255,0))    
     
    screen.fill(black )
    screen.blit(BackGround,(0,0))
    screen.blit(nave.image, nave.rect)
    screen.blit(text, (width-130,10)) 
    screen.blit(text2, (10,10)) 
    nave.tiro_grupo.update()
    nave.tiro_grupo.draw(screen) 
    inimigo_grupo.update()
    inimigo_grupo.draw(screen)
    nave_grupo.update()
    nave_grupo.draw(screen)

#    screen.blit(inimigo.image, inimigo.rect)
    pygame.display.flip(   )
