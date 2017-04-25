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
        pygame.sprite.Sprite(__init__(self))


class Player(Entity):
    def __init__(self, x, y):
        pass

    def update():
        pass

    def collide():
        pass


class Platform(Entity):
    def __init__(self, x, y):
        Entity.init(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#DDDDDD"))
        self.rect = Rect(x, y, 32, 32)

def main():
    global cameraX, cameraY
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Use arrows to move")
    timer = pygame.time.Clock()

    bg = Surface((32, 32))
    bg.convert()
    bg.fill(Color("#000000"))

    entities = pygame.sprite.Group()
    level = [
        "PPPPPPPPPPPPPPPPPPPP",
        "P                  P",
        "P                  P",
        "P                  P",
        "P                  P",
        "P                  P",
        "P                  P",
        "P             P    P",
        "P                  P",
        "P       PPPPPPPPPP P",
        "P                  P",
        "P    P             P",
        "P                  P",
        "P                  P",
        "PPPPPPPPPPPPPPPPPPPP",
    ]
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                entities.add(p)
            x += 32
        y += 32
        x = 0


    while 1:

        # draw background
        for y in range(32):
            for x in range(32):
                screen.blit(bg, (x*32, y*32))

        # draw the entities
        entities.draw(screen)

        pygame.display.update()


if __name__== "__main__":
    main()