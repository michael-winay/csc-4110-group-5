import random
import pygame
from pygame import *
from pygame.display import *
from pygame.sprite import *

#sprites
class Mole(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)

        sprite_image_raw = image.load("mole.png").convert_alpha()
        self.image = transform.scale(sprite_image_raw, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def random_pos(self):
        self.rect.centerx = random.randrange(25, 475)
        self.rect.centery = random.randrange(25, 475)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def collide_point(self, pos):
        return self.rect.collidepoint(pos)

#game init
pygame.init()

screen = display.set_mode((500, 500))
screen_rect = screen.get_rect()
display.set_caption("Whack-a-mole")

background = image.load("grass.jpg")
mole = Mole(screen_rect.centerx, screen_rect.centery)

#main game loop
game_clock = time.Clock()

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == MOUSEBUTTONDOWN:
            if mole.collide_point(event.pos):
                mole.random_pos()
    
    screen.blit(background, (0, 0))
    mole.draw(screen)
    display.flip()

pygame.quit()