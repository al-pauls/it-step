import pygame, sys, color
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("линия")
screen.fill(color.RED)
pygame.draw.line(screen,color.YELLOW , (25, 210), (245, 35), 7)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
