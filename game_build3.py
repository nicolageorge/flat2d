# import pygame
import pygame
from pygame import *

window_height = 480
window_width  = 640

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Player(Entity):
    def __init__(self):
        pass

    def update():
        pass

    def collide():
        pass


class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#DDDD00"))
        # Rect(left, top, width, height) 
        self.rect = Rect(x, y, 32, 32)


def main():
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    timer = pygame.time.Clock()

    bg = Surface((32, 32))
    bg.convert()
    bg.fill(Color("#000000"))
    entities = pygame.sprite.Group()
    
    # 20 columns, 640 / 32
    # 15 rows, 480 / 32
    level = [
        "PPPPPPPPPPPPPPPPPPPP",
        "P                  P",
        "P                  P",
        "P   PPP            P",
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
    x = y = 0
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                entities.add(p)
            x += 32
        y += 32
        x = 0


    while 1:
        timer.tick(60)
        # this gets input from the user. Pygame understands basic windows
        # commands. Pygame.event handles anything that newwds to go to the 
        # event queue. Input from any sort of device, keyboard, joystick, etc
        # This creates a new event object that goes to the queue
        # pygame.event.get gets events from the queue.
        # Types of events:
        # QUIT - quit or close button
        # ACTIVEEVENT - constains state or gain
        # KEYDOWN - Unicode Key when pressed
        # KEYUP - unicode key when release
        # MOUSEMOTION - mouse position
        # MOUSEBUTTONDOWN - Position mouse button pressed
        # MOUSEBUTTONUP - position when released
        # JOYBUTTONDOWN - joystick button pressed
        # JOYBUTTONUP - joystick button released
        # VIDEORESIZE - window or video resize
        # USEREVENT - coded user event

        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "QUIT"

        # draw background
        for y in range(32):
            for x in range(32):
                screen.blit(bg, (x*32, y*32))

        # draw the entities
        entities.draw(screen)

        pygame.display.update()


if __name__== "__main__":
    main()
