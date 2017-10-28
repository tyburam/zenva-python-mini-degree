import pygame

def load_img(path, width, height):
    return pygame.transform.scale(pygame.image.load(path),(width,height))

def check_collision(first, second):
    if (first[1] >= second[1] and first[1]  <= (second[1] + second[3])) or (first[1] + first[3] >= second[1] and first[1] + first[3] <= second[1] + second[3]):
        if (first[0] >= second[0] and first[0] <= (second[0] + second[2])) or ((first[0] + first[2]) >= second[0] and (first[0] + first[2]) <= second[0] + second[2]):
            return True
    return False

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

font = pygame.font.SysFont("comicsans", 60)
textWin = font.render("Great Job!", True, black)

finished = False
while not finished:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            finished = True
    
    pressedKeys = pygame.key.get_pressed()
    if 0 != pressedKeys[pygame.K_SPACE]:
        playerY -= 5         

    screen.blit(backgroundImage, (0,0))
    screen.blit(treasureImage, (treasureX, treasureY))
    screen.blit(playerImage, (playerX,playerY))

    if check_collision((playerX, playerY, 35, 40), (treasureX, treasureY, 35, 40)):
        screen.blit(textWin, (300,300))

    pygame.display.flip()
    frame.tick(30)