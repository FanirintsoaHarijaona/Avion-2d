"""fichier spécifiant les traits d'un joueur"""
import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player,self).__init__()
        #surface sur lequel on va contenir l'image du joueur
        self.surface = pygame.image.load("assets/fusee.jpeg").convert_alpha()
        self.surface = pygame.transform.scale(self.surface,(75,25))
        pygame.transform.rotate(self.surface,90)
        self.surface.set_colorkey((255,255,255),RLEACCEL)
        self.rect = self.surface.get_rect()
        
    
    def getDimensions(self):
        return self.rect

    def blit(self, screen):
        screen.blit(self.surface,(self.rect))

    def update(self, pressed_keys):
    #garder le joueur dans la fenêtre
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
            if self.rect.top<=0:
                self.rect.top=0
        elif pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
            if self.rect.bottom>=500:
                self.rect.bottom=500 
        elif pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
            if self.rect.left<0:
                self.rect.left=0
        elif pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)
            if self.rect.right>500:
                self.rect.right=500
        
        
        
        
        
        
