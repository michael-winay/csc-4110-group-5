import random
import pygame
from pygame import *
from pygame.display import *
from pygame.sprite import *

#sprites
class Mole(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)

        sprite_image_raw = image.load("Project3/mole.png").convert_alpha()
        self.image = transform.scale(sprite_image_raw, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def random_pos(self):
        self.rect.centerx = random.randrange(25, 475)
        self.rect.centery = random.randrange(60, 475)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def collide_point(self, pos):
        return self.rect.collidepoint(pos)

#game init
pygame.init()

screen = display.set_mode((500, 500))
screen_rect = screen.get_rect()
display.set_caption("Whack-a-mole")
icon = pygame.image.load("Project3/whack-a-mole.png")
pygame.display.set_icon(icon)

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 180
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0,0,0))
    screen.blit(score, (x, y))

background = image.load("Project3/grass.jpg")
mole = Mole(screen_rect.centerx, screen_rect.centery)

# Static Hole PNG
holeimg = pygame.image.load("Project3/hole.png")
hole_left = 50
hole_middle = 220
hole_right = 390
hole_top = 100
hole_mid = 250
hole_bottom = 400

def hole1():
    screen.blit(holeimg, (hole_left, hole_top))
def hole2():
    screen.blit(holeimg, (hole_middle, hole_top))
def hole3():
    screen.blit(holeimg, (hole_right, hole_top))
def hole4():
    screen.blit(holeimg, (hole_left, hole_mid))
def hole5():
    screen.blit(holeimg, (hole_middle, hole_mid))
def hole6():
    screen.blit(holeimg, (hole_right, hole_mid))
def hole7():
    screen.blit(holeimg, (hole_left, hole_bottom))
def hole8():
    screen.blit(holeimg, (hole_middle, hole_bottom))
def hole9():
    screen.blit(holeimg, (hole_right, hole_bottom))

#main game loop
game_clock = time.Clock()

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False

        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                game_running = False

        elif event.type == MOUSEBUTTONDOWN:
            if mole.collide_point(event.pos):
                mole.random_pos()
                score_value += 1

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
    show_score(textX, textY)
    display.flip()

pygame.quit()