import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((720, 760))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()