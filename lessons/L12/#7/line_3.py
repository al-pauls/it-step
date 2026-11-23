import pygame, sys, color
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("3 линии")
screen.fill(color.GREEN)
pygame.draw.line(screen, color.BLUE, (200, 100), (200, 300), 5)
pygame.draw.line(screen, color.BLUE, (200, 180), (300, 100))
pygame.draw.line(screen, color.BLUE, (200, 180), (300, 300), 3)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
