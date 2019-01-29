import pygame
import random


class Mole(pygame.sprite.Sprite):

    def __init__(self, gamesurface):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 1
        self.orig_sprite = pygame.image.load("mole1.png")
        self.sprite = self.orig_sprite
        self.index = 0
        self.gamesurface = gamesurface
        self.time = 0
        self.sprite1 = pygame.image.load("mole2.png")
        self.spritehit = pygame.image.load("molehit.png")
        self.rect = self.sprite.get_rect()


    #TODO detect collision with players or other moles. player collision = spritechange, mole collision = generate new moleposition

    def detect_collision(self,object,debug_mode = False):
        collision = False
        if self.rect.colliderect(object):
            collision = True
        return collision


    def spriteanim(self):
        if self.index == 0:
            self.sprite = self.orig_sprite
            self.index += 1
        else:
            self.sprite = self.sprite1
            self.index -= 1

        if 0 > self.index >= 2:
            self.index = 0


    def spritehover(self,hit):
        if hit:
            self.sprite = self.spritehit
            #oldcenter = self.rect.center
            #self.sprite.get_rect(center=oldcenter)

        else:
            self.sprite = self.orig_sprite
            #oldcenter = self.rect.center
            #self.sprite.get_rect(center=oldcenter)


    def drawmole(self, coords):

        self.gamesurface.blit(self.sprite, coords)