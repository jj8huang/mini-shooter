import pygame
pygame.init()

displayWidth = 450
displayHeight = 600

#colours:R  G  B
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

miniShooterDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Mini Shooter") #Title of game

mainCharImg = pygame.image.load("characterModels/mainGuy.png")

def mainChar(x, y): #display main character
    miniShooterDisplay.blit(mainCharImg, (x,y))

x = displayWidth * 0.4
y = displayHeight * 0.875
moveLeft = False
moveRight= False
clock = pygame.time.Clock()
crash = False
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
    if moveRight == True and x < displayWidth - mainCharImg.get_size()[0]:
        x = x + 3
        print event

    miniShooterDisplay.fill(WHITE)
    mainChar(x, y)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
