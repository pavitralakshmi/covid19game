import pygame
import os
import pygame
import sys
from pygame import mixer
from pygame import mixer
pygame.init()

screen = pygame.display.set_mode((700, 600))

#  Background
background = pygame.image.load('Background_Wallpaper.jpg')
screen.blit(background, (0, 0))


#  Background Music
mixer.music.load('Mainpage_Music.mp3')
mixer.music.set_volume(0.05)
mixer.music.play()
font = pygame.font.Font('freesansbold.ttf', 60)
font1 = pygame.font.SysFont('Comic Sans Ms', 40)
main_font = pygame.font.SysFont('Comic Sans Ms', 40)
#Title and Icon
pygame.display.set_caption("Covid-19 Fighter ")
icon = pygame.image.load('rainbow (1).png')
pygame.display.set_icon(icon)

def TEXT(x, y ,inputtext):
    textout = font.render(inputtext, True, (255, 255, 255))
    screen.blit(textout, (x, y))

def smallText(x, y ,inputtext):
    textout = font1.render(inputtext, True, (127.5, 127.5, 127.5))
    screen.blit(textout, (x, y))

class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position,buttontext):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            if buttontext == " ":
                mixer.music.stop()
                os.system('Mainpage.py')

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "pink")
        else:
            self.text = main_font.render(self.text_input, True, "white")





running = True
sleeptime = 1
while running:
    TEXTa = "GAME"
    TEXTb = "The purpose of this game is for kids"
    TEXTc = "      to develop self-awareness of"
    TEXTd = "COVID-19and how to act in a secure"
    TEXTe = "manner. While playing this game,"
    TEXTf = "you will learn some good practices "
    TEXTg = "          to adapt and follow."


    TEXTh = "If you want to move to the right"
    TEXTi = "of the screen, press the right arrow"
    TEXTj = "key, and if you want to move to the "
    TEXTk = "left, press the left arrow key."
    TEXTl = "CONTROLS"
    TEXTX1 = 260
    TEXTX = 10
    TEXTY = 1

    TEXT(TEXTX1, TEXTY,TEXTa)
    TEXT(TEXTX1-90, TEXTY+320,TEXTl)
    smallText(TEXTX, TEXTY+50,TEXTb)
    smallText(TEXTX, TEXTY+90,TEXTc)
    smallText(TEXTX, TEXTY+130,TEXTd)
    smallText(TEXTX, TEXTY+170,TEXTe)
    smallText(TEXTX, TEXTY+210,TEXTf)
    smallText(TEXTX, TEXTY+250,TEXTg)
    smallText(TEXTX, TEXTY+360,TEXTh)
    smallText(TEXTX, TEXTY+400,TEXTi)
    smallText(TEXTX, TEXTY+440,TEXTj)
    smallText(TEXTX, TEXTY+480,TEXTk)
    button_surface = pygame.image.load("CLOSE (2).png")
    button_surface = pygame.transform.scale(button_surface, (80, 80))
    button = Button(button_surface,640, 540, " ")
    button.update()
    button.changeColor(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkForInput(pygame.mouse.get_pos(), button.text_input)
    pygame.display.update()
