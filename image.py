"""
Auteur : Noah BELLO

Nom du programme : Création de la classe Image
Date : 15/11/2022
"""

import pygame

class Image:

    def __init__(self):
        #Création du fond d'écran
        self.background = pygame.image.load("image/terrain.jpg")
        self.background = pygame.transform.scale(self.background, (900, 500))

        #Création du bouton play
        self.button_play = pygame.image.load("image/play.png") 
        self.button_play = pygame.transform.scale(self.button_play, (200, 200))

        #Création du bouton règle
        self.button_regle = pygame.image.load("image/regle2.png")
        self.button_regle = pygame.transform.scale(self.button_regle, (1100, 800))

        #Création du bouton retour
        self.button_retour = pygame.image.load("image/retour.png")
        self.button_retour = pygame.transform.scale(self.button_retour, (50, 50))

        #Création du bouton touche
        self.button_touche = pygame.image.load("image/touche2.png")
        self.button_touche = pygame.transform.scale(self.button_touche, (100, 100))

        #Création du bouton quitter
        self.button_quit = pygame.image.load("image/quitter2.png")
        self.button_quit = pygame.transform.scale(self.button_quit, (200, 200))

        #Création du bouton recommencer
        self.button_recom= pygame.image.load("image/recommencer2.png")
        self.button_recom = pygame.transform.scale(self.button_recom, (200, 200))

        #Création de l'image de pause
        self.image_pause = pygame.image.load("image/image_pause.jpeg")
        self.image_pause = pygame.transform.scale(self.image_pause, (900, 500))

        #Création de l'image de victoire
        self.victoire = pygame.image.load("image/victoire.png")
        self.victoire = pygame.transform.scale(self.victoire, (900, 500))