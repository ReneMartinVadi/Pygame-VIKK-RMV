import pygame, sys #Impordib pygame ja sysi
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

#Lisan sinised autod
blue_car1 = pygame.image.load("f1_blue.png") #Lisame sinise auto pildi
blue_car5 = pygame.image.load("f1_blue.png") #Lisame sinise auto pildi

#Kiirus ja asukoht
posM, posF = 295, 390
posX, posY = 436, 258
posL, posV = 145, 75
speedY, speedV = 7, 5

# sulgemine hiirega
while True:
    sisend = pygame.event.poll()
    if sisend.type == pygame.QUIT:
        sys.exit()

    # skoori lisamine ekraanile
    score = 0 # Muutuja score algväärtus on 0
    score2 = 0
    font = pygame.font.Font(pygame.font.match_font('comic sans'), 16)
    text = font.render("Vasak: " + str(score), True, [255, 255, 255])
    screen.blit(text, [535, 20])

    screen.blit(red_car, [posM, posF])  # Näitab meil aknas meie lisatud punast autot
    screen.blit(blue_car1, (posX,posY)) #anname esimesele pildile koordinaatideks x=436 ja y=258
    screen.blit(blue_car5, (posL, posV)) #anname viiendale pildile koordinaatideks x=145 ja y=75

    # auto positsioon suureneb kiiruse võrra
    posY += speedY
    posV += speedV

    # kui auto jõuab alla, siis läheb tagasi üles ja suurendab ühe võrra skoori
    if posY > screenY:
        posX, posY = 436, -233
    if posY < -80:
        score += 1

    if posL > screenY:
        posL, posV = 145, -75

    pygame.display.flip()  # Värskendame ekraani
