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
        pygame.sprite.Sprite.__init__(self)


class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = Surface((32, 32))
        self.image.fill(Color("#0000FF"))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    def update(self, up, down, left, right, platforms):
        if up:
            # only jump if on onGround
            if self.onGround:
                self.yvel -= 20
        if down:
            # pass
            self.yvel = 8
        if left:
            self.xvel = -8
        if right:
            self.xvel = 8
        if not self.onGround:
            # accelerate with gravity
            self.yvel += 0.9
            # max falling speed
            if self.yvel > 50:
                self.yvel = 50

        if not(left or right):
            self.xvel = 0
        # if not(up or down):
            # self.yvel = 0

        # add velocity to x direction 
        self.rect.left += self.xvel
        #check for horizontal collisions
        self.collide(self.xvel, 0, platforms)

        # add velocity to y direction 
        self.rect.top += self.yvel
        # assume we re in the air
        self.onGround = False
        # check for vertical collisions
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom



class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#DDDDDD"))
        self.rect = Rect(x, y, 32, 32)

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Use arrows to move")
    timer = pygame.time.Clock()

    up = down = left = right = False
    bg = Surface((32, 32))
    bg.convert()
    bg.fill(Color("#000000"))

    entities = pygame.sprite.Group()
    player = Player(32, 32)
    platforms = []
    level = [
        "PPPPPPPPPPPPPPPPPPPP",
        "P                  P",
        "P                  P",
        "P                  P",
        "P                  P",
        "P   P  P  P  P     P",
        "P                  P",
        "P             P    P",
        "P                  P",
        "P       PPPPPPPPPP P",
        "P                  P",
        "P    P P  P  P   P P",
        "P                  P",
        "P                  P",
        "PPPPPPPPPPPPPPPPPPPP",
    ]

    # adding to entities
    x = y = 0
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            x += 32
        y += 32
        x = 0
    entities.add(player)

    while 1:
        timer.tick(60)
        
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False


        # draw background
        for y in range(32):
            for x in range(32):
                screen.blit(bg, (x*32, y*32))

        player.update(up, down, left, right, platforms)


        # draw the entities
        entities.draw(screen)

        pygame.display.update()


if __name__== "__main__":
    main()
