import pygame, sys
from pygame.locals import *
pygame.init()
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("линия")
screen.fill(RED)
pygame.draw.line(screen,YELLOW , (25, 210), (245, 35), 7)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
