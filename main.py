import tkinter as tk
from tkinter import Label, Button
from pageinscription import PageInscription
from pageconnexion import PageConnexion
from PIL import Image, ImageTk
import os

class PageAccueil:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Page d'Accueil")
        self.root.geometry("800x600")
        self.root.configure(bg="#313339")

        self.blanc = "#FFFFFF"
        self.gris = "#424549"
        self.gris_hover = "#313339"
        self.gris_clique = "#212225"

        # Obtenez les dimensions de l'écran
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculez les coordonnées pour centrer la fenêtre
        x_position = (screen_width - 800) // 2
        y_position = (screen_height - 600) // 2
        
        # Configurez la géométrie de la fenêtre
        self.root.geometry(f"800x600+{x_position}+{y_position}")

     
        self.afficher_widgets()


    def afficher_widgets(self):
        # Label de bienvenue
        label_bienvenue = Label(self.root, text="Bienvenue sur notre Plateforme", font=("Helvetica", 20), fg=self.blanc, bg="#313339")
        label_bienvenue.pack(pady=(30, 0))  # Ajustez la valeur de pady

        # Ajouter le logo
        self.ajouter_logo()

        # Bouton Se Connecter
        button_se_connecter = Button(self.root, text="Connexion", font=("Helvetica", 18), bg=self.gris, fg=self.blanc,
                                activebackground=self.gris_clique, activeforeground=self.blanc,
                                command=self.ouvrir_connexion)
        button_se_connecter.pack(pady=20, ipadx=30, ipady=15)

        # Bouton S'Inscrire
        button_s_inscrire = Button(self.root, text="Inscription", font=("Helvetica", 18), bg=self.gris, fg=self.blanc,
                                activebackground=self.gris_clique, activeforeground=self.blanc,
                                command=self.ouvrir_page_inscription)
        button_s_inscrire.pack(pady=20, ipadx=30, ipady=15)

    def ajouter_logo(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_directory, "images", "logo-discord.png")
        logo_image = Image.open(image_path)
        width, height = logo_image.size
        new_width = int(width * 0.35)
        new_height = int(height * 0.35)
        logo_image = logo_image.resize((new_width, new_height), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = Label(self.root, image=logo_photo, bg="#313339")
        logo_label.image = logo_photo
        logo_label.pack(pady=(30, 30))  # Placer le logo entre le titre et les boutons

    def ouvrir_page_inscription(self):
        fenetre_inscription = tk.Toplevel(self.root)
        page_inscription = PageInscription(fenetre_inscription)

    def ouvrir_connexion(self):
        fenetre_connexion = tk.Toplevel(self.root)
        page_connexion = PageConnexion(fenetre_connexion)
        
    def executer(self):
        self.root.mainloop()

# Création de l'instance de la classe et exécution de la page d'accueil
page_accueil = PageAccueil()
page_accueil.executer()