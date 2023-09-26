"""
Auteur : Noah BELLO

Nom du programme : Création de la classe Joueur et ses modules
Date : 15/11/2022
"""

import pygame

class Joueur():
    def __init__(self, x, y, taille):
        self.x = x
        self.y = y
        self.taille = taille
        self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])
        self.vitesse_y_1 = 0
        self.vitesse_y_2 = 0
    
    def mouvement(self, vitesse):
        self.rect.y += vitesse

    def afficher(self, surface):
        pygame.draw.rect(surface, (0, 255, 35), self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 1)