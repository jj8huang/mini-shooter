import pygame
import random
pygame.init()

displayWidth = 450
displayHeight = 600

#colours:R  G  B
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255,127,80)

miniShooterDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Mini Shooter") #Title of game

mainCharImg = pygame.image.load("characterModels/mainGuy.png")
enemyImg = pygame.image.load("characterModels/mainGuy.png")

def mainChar(x, y): #display main character
    miniShooterDisplay.blit(mainCharImg, (x,y))

def enemy(x, y): #display enemy
    miniShooterDisplay.blit(mainCharImg, (x, y))

def enemiesDodged():


x = displayWidth * 0.4
y = displayHeight * 0.875
mainCharWidth = mainCharImg.get_size()[0]
mainCHarHeight = mainCharImg.get_size()[1]
moveLeft = False
moveRight= False
clock = pygame.time.Clock()
crash = False
enemyHeight = enemyImg.get_size()[1]
enemyWidth = enemyImg.get_size()[0]
enemyStartX = random.randrange(0, displayWidth - enemyWidth)
enemyStartY = 0 - enemyHeight
enemySpeed = 7

while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveRight = True
            elif event.key == pygame.K_LEFT:
                moveLeft = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moveRight = False
            if event.key == pygame.K_LEFT:
                moveLeft = False
    if moveLeft == True and x > 0:
        x = x - 3
    if moveRight == True and x < displayWidth - mainCharWidth:
        x = x + 3
        print event

    miniShooterDisplay.fill(ORANGE)
    enemy(enemyStartX, enemyStartY)
    enemyStartY = enemyStartY + enemySpeed
    mainChar(x, y)
    if enemyStartY > displayHeight:
        enemyStartY = 0 - enemyHeight
        enemyStartX = random.randrange(0, displayWidth - enemyImg.get_size()[0])
    if y < enemyStartY + enemyHeight:
        if x > enemyStartX and x < enemyStartX + enemyWidth or x + mainCharWidth > enemyStartX and x + mainCharWidth < enemyStartX + enemyWidth:
            print('YOU DEAD BOI')
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
