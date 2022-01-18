import os
import pygame
import sys
from pygame import mixer

pygame.init()

pygame.display.set_caption("Main Menu")
icon = pygame.image.load('rainbow (1).png')

background = pygame.image.load('Background_Wallpaper.jpg')
mixer.music.load('Mainpage_Music.mp3')
mixer.music.play()
screen = pygame.display.set_mode((700, 600))
main_font = pygame.font.SysFont("cambria", 48)
pygame.display.set_icon(icon)

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
            if buttontext == "Start Game":
                mixer.music.stop()
                os.system('1.py')

            if buttontext == "Exit Game":
                pygame.quit()
                sys.exit()

            if buttontext == "Game & Controls":
                mixer.music.stop()
                os.system('INTRO.py')

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "pink")
        else:
            self.text = main_font.render(self.text_input, True, "white")

button_surface = pygame.image.load("Button.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))

button = Button(button_surface, 350, 100, "Start Game")
button1 = Button(button_surface, 350, 300, "Exit Game")
button2 = Button(button_surface, 350, 500, "Game & Controls")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkForInput(pygame.mouse.get_pos(),button.text_input)
            button1.checkForInput(pygame.mouse.get_pos(),button1.text_input)
            button2.checkForInput(pygame.mouse.get_pos(),button2.text_input)


    screen.blit(background, (0, 0))
    button.update()
    button1.update()
    button2.update()
    button.changeColor(pygame.mouse.get_pos())
    button1.changeColor(pygame.mouse.get_pos())
    button2.changeColor(pygame.mouse.get_pos())

    pygame.display.update()