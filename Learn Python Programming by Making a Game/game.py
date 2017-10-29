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
enemyX = playerX
enemyY = 450
treasureX = playerX
treasureY = 50
level = 1

playerImage = load_img("images/player.png", 35, 40).convert_alpha()
backgroundImage = load_img("images/background.png", 900, 700)
treasureImage = load_img("images/treasure.png", 35, 40)
enemyImage = load_img("images/enemy.png", 35, 40).convert_alpha()
font = pygame.font.SysFont("comicsans", 70)

finished = False
enemyMovingRight = True

while not finished:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            finished = True
    
    if enemyX >= 820:
        enemyMovingRight = False
    elif enemyX <= 30:
        enemyMovingRight = True
        
    if enemyMovingRight:
        enemyX += 5
    else:
        enemyX -= 5

    pressedKeys = pygame.key.get_pressed()
    if 0 != pressedKeys[pygame.K_SPACE]:
        playerY -= 5         

    screen.blit(backgroundImage, (0,0))
    screen.blit(treasureImage, (treasureX, treasureY))
    screen.blit(playerImage, (playerX,playerY))
    screen.blit(enemyImage, (enemyX, enemyY))

    if check_collision((playerX, playerY, 35, 40), (treasureX, treasureY, 35, 40)):
        level += 1
        textWin = font.render("You've reached level " + str(level), True, black)
        screen.blit(textWin, (450 - (textWin.get_width() / 2),300 - (textWin.get_height() / 2)))
        playerY = 650

    pygame.display.flip()
    frame.tick(30)