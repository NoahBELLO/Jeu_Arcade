"""
Auteur : Noah BELLO

Nom du programme : Jeu de Pong
Date : 15/11/2022
"""

#Importation des fichiers et modules pour le bon fonctionnement du jeu
import pygame, sys
from game import Game
from image import Image

#Initialisation de la page
pygame.init()

pygame.display.set_caption("Jeu Pong") #Nom de la fenêtre
screen = pygame.display.set_mode((900, 500)) #Dimension de la fenêtre

#Création de la class Clock du module pygame.time
clock = pygame.time.Clock() 
FPS = 30

#Création de la variable de type Game et d'une variable booléen
game = Game(screen)
picture = Image() 
running = True

while running:
    screen.blit(picture.background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                game.joueur_1.vitesse_y_1 = -20
            elif event.key == pygame.K_s:
                game.joueur_1.vitesse_y_1 = 20
            elif event.key == pygame.K_UP:
                game.joueur_2.vitesse_y_2 = -20
            elif event.key == pygame.K_DOWN:
                game.joueur_2.vitesse_y_2 = 20        
            elif event.key == pygame.K_SPACE:
                game.balle_tire = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                    game.joueur_1.vitesse_y_1 = 0
            elif event.key == pygame.K_s:
                    game.joueur_1.vitesse_y_1 = 0
            elif event.key == pygame.K_UP:
                    game.joueur_2.vitesse_y_2 = 0
            elif event.key == pygame.K_DOWN:
                    game.joueur_2.vitesse_y_2 = 0  

        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            game.x_souris, game.y_souris = pygame.mouse.get_pos()
            game.event_souris(game.x_souris, game.y_souris)
            
    game.mouvement_joueur(game.joueur_1.vitesse_y_1, game.joueur_2.vitesse_y_2)

    game.fonctionnement_balle()

    game.balle.rect.clamp_ip(game.rect)

    if game.is_playing: game.start()

    else:
        game.acceuil(picture.button_play, picture.button_regle, picture.button_touche, picture.button_quit)    
        if game.but_du_jeu: game.fonction_retour(picture.button_retour, 1)
        
        elif game.touche: game.fonction_retour(picture.button_retour, 0)

    if game.etat_1:
        screen.blit(picture.image_pause, (0, 0))
        game.ecran_menu(picture.button_recom, picture.button_quit, picture.button_play)  

    if game.score_1 == 5 or game.score_2 == 5: game.afficher_victoire(picture.victoire, game.score_1, picture.button_quit, picture.button_recom)
    
    pygame.display.flip()

    clock.tick(FPS)