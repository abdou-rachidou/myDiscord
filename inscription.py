import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from utilisateurs import Utilisateurs
from PIL import Image, ImageTk
import os

class PageInscription:
    def __init__(self, root):
        self.root = root
        self.utilisateur = Utilisateurs()
        self.createUtilisateur()

    def createUtilisateur(self):
        # Définir la géométrie pour agrandir la fenêtre
        self.root.geometry("1000x800")
        # Centrer la fenêtre par rapport à l'écran
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - 1000) // 2
        y_position = (screen_height - 800) // 2
        self.root.geometry(f"1000x800+{x_position}+{y_position}")

        # Configurer les colonnes pour qu'elles s'étirent horizontalement
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        # Configurer les lignes pour qu'elles s'étirent verticalement
        for i in range(7):  # Augmenté à 7 pour ajouter une ligne pour le titre
            self.root.rowconfigure(i, weight=1)

        # Changer la couleur de fond de la fenêtre
        self.root.configure(bg="#313339")

        # Ajouter le titre au-dessus des labels
        Label(self.root, text="Page d'inscription", font=("Helvetica", 20), bg="#313339", fg="white").grid(row=0, column=0, columnspan=3, pady=(10, 0))

        # Ajouter le logo
        self.ajouter_logo()

        # Création des labels et entry widgets pour chaque champ du produit
        label_styles = {"font": ("Helvetica", 18), "bg": "#313339", "fg": "#8A8E92"}
        entry_styles = {"font": ("Helvetica", 18), "bg": "#424549", "fg": "white"}

        Label(self.root, text="Nom :", **label_styles).grid(row=2, column=0, sticky="e", pady=(7, 0))
        self.nom_entry = Entry(self.root, **entry_styles)
        self.nom_entry.grid(row=2, column=1, pady=(7, 0), ipady=5, sticky="ew")  # Ajustement pour centrer l'entrée

        Label(self.root, text="Prenom :", **label_styles).grid(row=3, column=0, sticky="e", pady=(7, 0))
        self.prenom_entry = Entry(self.root, **entry_styles)
        self.prenom_entry.grid(row=3, column=1, pady=(7, 0), ipady=5, sticky="ew")  # Ajustement pour centrer l'entrée

        Label(self.root, text="Email :", **label_styles).grid(row=4, column=0, sticky="e", pady=(7, 0))
        self.email_entry = Entry(self.root, **entry_styles)
        self.email_entry.grid(row=4, column=1, pady=(7, 0), ipady=5, sticky="ew")  # Ajustement pour centrer l'entrée

        Label(self.root, text="Mot de passe :", **label_styles).grid(row=5, column=0, sticky="e", pady=(7, 0))
        self.mot_de_passe_entry = Entry(self.root, show="*", **entry_styles)
        self.mot_de_passe_entry.grid(row=5, column=1, pady=(7, 0), ipady=5, sticky="ew")  # Ajustement pour centrer l'entrée

        # Changer la couleur de fond des boutons
        button_styles = {"bg": "#424549", "fg": "white"}

        cancel_button = Button(self.root, text="Annuler", command=self.root.destroy, **button_styles)
        cancel_button.grid(row=7, column=0, pady=10, sticky="nsew")

        save_button = Button(self.root, text="Enregistrer", command=self.save_user, **button_styles)
        save_button.grid(row=7, column=2, pady=10, sticky="nsew")

    def ajouter_logo(self):
        # Obtenez le chemin absolu du répertoire du script
        script_directory = os.path.dirname(os.path.abspath(__file__))

        # Construisez le chemin complet vers l'image
        image_path = os.path.join(script_directory, "images", "logo-discord.png")

        # Charger le logo
        logo_image = Image.open(image_path)
        
        # Agrandir l'image de 5%
        width, height = logo_image.size
        new_width = int(width * 0.35)
        new_height = int(height * 0.35)
        logo_image = logo_image.resize((new_width, new_height), Image.LANCZOS)
        
        logo_photo = ImageTk.PhotoImage(logo_image)

        # Créer un label pour afficher le logo
        logo_label = Label(self.root, image=logo_photo, bg="#313339")
        logo_label.image = logo_photo  # Gardez une référence pour éviter la suppression par le garbage collector
        logo_label.grid(row=1, column=0, columnspan=3, pady=(20, 0))  # Augmentez la valeur de pady pour ajuster l'espacement

    def save_user(self):
        nom = self.nom_entry.get()
        prenom = self.prenom_entry.get()
        email = self.email_entry.get()
        mot_de_passe = self.mot_de_passe_entry.get()

        # Valider les données avant de les envoyer à la base de données
        if not self.utilisateur.validation_email(email):
            messagebox.showerror("Erreur", "Adresse email invalide.")
            return
    
        if not self.utilisateur._validation_password(mot_de_passe):
            messagebox.showerror("Erreur", "Mot de passe invalide.")
            return

        # Appel de la méthode pour enregistrer l'utilisateur dans la base de données
        add_result = self.utilisateur.Create_utilisateur(nom, prenom, email, mot_de_passe)
        self.root.destroy()  # Fermer la fenêtre après avoir ajouté l'utilisateur

        if add_result:
            messagebox.showinfo("Succès", "Votre inscription est complète.")
        else:
            messagebox.showerror("Erreur", "Une erreur s'est produite lors de l'inscription.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PageInscription(root)
    root.mainloop()
