import math
import random
import os
import pygame
import sys

# from ButtonModule import Button

pygame.init()

# Create The Screen
screen = pygame.display.set_mode((700, 600))

#  Background
background = pygame.image.load('Background.jpg')

# Title and Icon
pygame.display.set_caption("Covid-19 Fighter")
icon = pygame.image.load('rainbow (1).png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Player.png')
playerX = 280
playerY = 420
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy 1
Enemy_1Img = pygame.image.load('coronavirus.png')
Enemy_1X = random.randint(0, 700)
Enemy_1Y = 50
Enemy_1X_change = 0


def Enemy_1(x, y):
    screen.blit(Enemy_1Img, (x, y))


# Enemy 2
Enemy_2Img = pygame.image.load('virus.png')
Enemy_2X = random.randint(0, 700)
Enemy_2Y = 40
Enemy_2X_change = 0


def Enemy_2(x, y):
    screen.blit(Enemy_2Img, (x, y))


# Enemy 3
Enemy_3Img = pygame.image.load('virus 2.png')
Enemy_3X = random.randint(0, 700)
Enemy_3Y = 40
Enemy_3X_change = 0


def Enemy_3(x, y):
    screen.blit(Enemy_3Img, (x, y))


# Bullet
BulletImg = pygame.image.load('red-cross.png')
BulletX = 0
BulletY = 480
BulletX_change = 0
BulletY_change = 3
Bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


def fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImg, (x + 50, y + 5))


def Collision1(Enemy_1X, Enemy_1Y, BulletX, BulletY):
    distance = math.sqrt((math.pow(Enemy_1X - BulletX, 2)) + (math.pow(Enemy_1Y - BulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def Collision2(Enemy_2X, Enemy_2Y, BulletX, BulletY):
    distance = math.sqrt((math.pow(Enemy_2X - BulletX, 2)) + (math.pow(Enemy_2Y - BulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def Collision3(Enemy_3X, Enemy_3Y, BulletX, BulletY):
    distance = math.sqrt((math.pow(Enemy_2X - BulletX, 2)) + (math.pow(Enemy_2Y - BulletY, 2)))
    if distance < 27:
        return True
    else:
        return False



def levels():
    if score_value == 2:
        screen = pygame.display.set_mode((700, 600))
        pygame.display.set_caption("Next level Menu")
        main_font = pygame.font.SysFont("freesansbold.ttf", 60)

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

            def checkForInput(self, position):
                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top):
                    if buttontext == "Next Level":
                        os.system('PRACTICE.py')

            def changeColor(self, position):
                if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                                  self.rect.bottom):
                    self.text = main_font.render(self.text_input, True, "orange")
                    self.text = main_font.render(self.text_input, True, "black")
        button_surface = pygame.image.load("mask.png")
        button_surface = pygame.transform.scale(button_surface, (512, 512))

        button = Button(button_surface, 350, 200, "Next Level")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button.checkForInput(pygame.mouse.get_pos())

            screen.fill("white")

            button.update()
            button.changeColor(pygame.mouse.get_pos())

            pygame.display.update()

def target_missed():
    screen.blit(Enemy_3Img, (280, 40))


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
        Enemy_1Y = random.randint(30, 150)
        Enemy_2X = random.randint(0, 700)
        Enemy_2Y = random.randint(30, 150)
        Enemy_3X = random.randint(0, 700)
        Enemy_3Y = random.randint(30, 150)
        sleeptime = 1
    sleeptime = sleeptime + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEYSTROKE FUNCTIONS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if Bullet_state == "ready":
                    BulletX = playerX
                    fire_bullet(BulletX, BulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= -45:
        playerX = -45
    elif playerX >= 620:
        playerX = 620

    # Bullet Movement
    if BulletY <= 0:
        BulletY = 480
        Bullet_state = "ready"

    if Bullet_state == "fire":
        fire_bullet(BulletX, BulletY)
        BulletY -= BulletY_change

    # Collision
    collision1 = Collision1(Enemy_1X, Enemy_1Y, BulletX, BulletY)

    if collision1:
        BulletY = 480
        Bullet_state = "ready"
        score_value += 1
        Enemy_1X = random.randint(0, 700)
        Enemy_1Y = random.randint(30, 150)
        target_missed()

    collision2 = Collision2(Enemy_2X, Enemy_2Y, BulletX, BulletY)
    if collision2:
        BulletY = 480
        Bullet_state = "ready"
        score_value += 1
        Enemy_2X = random.randint(0, 700)
        Enemy_2Y = random.randint(50, 150)
    collision3 = Collision3(Enemy_3X, Enemy_3Y, BulletX, BulletY)
    if collision3:
        BulletY = 480
        Bullet_state = "ready"
        score_value += 1
        Enemy_2X = random.randint(0, 700)
        Enemy_2Y = random.randint(50, 150)

    player(playerX, playerY)
    show_score(textX, textY)
    levels()
    Enemy_1(Enemy_1X, Enemy_1Y)
    Enemy_2(Enemy_2X, Enemy_2Y)
    Enemy_3(Enemy_3X, Enemy_3Y)
    pygame.display.update()
