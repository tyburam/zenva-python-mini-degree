import pygame

def load_img(path, width, height):
    scaled  = pygame.transform.scale(pygame.image.load(path),(width,height))
    return scaled.convert_alpha()

pygame.init()
screen = pygame.display.set_mode((900,700))
frame = pygame.time.Clock()

blue = (0,0,255)
black = (0,0,0)
white = (255, 255, 255)

playerX = 0
playerY = 50
playerImage = load_img("images/player.png", 30, 30)

finished = False
while not finished:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            finished = True
    
    pressedKeys = pygame.key.get_pressed()
    if 1 == pressedKeys[pygame.K_SPACE]:
        y += 5

    screen.fill(white)

    screen.blit(playerImage, (playerX,playerY))

    pygame.display.flip()
    frame.tick(30)