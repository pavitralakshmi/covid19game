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

#Title and Icon
pygame.display.set_caption("Covid-19 Fighter ")
icon = pygame.image.load('rainbow (1).png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('open-hands.png')
playerX = 300
playerY = 500
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Sanatizer
Sanatizer_1Img = pygame.image.load('sanatizer6.png')
Sanatizer_1X = 350
Sanatizer_1Y = 75
Sanatizer_1X_change = 0


def Sanatizer_1(x, y):
    screen.blit(Sanatizer_1Img, (x, y))


# Bullet
BulletImg = pygame.image.load('drop.png')
BulletX = 350
BulletY = 75
BulletX_change = 0
BulletY_change = 3
Bullet_state = "fire"


# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 45
textY = 25


def show_score(x, y):
    score = font.render("Hands Sanitized :" + str(score_value) + "/5", True, (0, 0, 0))
    screen.blit(score, (x, y))

# Score

Levels_value = 1
font = pygame.font.Font('freesansbold.ttf', 32)

text_1X = 500
text_1Y = 25


def show_LEVELS(x, y):
    Level = font.render("Level : " + str(Levels_value) , True, (0, 0, 0))
    screen.blit(Level, (x, y))


def fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImg, (x + 0, y + 0))


def Collision1(playerX, playerY, BulletX, BulletY):
    distance = math.sqrt((math.pow((playerX+40) - BulletX, 2)) + (math.pow(playerY - BulletY, 2)))
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
                os.system('2.py')

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "pink")
        else:
            self.text = main_font.render(self.text_input, True, "white")

        # def target_missed():
        # screen.blit(Enemy_3Img, (280, 40))


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
    screen.fill((250, 255, 255))

    # Background Image

    screen.blit(background, (0, 0))
    if sleeptime == 300:
        Sanatizer_1X = random.randint(0, 600)
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #if Bullet_state == "fire":
        #BulletX = Sanatizer_1X
        #fire_bullet(BulletX, BulletY)

    playerX += playerX_change

    if playerX <= 3:
        playerX = 3
    elif playerX >= 575:
        playerX = 575


    # Bullet Movement
    if BulletY >= 700:
        BulletY = 75
        Bullet_state = "fire"

    if Bullet_state == "fire":
        BulletX = Sanatizer_1X+30
        fire_bullet(BulletX, BulletY)
        BulletY += BulletY_change

    player(playerX, playerY)
# Collision
    collision1 = Collision1(playerX, playerY, BulletX, BulletY)

    if collision1:
        Splash_Sound = mixer.Sound('Water_Splash.mp3')
        Splash_Sound.play()
        BulletY = 75
        Bullet_state = "fire"
        score_value += 1
        # playerX = random.randint(0, 700)
        # playerY = 500



    show_score(textX, textY)
    levels()
    Sanatizer_1(Sanatizer_1X, Sanatizer_1Y)
    show_LEVELS(text_1X, text_1Y)
    pygame.display.update()