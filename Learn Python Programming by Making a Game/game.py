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
red = (255, 0, 0)
black = (0,0,0)
white = (255, 255, 255)

playerX = 450 - (35/2)
playerY = 650
enemyX = playerX
enemyY = 570
enemyMovingRight = True
treasureX = playerX
treasureY = 50
level = 1

enemies = [(enemyX, enemyY, enemyMovingRight)]
enemyNames = {0:"Max", 1:"Jill", 2:"Greg", 3:"Diane"}

playerImage = load_img("images/player.png", 35, 40).convert_alpha()
backgroundImage = load_img("images/background.png", 900, 700)
treasureImage = load_img("images/treasure.png", 35, 40)
enemyImage = load_img("images/enemy.png", 35, 40).convert_alpha()
font = pygame.font.SysFont("comicsans", 70)

finished = False
while not finished:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            finished = True

    enemyIndex = 0
    for enemyX, enemyY, enemyMovingRight in enemies:
        if enemyX >= 800:
            enemyMovingRight = False
        elif enemyX <= 40:
            enemyMovingRight = True

        if enemyMovingRight:
            enemyX += 5 * level
        else:
            enemyX -= 5 * level
        enemies[enemyIndex] = (enemyX, enemyY, enemyMovingRight)
        enemyIndex += 1

    pressedKeys = pygame.key.get_pressed()
    if 0 != pressedKeys[pygame.K_SPACE]:
        playerY -= 5         

    screen.blit(backgroundImage, (0,0))
    screen.blit(treasureImage, (treasureX, treasureY))
    screen.blit(playerImage, (playerX,playerY))

    playerPos = (playerX, playerY, 35, 40)
    treasurePos = (treasureX, treasureY, 35, 40)

    enemyIndex = 0
    for enemyX, enemyY, enemyMovingRight in enemies:
        screen.blit(enemyImage, (enemyX, enemyY))
        enemyPos = (enemyX, enemyY, 35, 40)
        if check_collision(playerPos, enemyPos):
            playerY = 650
            name = enemyNames[enemyIndex]
            textLost = font.render("You were killed by" + name, True, red)
            screen.blit(textLost, (450 - (textLost.get_width() / 2),300 - (textLost.get_height() / 2)))
        enemyIndex += 1

    if check_collision(playerPos, treasurePos):
        level += 1
        enemies.append((enemyX - 50 * level, enemyY - 50*level, False))
        textWin = font.render("You've reached level " + str(level), True, black)
        screen.blit(textWin, (450 - (textWin.get_width() / 2),300 - (textWin.get_height() / 2)))
        playerY = 650

    pygame.display.flip()
    frame.tick(30)