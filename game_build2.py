# import pygame
import pygame
from pygame import *

window_height = 480
window_width  = 640

DISPLAY = (window_width, window_height)
DEPTH = 32
FLAGS = 0

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pass


class Player(Entity):
    def __init__(self):
        pass

    def update():
        pass

    def collide():
        pass


class Platform(Entity):
    def __init__(self):
        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    bg = Surface((32, 32))
    bg.convert()
    bg.fill(Color("#000000"))
    while 1:
        timer.tick(60)
        #draw background
        for y in range(32):
            for x in range(32):
                screen.blit(bg, (x*32, y*32))

        pygame.display.update()


if __name__== "__main__":
    main()
