import pygame, sys #impordib pygame ja sysi

# värvid
red = [255, 0, 0] #Anname värvi "red"
green = [0, 255, 0] #Annab värvi "green"
blue = [0, 0, 255] #Annab värvi "blue"
pink = [255, 153, 255] #Annab värvi "pink"
lGreen = [153, 255, 153] #Annab värvi "lGreen"
lBlue = [153, 204, 255] #Annab värvi "lBlue"

#ekraani seaded
screenX = 640 #Annab ekraani X suuruse 640
screenY = 480 #Annab ekraani Y suuruse 480
screen = pygame.display.set_mode([screenX, screenY]) #Valmistab meile ette ekraani
pygame.display.set_caption("Ping-pong") #Annab ekraanile nimeks Ping-pong
screen.fill(lBlue) #Paneb ekraani taustaks värvi lBlue
clock = pygame.time.Clock() #Anname meie mängule mingisuguse fps-i

#graafika laadimine
ball = pygame.image.load("ball.png") #Annab mängule teada, et on vaja laadida pilt nimega ball

#kiirus ja asukoht
posX, posY = 0, 0 #Palli põhiline asukoht
speedX, speedY = 3, 4 #Palli kiirus

gameover = False #Gameover on siin hetkel false
while not gameover: #Kui hetkel gameover pole
  clock.tick(60) #Meie mängu hetkene fps

  screen.blit(ball, (posX, posY)) #Lisame pildi ekraanile

  posX += speedX #Kui posX on suurem kui speedX
  posY += speedY #Kui posY on suurem kui speedY

  if posX > screenX - ball.get_rect().width or posX < 0: #Kui meie pall läheb vastu äärt, läheb ta teises suunas
    speedX = -speedX #speedX on võrdne -speedX-ga

  if posY > screenY - ball.get_rect().height or posY < 0: #Kui meie pall läheb jälle vastu äärt, läheb ta jälle teises suunas
    speedY = -speedY #speedY on võrdne -speedY-ga

  pygame.display.flip() #Värskendab ekraani
  screen.fill(lBlue) #Paneb uuesti taustaks helesinise

x = 200 #Hetekese objekti X-koordinaat
y = 420 #Hetekese objekti Y-koordinaat

alus = pygame.image.load("pad.png").convert() #Laeme sisse aluse

rect = alus.get_rect() #Lisame meie alusele võimaluse tunnetada, kui pall läheb selle vastu
rect.center = (x,y) #See on meie aluse keskne koht

width = 120 #Aluse pikkus
height = 20 #Aluse kõrgus

vel = 10 #Aluse kiirus

run = True #Näitab, et mäng jookseb

while run: #Kui programm samal ajal jookseb
    pygame.time.delay(10) # Teeb ajale 10ms delay

    # that was returned by pygame.event.get() method.
    for event in pygame.event.get(): #Kui evendis on vaja saada pygame.event

        if event.type == pygame.QUIT: #Kui selle mängus toimuva asja tüüp on Quit
            run = False #Paneb mängu kinni
    keys = pygame.key.get_pressed() #Kui vajutatakse spetsiifilist klahvi

    if keys[pygame.K_LEFT] and x > 0: #Kui vajutatakse vasakut klahvi
        x -= vel #X-koordinaat väheneb

    
    if keys[pygame.K_RIGHT] and x < 640 - width: #Kui vajutatakse paremat klahvi 
        x += vel #Juurdekasv x-koordinaadis
        
    screen.fill((0, 0, 0)) #Teeb meie ekraani värvi täisti mustaks

    screen.blit(alus, rect) #Teeb meile siia objekti nimega alus ja ristküliku

    pygame.display.update() # Värskendab ekraani


running = True # Muutuja "running" omistab endale True väärtuse
while running: # Kuni "running" on True,
  for event in pygame.event.get(): # Iga tsüklimuutuja väärtus "pygame.event.get()".
    if event.type == pygame.QUIT: # Kui muutuja "event.type" on võrdeline pygame.QUIT meetodi väärtusega (akna sulgemine)
      running = False # Muutuja "running" omistab väärtuse False.
    if running == False: # Kui muutuja "running" väärtus on võrdeline False'ga,
      pygame.quit() # pygame moodul suletakse.
