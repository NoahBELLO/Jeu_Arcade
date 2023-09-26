"""
Auteur : Noah BELLO

Nom du programme : Création de la classe Game et ses modules
Date : 15/11/2022
"""

import pygame, math, random, sys
from joueur import Joueur
from balle import Balle

class Game:
    
    def __init__(self, ecran):
        
        self.ecran = ecran
        self.is_playing = False

        self.vitesse_y_1, self.vitesse_y_2 = 0, 0
        self.joueur_1 = Joueur(20, 250, (20, 80))
        self.joueur_2 = Joueur(860, 250, (20, 80))
        
        self.rect = pygame.Rect(0, 0, 900, 500)

        self.balle_direction = [-1, 1]
        self.balle = Balle(450, 250, [10, 10], random.choice(self.balle_direction))
        self.balle_tire = False
        self.balle_vitesse_x, self.balle_vitesse_y = 15, 2

        self.score_1, self.score_2 = 0, 0

        self.x_souris, self.y_souris = 0, 0

        self.etat_1 = False
        self.but_du_jeu = False
        self.retour = False
        self.touche = False
        self.choix = False

    def start(self):
        self.is_playing = True

        self.afficher_score_bouton(self.ecran)

        self.balle.afficher(self.ecran)

        self.joueur_1.afficher(self.ecran)
        self.joueur_2.afficher(self.ecran)

    def mouvement_joueur(self, vitesse_1, vitesse_2):
        self.joueur_1.mouvement(vitesse_1)
        self.joueur_2.mouvement(vitesse_2) 

        self.joueur_1.rect.clamp_ip(self.rect)
        self.joueur_2.rect.clamp_ip(self.rect) 

    def acceuil(self, button_play, button_regle, button_touche, button_quit):
        self.ecran.blit(button_play, (210, 110))
        self.ecran.blit(button_regle, (500, 160))
        self.ecran.blit(button_touche, (270, 350))
        self.ecran.blit(button_quit, (500, 300))

        self.creer_message("Grande", f"Jeu de Pong", [225, 0, 20, 20], (0, 0, 0))

    def afficher_score_bouton(self, surface):
        image_pause = pygame.image.load("image/pause.png")
        image_pause_rect = pygame.Rect(380, 0, 225, 225)
        surface.blit(image_pause, image_pause_rect)

        self.creer_message("Petite", f"Joueur 1 : {self.score_1}", [100, 70, 20, 20], (0, 0, 0))
        self.creer_message("Petite", f"Joueur 2 : {self.score_2}", [535, 70, 20, 20], (0, 0, 0))

    def afficher_regle(self, button_retour):
        self.ecran.blit(button_retour, (0, 0))

        self.creer_message("Petite", "Règle du Jeu", [350, 50, 20, 20], (0, 0, 0))
        self.creer_message("Mini", "Les deux joueurs commandent chacun une raquette, représentée par un trait vertical aux", [0, 120, 20, 20], (0, 0, 0))
        self.creer_message("Mini", "extrémités gauche et droite du terrain de jeu.", [0, 150, 20, 20], (0, 0, 0))
        self.creer_message("Mini", "Le joueur déplace cette raquette en la faisant glisser verticalement entre les extrémités", [0, 200, 20, 20], (0, 0, 0))
        self.creer_message("Mini", "de l'écran à l'aide des contrôles.", [0, 220, 20, 20], (0, 0, 0))
        self.creer_message("Mini", "Si la balle frappe la raquette, elle rebondit vers l'autre joueur. Si elle manque la", [0, 250, 20, 20], (0, 0, 0))
        self.creer_message("Mini", "raquette, l'autre joueur marque un point.", [0, 270, 20, 20], (0, 0, 0))
        self.creer_message("Mini", "La vitesse de la balle augmente au cours de la partie, jusqu'à ce que l'un des joueurs", [0, 300, 20, 20], (0, 0, 0))
        self.creer_message("Mini", "perde le point.", [0, 320, 20, 20], (0, 0, 0))
        self.creer_message("Moyenne", "Le premier qui a 5 gagne !!!", [25, 400, 20, 20], (0, 0, 0))

    def afficher_touche(self, button_retour):
        self.ecran.blit(button_retour, (0, 0))

        self.creer_message("Petite", "Joueur 1", [0, 100, 20, 20], (0, 0, 0))
        self.creer_message("Mini", "Pour monter, la touche z", [0, 150, 20, 20], (0, 0, 0))
        self.creer_message("Mini", "Pour descendre, la touche s", [0, 170, 20, 20], (0, 0, 0))
        self.creer_message("Petite", "Joueur 2", [0, 250, 20, 20], (0, 0, 0))
        self.creer_message("Mini", "Pour monter, la touche flèche du haut", [0, 300, 20, 20], (0, 0, 0))
        self.creer_message("Mini", "Pour descendre, la touche flèche du bas", [0, 320, 20, 20], (0, 0, 0))
        self.creer_message("Mini", "Pour lancer la balle, la touche retour", [0, 400, 20, 20], (0, 0, 0))

    def changement_direction_balle(self, vitesse, angle):
        vitesse = -(vitesse * math.cos(angle))
        return vitesse

    def creer_message(self, font, message, message_rectangle, couleur):
        if font == "Mini":
            font = pygame.font.Font("image/my_font.ttf", 17)
        if font == "Petite":
            font = pygame.font.Font("image/my_font.ttf", 24)
        if font == "Moyenne":
            font = pygame.font.Font("image/my_font.ttf", 30)
        if font == "Grande":
            font = pygame.font.Font("image/my_font.ttf", 40)
        if font == "Maxi":
            font = pygame.font.Font("image/my_font.ttf", 80)
        
        message = font.render(message, True, couleur)
        self.ecran.blit(message, message_rectangle)

    def recommencer(self):
        self.score_1 = 0
        self.score_2 = 0

    def ecran_menu(self, button_recom, button_quit, button_play):
        self.ecran.blit(button_play, (150, -60))        
        self.ecran.blit(button_recom, (350, -60))
        self.ecran.blit(button_quit, (550, -60))

    def fonction_retour(self, button_retour, instruction):
        if instruction == 1:
            if not self.retour:            
                pygame.draw.rect(self.ecran, (150, 150, 150), (0, 0, 900, 500))
                self.afficher_regle(button_retour)
        else:
            if not self.retour:
                pygame.draw.rect(self.ecran, (0, 255, 255), (0, 0, 900, 500))
                self.afficher_touche(button_retour)

    def event_souris(self, souris_x, souris_y):
        if (souris_x < 310 and souris_x > 240 and souris_y < 220 and souris_y > 190):
            self.is_playing = True
                
        elif (souris_x < 535 and souris_x > 380 and souris_y < 40 and souris_y > 0):
            self.etat_1 = True

        elif (souris_x < 660 and souris_x > 520 and souris_y < 230 and souris_y > 190):
            self.but_du_jeu = True

        elif(souris_x < 50 and souris_x > 0 and souris_y < 45 and souris_y > 10):
            self.retour = True
            
        elif (souris_x < 370 and souris_x > 250 and souris_y < 450 and souris_y > 360):
            self.touche = True

        elif (souris_x < 310 and souris_x > 170 and souris_y < 55 and souris_y > 25):
            self.etat_1 = False
            
        elif (souris_x < 500 and souris_x > 200 and souris_y < 60 and souris_y > -15):
            self.recommencer()
            self.etat_1 = False       

        elif (souris_x < 710 and souris_x > 580 and souris_y < 50 and souris_y > 30):
            sys.exit() 
            
        elif (souris_x < 670 and souris_x > 520 and souris_y < 420 and souris_y > 380):
            sys.exit() 

        elif (souris_x < 130 and souris_x > 0 and souris_y < 45 and souris_y > 5):
            sys.exit()

        elif (souris_x < 280 and souris_x > 140 and souris_y < 40 and souris_y > 5):
            self.recommencer()

    def fonctionnement_balle(self):
        if self.balle_tire:
            self.balle.mouvement(self.balle_vitesse_x, self.balle_vitesse_y)

        if self.joueur_1.rect.colliderect(self.balle.rect) or self.joueur_2.rect.colliderect(self.balle.rect):
            self.balle_vitesse_x = self.changement_direction_balle(self.balle_vitesse_x, 0)
            self.balle_vitesse_y = self.changement_direction_balle(self.balle_vitesse_y, 60)
            self.balle.vitesse_aleatoire_y = random.randint(1, 15)

        if self.balle.rect.top <= 0 or self.balle.rect.bottom >= 500: self.balle_vitesse_y = self.changement_direction_balle(self.balle_vitesse_y, 0)

        if self.balle.rect.right >= 915:
            self.balle.rect.x, self.balle.rect.y = 450, 250
            self.score_1 += 1
            self.balle_tire = False

        if self.balle.rect.left <= -15:
            self.balle.rect.x, self.balle.rect.y = 450, 250
            self.score_2 += 1
            self.balle_tire = False

    def afficher_victoire(self, victoire, score, button_quit, button_recom):
        self.ecran.blit(victoire, (0, 0))
        
        self.ecran.blit(button_quit, (-30, -75))
        self.ecran.blit(button_recom, (110, -75))

        if score == 5: self.creer_message("Maxi", "Du Joueur 1", [10, 375, 20, 20], (255, 255, 225)) 
        else: self.creer_message("Maxi", "Du Joueur 2", [10, 375, 20, 20], (255, 255, 255))
    