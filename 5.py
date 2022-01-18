import pygame
import math
import random
import os
import sys
from pygame import mixer
pygame.init()

screen = pygame.display.set_mode((700, 600))

#  Background
background = pygame.image.load('background1234.png')

#  Background Music
mixer.music.load('background.mp3')
mixer.music.set_volume(0.05)
mixer.music.play()


# Title and Icon
pygame.display.set_caption("Covid-19 Fighter")
icon = pygame.image.load('rainbow (1).png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('needle1.png')
playerX = 280
playerY = 410
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Soap
SoapImg = pygame.image.load('soap.png')
Soap_X = 480
Soap_Y = 200
Soap_X_change = 0


def Soap(x, y):
    screen.blit(SoapImg, (x, y))


# Enemy 1
Enemy_1Img = pygame.image.load('coronavirus.png')
Enemy_1X = random.randint(0, 700)
Enemy_1Y = 100
Enemy_1X_change = 0


def Enemy_1(x, y):
    screen.blit(Enemy_1Img, (x, y))


# Enemy 2
Enemy_2Img = pygame.image.load('virus.png')
Enemy_2X = random.randint(0, 700)
Enemy_2Y = 100
Enemy_2X_change = 0.8


def Enemy_2(x, y):
    screen.blit(Enemy_2Img, (x, y))


# Enemy 3
Enemy_3Img = pygame.image.load('virus 2.png')
Enemy_3X = random.randint(0, 700)
Enemy_3Y = 330
Enemy_3X_change = 0.8


def Enemy_3(x, y):
    screen.blit(Enemy_3Img, (x, y))


# Bullet
BulletImg = pygame.image.load('red-cross.png')
BulletX = 0
BulletY = 480
BulletX_change = 0
BulletY_change = 4
Bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 15


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


Levels_value = 5
font = pygame.font.Font('freesansbold.ttf', 32)

text_1X = 500
text_1Y = 15


def show_LEVELS(x, y):
    Level = font.render("Level : " + str(Levels_value), True, (0, 0, 0))
    screen.blit(Level, (x, y))


def fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImg, (x + 100, y + 5))


def bouce_back(x, y):
    global Bullet_state
    Bullet_state = "backfire"
    screen.blit(BulletImg, (x + 100 , y +5))
def Collision1(Enemy_1X, Enemy_1Y, BulletX, BulletY):
    distance = math.sqrt((math.pow(Enemy_1X - 70 - BulletX, 2)) + (math.pow(Enemy_1Y - BulletY, 2)))

    if distance < 27:
        #print("Enemy_1X", Enemy_1X, Enemy_1Y, BulletX, BulletY, distance)
        return True

    else:
        return False


def Collision2(Enemy_2X, Enemy_2Y, BulletX, BulletY):
    distance = math.sqrt((math.pow(Enemy_2X - 70 - BulletX, 2)) + (math.pow(Enemy_2Y - BulletY, 2)))

    if distance < 27:
        return True
    else:
        return False


def Collision3(Enemy_3X, Enemy_3Y, BulletX, BulletY):
    distance = math.sqrt((math.pow(Enemy_3X - 70 - BulletX, 2)) + (math.pow(Enemy_3Y - BulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def Collision4(Soap_X, Soap_Y, BulletX, BulletY):
    distance = math.sqrt((math.pow(Soap_X - 40 - BulletX, 2)) + (math.pow(Soap_Y - BulletY, 2)))
    #print("Soap_X", Soap_X, Soap_Y, BulletX, BulletY, distance)
    if distance < 58.2:
        # print("Enemy_1X", Enemy_1X, Enemy_1Y, BulletX,BulletY, distance)
        return True

    else:
        return False


def Collision5(playerX, playerY, BulletX, BulletY):
    distance = math.sqrt((math.pow(playerX - 70 - BulletX, 2)) + (math.pow(playerY - BulletY, 2)))

    if distance < 27:
        return True

    else:
        return False


main_font = pygame.font.SysFont("cambria", 60)


class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(350, 220))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position, buttontext):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            #print("Next Level text", buttontext)
            if buttontext == "Next Level":
                mixer.music.stop()
                os.system('Mainpage.py')

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "pink")
        else:
            self.text = main_font.render(self.text_input, True, "white")


def target_missed():
    screen.blit(Enemy_3Img, (280, 40))


