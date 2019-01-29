import pygame
import time
class Player(pygame.sprite.Sprite):

    def __init__(self, gamesurface):
        pygame.sprite.Sprite.__init__(self)
        self.gamesurface = gamesurface
        self.canvas = gamesurface.get_rect()
        self.time = 0
        self.score = 0
        self.x = 0
        self.y = 0
        self.orig_sprite = pygame.image.load("mallet.png").convert_alpha()
        self.rect = self.orig_sprite.get_rect()
        self.sprite = self.orig_sprite
        self.width = 100
        self.height = 100

        self.internal_clock = pygame.time.Clock()
        gamesurface.blit(self.sprite, [self.x, self.y])



    # def rotatePlayer(self,angle):
    #     self.rect = self.sprite.get_rect()
    #     self.sprite = pygame.transform.rotate(self.sprite,angle)
    #     pygame.display.update()
    #
    #     #self.sprite = self.orig_sprite
    #     #pygame.display.update()


    def placePlayer(self, coords):
        self.rect = self.orig_sprite.get_rect()
        self.rect.x = coords[0] - 50
        self.rect.y = coords[1] - 50
        self.gamesurface.blit(self.sprite,(self.rect.x,self.rect.y))

    def decreaseTime(self):
        self.time -= 1
        return self.time

    def increaseScore(self):
        self.score += 10
        return self.score

    def hitMallet(self,angle, coords):
        game_rect = self.gamesurface.get_rect()
        self.rect = self.orig_sprite.get_rect(center = game_rect.center)
        self.sprite = pygame.transform.rotate(self.sprite, angle)

        #self.sprite = pygame.transform.rotate(self.sprite, 90)

    def detect_collision(self, objectdetect, debug_mode=False):
        collision = False
        if self.rect.colliderect(objectdetect):
            #print('hammer collided')
            collision = True
        # if objectdetect.x >= self.x and objectdetect.x <= self.x + self.width or objectdetect.x + objectdetect.width >= self.x + self.width and objectdetect.x + objectdetect.width <= self.x+self.width:
        #     if debug_mode:
        #         print("In the X boundary")
        #     if objectdetect.y >= self.y and objectdetect.y <= self.y + self.height or objectdetect.y + objectdetect.height >= self.y + self.height and objectdetect.y + objectdetect.height <= self.y + self.height:
        #         if debug_mode:
        #             print("In the Y boundary. Object Collided!")
        #         collision = True
        return collision