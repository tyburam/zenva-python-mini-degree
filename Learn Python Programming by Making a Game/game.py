import pygame

pygame.init()

screen = pygame.display.set_mode((900,700))
finished = False
x = 0
y = 50

while not finished:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            finished = True
    
    pressedKeys = pygame.key.get_pressed()
    rectOne = pygame.Rect(x,y,30,30)
    color = (0,0,255)
    pygame.draw.rect(screen, color, rectOne)
    pygame.display.flip()