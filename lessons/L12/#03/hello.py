import pygame, sys
from pygame.locals import *
pygame.init()
GREEN = (0, 255, 0)
screen = pygame.display.set_mode((720, 760))
pygame.display.set_caption("привет мир!")
screen.fill(GREEN)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()