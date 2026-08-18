import pygame
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((500, 500))
background = pygame.image.load('background.png')
mixer.music.load('music.mp3')
mixer.music.play(-1)
we=True
while we:
    screen.blit(background,(0,0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            we=False
            break
pygame.display.update()
