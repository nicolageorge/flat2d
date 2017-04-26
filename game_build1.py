# Pygame is a Python Wraper for Simple DirectMedia Layer (SDL) . Pygame 
# focuses on bringing the world of graphics and game programming to 
# programmers in an easy and efficient way.

# Typically Pygame projects are small, simple, two dimenstional. Ex:
# - PyPlace - 2Dimnsional isometric engine
# - AutoManga - cell based anime-style animation engine

# SDL is considered an alternative to DirectX especially on linux machines.
#As a multimedia and graphics library, SDL provides low level access to a 
# computer's video, sound, keyboard, mouse and joystick.

# SDL is similar in structure to a very rudimentary version of DirectX, 
# the big difference being that SDL is open source, supports multiple OS(
# Linux, Mac, Solaris, FreeeBSD and Windows) and has an API binding to 
# other languages ( including Python)

# The general problem is the lack of documentation which leads new 
# developers to go through the Pygame package, looking for information. 
# However, if you browse through you will find an overwhelming amount of 
# classes at the top of the index, making the package seem confusing. The 
# thing is that you can do a great deal with a few functions and you may
# never need to use many of the classes.
import pygame
from pygame import *

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

    while 1:
        timer.tick(60)


# __name__
# Every module has a name and statements in a module can find out the name 
# of its module. This is especially handy in one particular situation - 
# As mentioned previously, when a module is imported for the first time,
# the main block in that module is run. What if we want to run the 
# block only if the program was used by itself and not when it was 
# imported from another module? This can be achieved using the 
# __name__ attribute of the module.

if __name__== "__main__":
    main()
