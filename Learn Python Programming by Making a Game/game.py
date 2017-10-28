import pygame

def load_img(path, width, height):
    return pygame.transform.scale(pygame.image.load(path),(width,height))

pygame.init()
screen = pygame.display.set_mode((900,700))
frame = pygame.time.Clock()

blue = (0,0,255)
black = (0,0,0)
white = (255, 255, 255)

playerX = 450 - (35/2)
playerY = 650
treasureX = playerX
treasureY = 50

playerImage = load_img("images/player.png", 35, 40).convert_alpha()
backgroundImage = load_img("images/background.png", 900, 700)
treasureImage = load_img("images/treasure.png", 35, 40)

finished = False
while not finished:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            finished = True
    
    pressedKeys = pygame.key.get_pressed()
    if 1 == pressedKeys[pygame.K_SPACE]:
        y -= 5

    screen.blit(backgroundImage, (0,0))
    screen.blit(treasureImage, (treasureX, treasureY))
    screen.blit(playerImage, (playerX,playerY))

    pygame.display.flip()
    frame.tick(30)