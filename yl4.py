import pygame, random
from pygame.surface import Surface, SurfaceType

pygame.init()

screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY]) # Tekitab akna, mille suuruseks on 640x480 ja salvestab selle muutujasse "screen".
pygame.display.set_caption("Ülesanne 4: Objektide animeerimine") # Akna pealkirjaks on "Ülesanne 4: Objektide animeerimine".

#Lisan tausta
bg = pygame.image.load("bg_rally.jpg") #Lisame tausta, milleks on nimi bg_shop.jpg
screen.blit(bg,[0,0]) #Näitab meil aknas meie lisatud tausta

#Lisan punase auto
red_car = pygame.image.load("f1_red.png")
screen.blit(red_car, [295,390])

#Lisan sinised autod
blue_car1 = pygame.image.load("f1_blue.png")
blue_car2 = pygame.image.load("f1_blue.png")
blue_car5 = pygame.image.load("f1_blue.png")
blue_car6 = pygame.image.load("f1_blue.png")
blue_car8 = pygame.image.load("f1_blue.png")
screen.blit(blue_car1, (436,258))
screen.blit(blue_car2, (400, 263))
screen.blit(blue_car5, (318, 204))
screen.blit(blue_car6, (273, 102))
screen.blit(blue_car8, (145, 75))


#kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 3

score = 0 # Muutuja score algväärtus on 0
font = pygame.font.Font(None, 74) #Anname oma skoorile mingi  teksti fondi, mille suurus on 74px
text = font.render(str(score), 1, white) #Lisame skoori tekstina
screen.blit(text, (10,10)) #Näitab meie skoori mängus sees

pygame.display.flip() #Värskendame ekraani

running = True # Muutuja "running" omistab endale True väärtuse
while running: # Kuni "running" on True,
  for event in pygame.event.get(): # Iga tsüklimuutuja väärtus "pygame.event.get()".
    if event.type == pygame.QUIT: # Kui muutuja "event.type" on võrdeline pygame.QUIT meetodi väärtusega (akna sulgemine)
      running = False # Muutuja "running" omistab väärtuse False.
    if running == False: # Kui muutuja "running" väärtus on võrdeline False'ga,
      pygame.quit() # pygame moodul suletakse.