"""fichier définissant les énemis de notre joueur"""
import pygame
#position random des missiles
import random


class Missile(pygame.sprite.Sprite):

    def __init__(self):
        super(Missile,self).__init__()
        self.surface = pygame.image.load("assets/missile.jpeg").convert_alpha()
        self.surface = pygame.transform.scale(self.surface,(50,20))
        pygame.transform.rotate(self.surface,-45)
        #self.surface.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.surface.get_rect(center=(random.randint(520,600),random.randint(0, 500),))
        #rapidité du missile
        self.speed = random.randint(5,20)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right<0:
            self.kill()

    def blit(self, screen):
        screen.blit(self.surface,(self.rect))
        
        