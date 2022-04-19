"""Importing """
from pickle import FALSE
import random
import pygame
import pickle
from os.path import exists
from pygame import *
from pygame.display import *
from pygame.sprite import *

#sprites
class Mole(Sprite):

    """
    Class to create moles

    Methods
    -----------
    random_pos():
        Gives a random position for mole

    draw(surface):
        Renders the mole into the foreground

    collide_point(pos):
        Makes a point in which mole hits other objects
    """

    def __init__(self, x: int, y: int) -> object:
        Sprite.__init__(self)

        sprite_image_raw = image.load("Project3/mole.png").convert_alpha()
        self.image = transform.scale(sprite_image_raw, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def random_pos(self):

        """
        Randomly positions the mole.

        Parameters
            self
        """
        self.rect.centerx = hole_horizontal[str(random.randrange(1, 4))]
        self.rect.centery = hole_vertical[str(random.randrange(1, 4))]

    def draw(self, surface):

        """
        Creates the mole for the game

        Parameters
            self.image - Picture of mole
            surface - Background on which to print image
        """
        surface.blit(self.image, self.rect)

    def collide_point(self, pos):

        """
        Creates a point on which the mole collides

        Parameters
            self
            pos - Position that the mole resides
        """
        return self.rect.collidepoint(pos)

#game init
pygame.init()

screen = display.set_mode((500, 500))
screen_rect = screen.get_rect()
display.set_caption("Whack-a-mole")
icon = pygame.image.load("Project3/whack-a-mole.png")


pygame.display.set_icon(icon)

# Static Hole PNG
holeimg = pygame.image.load("Project3/hole.png")
HOLE_LEFT = 50
HOLE_MIDDLE = 220
HOLE_RIGHT = 390
HOLE_TOP = 100
HOLE_MID = 250
HOLE_BOTTOM = 400
hole_horizontal = {"1": HOLE_LEFT + 33, "2": HOLE_MIDDLE + 33, "3": HOLE_RIGHT + 33}
hole_vertical = {"1": HOLE_TOP + 30, "2": HOLE_MID + 30, "3": HOLE_BOTTOM + 30}

def hole1():

    """
    Creates a mole-hole in top/left
    """
    screen.blit(holeimg, (HOLE_LEFT, HOLE_TOP))
def hole2():

    """
    Creates a mole-hole in top/middle
    """
    screen.blit(holeimg, (HOLE_MIDDLE, HOLE_TOP))
def hole3():

    """
    Creates a mole-hole in top/right
    """
    screen.blit(holeimg, (HOLE_RIGHT, HOLE_TOP))
def hole4():

    """
    Creates a mole-hole in mid/left
    """
    screen.blit(holeimg, (HOLE_LEFT, HOLE_MID))
def hole5():

    """
    Creates a mole-hole in mid/middle
    """
    screen.blit(holeimg, (HOLE_MIDDLE, HOLE_MID))
def hole6():

    """
    Creates a mole-hole in mid/right
    """
    screen.blit(holeimg, (HOLE_RIGHT, HOLE_MID))
def hole7():

    """
    Creates a mole-hole in bottom/left
    """
    screen.blit(holeimg, (HOLE_LEFT, HOLE_BOTTOM))
def hole8():

    """
    Creates a mole-hole in bottom/middle
    """
    screen.blit(holeimg, (HOLE_MIDDLE, HOLE_BOTTOM))
def hole9():

    """
    Creates a mole-hole in bottom/right
    """
    screen.blit(holeimg, (HOLE_RIGHT, HOLE_BOTTOM))

# Score
score_value = 0
highscore = 0
file_exists = exists("highscore.pickle")
if file_exists:
    pickle_off = open("highscore.pickle","rb")
    highscore = pickle.load(pickle_off)

font = pygame.font.Font(None, 32)

TEXT_X = 300
TEXT_Y = 10
HIGHSCORE_X = 100
HIGHSCORE_Y = 10

def show_score(x, y):

    """
    Renders current score at the middle/top of the screen

    Parameters
        x - Horizontal coordinate
        y - Vertical coordinate
    """
    score = font.render("Score: " + str(score_value), True, (0,0,0))
    screen.blit(score, (x, y))

def show_highscore(x, y):

    """
    Renders current score at the middle/top of the screen

    Parameters
        x - Horizontal coordinate
        y - Vertical coordinate
    """
    score = font.render("Highscore: " + str(highscore), True, (0,0,0))
    screen.blit(score, (x, y))

background = image.load("Project3/grass.jpg")
mole = Mole(screen_rect.centerx, screen_rect.centery)
mixer.music.load("Project3\smash.mp3") #loading music and hit sound

#main game loop
game_clock = time.Clock()

GAME_RUNNING = True
while GAME_RUNNING:
    for event in pygame.event.get():
        if event.type == QUIT:
            if score_value > highscore:
                highscore = score_value
            pickling_on = open("highscore.pickle","wb")
            pickle.dump(highscore, pickling_on)
            pickling_on.close()

            GAME_RUNNING = False

        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                GAME_RUNNING = False
        
        elif event.type == MOUSEBUTTONDOWN:
            if mole.collide_point(event.pos):
                mixer.music.play()               
                mole.random_pos()
                score_value += 1
                if score_value > highscore:
                    highscore = score_value
                
    screen.blit(background, (0, 0))
    hole1()
    hole2()
    hole3()
    hole4()
    hole5()
    hole6()
    hole7()
    hole8()
    hole9()
    mole.draw(screen)
    show_score(TEXT_X, TEXT_Y)
    show_highscore(HIGHSCORE_X, HIGHSCORE_Y)
    display.flip()

pygame.quit()
