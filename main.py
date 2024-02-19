import pygame
import sys
from tkinter import Tk  # Importez la classe Tk depuis le module tkinter
from inscription import PageInscription
from connexion import PageConnexion

class PageAccueil:
    def __init__(self):
        pygame.init()

        self.largeur_fenetre = 800
        self.hauteur_fenetre = 600

        self.blanc = (255, 255, 255)
        self.noir = (0, 0, 0)
        self.gris = (255, 255, 255)  # Couleur de fond normale des boutons
        self.gris_hover = (150, 150, 150)  # Couleur de fond au survol
        self.gris_clique = (100, 100, 100)  # Couleur de fond lorsqu'un bouton est cliqué

        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))
        pygame.display.set_caption("Page d'Accueil")

        self.rect_se_connecter = pygame.Rect(250, 200, 300, 100)
        self.rect_s_inscrire = pygame.Rect(250, 350, 300, 100)

    def afficher_texte(self, texte, taille, couleur, position):
        font = pygame.font.Font(None, taille)
        texte_surface = font.render(texte, True, couleur)
        texte_rect = texte_surface.get_rect(center=position)
        self.fenetre.blit(texte_surface, texte_rect)

    def executer(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    if self.rect_se_connecter.collidepoint(x, y):
                        self.ouvrir_connexion()
                        # Ajoutez ici la logique pour ouvrir la page de connexion

                    elif self.rect_s_inscrire.collidepoint(x, y):
                        self.ouvrir_page_inscription()

            self.fenetre.fill(self.blanc)

            if self.rect_se_connecter.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.fenetre, self.gris_hover, self.rect_se_connecter)
                pygame.draw.rect(self.fenetre, self.noir, self.rect_se_connecter, 2)
            else:
                pygame.draw.rect(self.fenetre, self.gris, self.rect_se_connecter)
                pygame.draw.rect(self.fenetre, self.noir, self.rect_se_connecter, 2)

            if self.rect_s_inscrire.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.fenetre, self.gris_hover, self.rect_s_inscrire)
                pygame.draw.rect(self.fenetre, self.noir, self.rect_s_inscrire, 2)
            else:
                pygame.draw.rect(self.fenetre, self.gris, self.rect_s_inscrire)
                pygame.draw.rect(self.fenetre, self.noir, self.rect_s_inscrire, 2)

            self.afficher_texte("Bienvenue sur notre Plateforme", 60, self.noir, (self.largeur_fenetre // 2, 100))
            self.afficher_texte("Se Connecter", 40, self.noir, (self.largeur_fenetre // 2, 250))
            self.afficher_texte("S'Inscrire", 40, self.noir, (self.largeur_fenetre // 2, 400))

            pygame.display.flip()

    def ouvrir_page_inscription(self):
        self.fenetre_inscription = Tk()
        page_inscription = PageInscription(self.fenetre_inscription)
        self.fenetre_inscription.mainloop()

    def ouvrir_connexion(self):
        self.fenetre_connexion = Tk()
        page_connexion = PageConnexion(self.fenetre_connexion)
        self.fenetre_connexion.mainloop()


# Création de l'instance de la classe et exécution de la page d'accueil
page_accueil = PageAccueil()
page_accueil.executer()