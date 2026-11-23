import pygame, sys
from common import color
from common import pg
from pygame.locals import *

s = pg.init_screen((500, 500), "5 линиий", color.GRAY)

pygame.draw.line(s, color.RED, (60, 60), (160, 60), 5)
pygame.draw.line(s, color.BLUE, (160, 60), (160, 160), 5)
pygame.draw.line(s, color.GREEN, (160, 160), (260, 160), 10)
pygame.draw.line(s, color.YELLOW, (260, 160), (260, 260), 10)
pygame.draw.line(s, color.BLACK, (260, 260), (360, 260), 10)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
