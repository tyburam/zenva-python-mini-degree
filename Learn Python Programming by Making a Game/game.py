import pygame

pygame.init()

screen = pygame.display.set_mode((900,700))
finished = False
x = 0
y = 50
frame = pygame.time.Clock()

playerImage = pygame.image.load("images/player.png")
playerImage = pygame.transform.scale(playerImage, (30, 30))
playerImage= playerImage.convert()

while not finished:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            finished = True
    
    pressedKeys = pygame.key.get_pressed()
    if 1 == pressedKeys[pygame.K_SPACE]:
        y += 5

    color = (0,0,255)
    black = (0,0,0)
    white = (255, 255, 255)

    screen.fill(black)

    rectOne = pygame.Rect(x,y,30,30)
    screen.blit(playerImage, (x,y))
    #pygame.draw.rect(screen, color, rectOne)

    pygame.display.flip()
    frame.tick(30)