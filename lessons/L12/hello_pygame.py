import pygame, sys
from pygame.locals import *
pygame.init()
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((650, 570))
pygame.display.set_caption("привет Pygame!")
screen.fill(BLUE)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()