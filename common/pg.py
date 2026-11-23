import pygame

def init_screen(size, caption, color):
    pygame.init()
    pygame.display.set_caption(caption)
    screen = pygame.display.set_mode(size)
    screen.fill(color)
    return screen