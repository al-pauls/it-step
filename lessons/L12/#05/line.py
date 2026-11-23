import pygame, sys
from pygame.locals import *
pygame.init()
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("линия")
screen.fill(GREEN)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.line(screen, BLUE, (60, 60), (150, 60), 5)
    pygame.display.update()