def levels():
    if score_value == 5:
        Level_Sound = mixer.Sound('LEVEL_MUSIC.mp3')
        Level_Sound.play()
        screen = pygame.display.set_mode((700, 600))
        pygame.display.set_caption("Next level Menu")
        button_surface = pygame.image.load("mask.png")
        button_surface = pygame.transform.scale(button_surface, (512, 512))
        button = Button(button_surface, 350, 200, "Next Level")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Mouse Event")
                    button.checkForInput(pygame.mouse.get_pos(), button.text_input)

                background = pygame.image.load('Background_wallpaper.jpg')
                screen.blit(background, (0, 0))
                button.update()
                button.changeColor(pygame.mouse.get_pos())

                pygame.display.update()


# Game Loop
running = True
sleeptime = 1
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 255, 255))

    # Background Image

    screen.blit(background, (0, 0))
    if sleeptime == 400:
        Enemy_1X = random.randint(0, 700)
        Enemy_1Y = random.randint(70, 150)

        sleeptime = 1
    sleeptime = sleeptime + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEYSTROKE FUNCTIONS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            if event.key == pygame.K_SPACE:
                if Bullet_state == "ready":
                    BulletX = playerX
                    fire_bullet(BulletX, BulletY)
                    SPACE_Sound = mixer.Sound('Space.mp3')
                    SPACE_Sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= -83:
        playerX = -83
    elif playerX >= 560:
        playerX = 560

    Enemy_2X += Enemy_2X_change

    if Enemy_2X <= 3:
        Enemy_2X_change = 0.8
    elif Enemy_2X >= 640:
        Enemy_2X_change = -0.8

    Enemy_3X += Enemy_3X_change

    if Enemy_3X <= 3:
        Enemy_3X_change = 0.8
    elif Enemy_3X >= 640:
        Enemy_3X_change = -0.8

    # Bullet Movement
    if BulletY <= 70:
        BulletY = 480
        Bullet_state = "ready"

    if Bullet_state == "fire":
        fire_bullet(BulletX, BulletY)
        BulletY -= BulletY_change

    if Bullet_state == "backfire":
        BulletY += BulletY_change
        bouce_back(BulletX, BulletY)
        if BulletY >= 480:
            Bullet_state = "ready"


    # Collision
    collision1 = Collision1(Enemy_1X, Enemy_1Y, BulletX, BulletY)

    if collision1:
        BulletY = 480
        Col_Sound = mixer.Sound('Col_Music.mp3')
        Col_Sound.play()
        Bullet_state = "ready"
        score_value += 1
        Enemy_1X = random.randint(0, 700)
        Enemy_1Y = random.randint(100, 150)
        # target_missed()

    collision2 = Collision2(Enemy_2X, Enemy_2Y, BulletX, BulletY)
    if collision2:
        BulletY = 480
        Col_Sound = mixer.Sound('Col_Music.mp3')
        Col_Sound.play()
        Bullet_state = "ready"
        score_value += 1

    collision3 = Collision3(Enemy_3X, Enemy_3Y, BulletX, BulletY)
    if collision3:
        BulletY = 480
        Col_Sound = mixer.Sound('Col_Music.mp3')
        Col_Sound.play()
        Bullet_state = "ready"
        score_value += 1

    collision4 = Collision4(Soap_X, Soap_Y, BulletX, BulletY)
    if collision4:
        BulletY_change = 4
        Col_Sound = mixer.Sound('Soap.mp3')
        Col_Sound.play()
        Bullet_state = "backfire"
        BulletY = BulletY + BulletY_change
        bouce_back(BulletX , BulletY)
        # if BulletY <= 480:
        #     BulletY_change = -4
        # elif BulletY >= 200:
        #     BulletY_change = -4
        # collision5 = Collision5(playerX, playerY, BulletX, BulletY)
        # if Collision5:
        #    Bullet_state = "ready"

    player(playerX, playerY)
    show_score(textX, textY)
    levels()
    show_LEVELS(text_1X, text_1Y)
    Enemy_1(Enemy_1X, Enemy_1Y)
    Enemy_2(Enemy_2X, Enemy_2Y)
    Enemy_3(Enemy_3X, Enemy_3Y)
    Soap(Soap_X, Soap_Y)
    pygame.display.update()
