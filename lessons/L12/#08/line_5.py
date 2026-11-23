import pygame, sys
from common import color
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("5 линиий")
screen.fill(color.GRAY)
pygame.draw.line(screen, color.RED, (60, 60), (160, 60), 5)
pygame.draw.line(screen, color.BLUE, (160, 60), (160, 160), 5)
pygame.draw.line(screen, color.GREEN, (160, 160), (260, 160), 10)
pygame.draw.line(screen, color.YELLOW, (260, 160), (260, 260), 10)
pygame.draw.line(screen, color.BLACK, (260, 260), (360, 260), 10)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
