import pygame, sys
from pygame.locals import *
from common import color
from common import pg


screen = pg.init_screen((640, 480), "Круг", color.GREEN)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.circle(screen, color.RED, (300, 200), 100)
    pygame.display.update()