import pygame 
from pygame.locals import * #import des attributs et fonctions de pygame
from Player import *
from Missile import *



pygame.init()
screen=pygame.display.set_mode((500,500))


pygame.display.set_caption('Rocket')#changement du titre de la fenêtre
me=Player()#initialisation du player

#définir un temps pour les missiles
clock = pygame.time.Clock()



#évènement pérsonnalisé pour le jeu
ADDMISSILE = pygame.USEREVENT+1
pygame.time.set_timer(ADDMISSILE,250)

#création des obstacles
missiles=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
all_sprites.add(me)

#boucle principale du jeu
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                running=False
        elif event.type == ADDMISSILE:
            # Creation d'un nouveau missile
            new_missile = Missile()
            missiles.add(new_missile)
            all_sprites.add(new_missile)
    
    #gestion des inputs claviers
    keyPressed=pygame.key.get_pressed()
    
    #mis à jour du mouvement du joueur
    me.update(keyPressed)
    for missile in missiles:
        missile.update()
    
    screen.fill((0,0,0))

    #affichage des sprites
    for image in all_sprites:
        image.blit(screen)

    # vérifie si un ennemi entre en collision avec notre joueur
    if pygame.sprite.spritecollideany(me, missiles):
    # If so, then remove the player and stop the loop
        me.kill()
        running = False
    pygame.display.flip()
    #s'assure que le frame tient pendant 30 secondes
    clock.tick(30)
pygame.quit()