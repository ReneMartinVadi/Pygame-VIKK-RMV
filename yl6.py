import pygame, sys

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

#ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock()

#graafika laadimine
ball = pygame.image.load("ball.png")

#kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 4

gameover = False
while not gameover:
  #fps
  clock.tick(60)

  #pildi lisamine ekraanile
  screen.blit(ball, (posX, posY))

  posX += speedX
  posY += speedY

  #kui puudub ääri, siis muudab suunda
  if posX > screenX - ball.get_rect().width or posX < 0:
    speedX = -speedX

  if posY > screenY - ball.get_rect().height or posY < 0:
    speedY = -speedY

  #graafika kuvamine ekraanil
  pygame.display.flip()
  screen.fill(lBlue)

# object current co-ordinates
x = 200
y = 420

# graafika laadimine
alus = pygame.image.load("pad.png").convert()

rect = alus.get_rect()
rect.center = (x,y)

# dimensions of the object
width = 120
height = 20

# velocity / speed of movement
vel = 10

# Indicates pygame is running
run = True

# infinite loop
while run:
    # creates time delay of 10ms
    pygame.time.delay(10)

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # it will make exit the while loop
            run = False
    # stores keys pressed
    keys = pygame.key.get_pressed()

    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x > 0:
        # decrement in x co-ordinate
        x -= vel

    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x < 640 - width:
        # increment in x co-ordinate
        x += vel

    # completely fill the surface object
    # with black colour
    screen.fill((0, 0, 0))

    # drawing object on screen which is rectangle here
    screen.blit(alus, rect)

    # it refreshes the window
    pygame.display.update()


running = True # Muutuja "running" omistab endale True väärtuse
while running: # Kuni "running" on True,
  for event in pygame.event.get(): # Iga tsüklimuutuja väärtus "pygame.event.get()".
    if event.type == pygame.QUIT: # Kui muutuja "event.type" on võrdeline pygame.QUIT meetodi väärtusega (akna sulgemine)
      running = False # Muutuja "running" omistab väärtuse False.
    if running == False: # Kui muutuja "running" väärtus on võrdeline False'ga,
      pygame.quit() # pygame moodul suletakse.