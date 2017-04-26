import pygame
from pygame import *

window_height = 480
window_width  = 640

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
    # The most important element is the suface. The surface is blank slate 
    # and is the space where we put lines images and colors. the display 
    # surface of the screen is set with pygame.display.set_mode()
    screen = pygame.display.set_mode((window_width, window_height))
    timer = pygame.time.Clock()
    
    # surfaces may be created with images (image.load()), text 
    # (font.render()) or just blank surfaces with Surface. this is the case
    bg = Surface((32, 32))

    # to convert various file formats into pixel format use the .convert 
    # surface method. Important because the SDL does not need to convert 
    # pixel formats on the fly. This will greatly impact speed and 
    # performance
    bg.convert()
    bg.fill(Color("#000000"))
    
    while 1:
        timer.tick(60)

        #draw background
        for y in range(32):
            for x in range(32):
                # BLIT = BLock Image Transfer
                # And when you use text, pygame renders it into an image 
                # then you have to blit it.
                screen.blit(bg, (x*32, y*32))

        pygame.display.update()


if __name__== "__main__":
    main()
