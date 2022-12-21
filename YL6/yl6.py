import pygame, sys  # impordib pygame ja sysi

pygame.init() #Initsialiseerib pygame

#Värv
helesinine = [0, 255, 255]

#Ekraani seaded
screenX = 640  # Annab ekraani X suuruse 640
screenY = 480  # Annab ekraani Y suuruse 480
screen = pygame.display.set_mode([screenX, screenY])  # Valmistab meile ette ekraani
pygame.display.set_caption("Ping-pong (uuendatud)")  # Annab ekraanile nimeks Ping-pong
screen.fill(helesinine)  # Paneb ekraani taustaks värvi lBlue
score = 0 #Meie muutuja nimega score
clock = pygame.time.Clock()  # Anname meie mängule mingisuguse fps-i

#Graafika laadimine
porkealus = pygame.image.load("pad.png") #Annab meie mängu põrkealusele pildi
porkealus = pygame.transform.scale(porkealus, [120,20]) #Muudab põrkealuse suurust
pall = pygame.image.load("ball.png") #Annab meie mängu pallile pildi
pall = pygame.transform.scale(pall, [20,20]) #Muudab palli suurust
posX = 200 #Määrab posX-i väärtuseks 200
posY = screenY / 1.5 #Määrab posY väärtuseks meie ekraani laiuse ScreenY ja jagab selle 1.5-ga
speedX = 0.2 #Määrab speedX väärtuseks 0.2
posL, posW = 69, 120 #Määrab posL väärtuseks 69 ja posW väärtuseks 120
speedL, speedW = 6, 9 #Määrab speedL väärtuseks 6 ja speedW väärtuseks 9
suundA, suundB = 0, 0 #Määrab suundA väärtuseks 0 ja suundB väärtuseks 0


#Muusika seaded
pygame.mixer.music.load("taustamuusika.mp3") #Laeb sisse muusika, mis hakkab taustal käima
pygame.mixer.music.play(0) #Mängib seda taustamuusikat sisse
pygame.mixer.music.set_volume(1.5) #Muudab heli tugevust

#Et aken jääks lahti ja saaks mängida
while True:
    fps = clock.tick(60) #meie kaadrisagedus, milleks on 60 (fps)

    #Sulgeb ekraani, kui me vajutame ristile
    sisestamine = pygame.event.poll() #Sisestamine võrdub pygame.event.rolliga
    for sisestamine in pygame.event.get(): #Sisestamisest on midagi pygame.event.get
        if sisestamine.type == pygame.QUIT: #Kui sisestamise tüüp on pygame.QUIT
            sys.exit() #Mäng läheb kinni

    posL += speedL #posL suureneb speedL võrra
    posW += speedW #posW suureneb speedW võrra

    porkealuse_moot = screen.blit(porkealus, (posX, posY)) #Määrab põrkealusele tema mõõtmete kasti ja alustusepositsioonid
    palli_moot = screen.blit(pall,(posL, posW)) #Määrab pallile tema mõõtmete kasti ja algusepositsioonid

#Palli kokkupuutumine mängus toimuvate asjadega
    if posL > screenX-pall.get_rect().width or posL < 0: #Kui posL on suurem kui ekraani ja palli kasti laiuse vahe või kui posL on väiksem kui null
        speedL = -speedL #speedL läheb vastupidiseks

    if posW < 0: #Kui posW on väiksem kui null
        speedW = -speedW #Siis speedW läheb vastupidiseks

    if posW > screenY-pall.get_rect().width-100: #Kui posW on suurem kui ekraani ja palli mõõdu laiuse vahe, mis sai saja võrra vähendatud

     if posW > screenY-pall.get_rect().width: #Kui posW on suurem kui ekraani ja palli mõõdu laiuse vahe
        sys.exit() #Ekraan sulgub ise

#Skooriteksti omadused
    font = pygame.font.Font(pygame.font.match_font("Times New Roman"), 20) #Määrab fondi ja selle suuruse
    skooritekst = font.render("Skooripunktid: " +str(score), True, [102, 0, 51]) #Määrab teksti ja värvi
    screen.blit(skooritekst, [420, 20]) #Määrab veel asukoha

#Palli kokkupuude põrkealusega
    if palli_moot.colliderect(porkealuse_moot) and posW > 0: #Kui palli mõõtmed puutuvad kokku põrkealuse mõõtmetega ja posW on suurem kui o
        speedW = -speedW #speedW muutub vastupidiseks
        score += 1 #Skoor suureneb ühe punkti võrra

    if palli_moot.colliderect(porkealuse_moot) and speedW > 0.5: #Kui palli mõõtmed puutuvad kokku põrkealuse mõõtmetega ja speedW on suurem kui 0.5
        speedW = -speedW #speedW muutub vastupidiseks
        skoor -= 1 #Skoor alaneb ühe punkti võrra

#Klahvi vajutamine aluse liigutamiseks
    if sisestamine.type == pygame.KEYDOWN: #Kui klahv vajutatakse alla
        if sisestamine.key == pygame.K_RIGHT: #Ja kui klahviks on parema noole klahv
            suundA = "liigu_paremale" #Siis liigub põrkealus paremale
        if sisestamine.key == pygame.K_LEFT: #Kui vajutatud klahv on hoopis vasak nool
            suundA = "liigu_vasakule" #Liigub see hoopis vasakule

#Kui klahvivajutus vabastatakse
    if sisestamine.type == pygame.KEYUP: #Kui klah lastakse lahti
        if sisestamine.key == pygame.K_RIGHT or sisestamine.key == pygame.K_LEFT: #Ja kui see on kas parem või vasak
            suundA =  0 #Siis jääb see ühte kohta seisma

    #Mängu enda piirjoonte tuvastamine
    if suundA == "liigu_vasakule": #Kui antakse liikuda vasakule
        if posX > 5: #Ja kui posX on suurem kui 5
            posX -= 15 #Siis posX ise väheneb 15 võrra
    if suundA == "liigu_paremale": #Kui antakse hoopis liikuda paremale
        if posX + 130 < screenX: #Ja kui posX + 130 on väiksem kui screenX
            posX += 15 #Siis suureneb posX 15 võrra

#Ekraani värskendamine
    pygame.display.flip() #Värskendab ekraani
    screen.fill(helesinine) #Paneb taustaks uuesti helesinise värvi
