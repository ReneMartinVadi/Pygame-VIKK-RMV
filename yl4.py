import pygame, random #Impordib pygame ja randomi
from pygame.surface import Surface, SurfaceType

pygame.init() #Käivitab "Pygame" mooduli

#Lisan värvid
white = [255, 255, 255] #Anname oma tekstile värvi, et seda kasutada hiljem skoori värvina

screenX = 640 #Ekraani X on 640
screenY = 480 #Ekraani Y  on 480
screen=pygame.display.set_mode([screenX,screenY]) # Tekitab akna, mille suuruseks on 640x480 ja salvestab selle muutujasse "screen".
pygame.display.set_caption("Ülesanne 4: Objektide animeerimine") # Akna pealkirjaks on "Ülesanne 4: Objektide animeerimine".

#Lisan tausta
bg = pygame.image.load("bg_rally.jpg") #Lisame tausta, milleks on nimi bg_shop.jpg
screen.blit(bg,[0,0]) #Näitab meil aknas meie lisatud tausta

#Lisan punase auto
red_car = pygame.image.load("f1_red.png") #Lisame punase auto pildi
screen.blit(red_car, [295,390]) #Näitab meil aknas meie lisatud punast autot

#Lisan sinised autod
blue_car1 = pygame.image.load("f1_blue.png") #Lisame sinise auto pildi
blue_car2 = pygame.image.load("f1_blue.png") #Lisame sinise auto pildi
blue_car3 = pygame.image.load("f1_blue.png") #Lisame sinise auto pildi
blue_car4 = pygame.image.load("f1_blue.png") #Lisame sinise auto pildi
blue_car5 = pygame.image.load("f1_blue.png") #Lisame sinise auto pildi
screen.blit(blue_car1, (436,258)) #anname esimesele pildile koordinaatideks x=436 ja y=258
screen.blit(blue_car2, (400, 263)) #anname teisele pildile koordinaatideks x=400 ja y=263
screen.blit(blue_car3, (318, 204)) #anname kolmandale pildile koordinaatideks x=318 ja y=204
screen.blit(blue_car4, (273, 102)) #anname neljandale pildile koordinaatideks x=273 ja y=102
screen.blit(blue_car5, (145, 75)) #anname viiendale pildile koordinaatideks x=145 ja y=75

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