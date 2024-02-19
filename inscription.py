import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from utilisateurs import Utilisateurs

class PageInscription:
    def __init__(self, root):
        self.root = root
        self.utilisateur = Utilisateurs()
        self.createUtilisateur()

    def createUtilisateur(self):
        # Définir la géométrie pour agrandir la fenêtre
        self.root.geometry("800x600")
        # Centrer la fenêtre par rapport à l'écran
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - 800) // 2
        y_position = (screen_height - 600) // 2
        self.root.geometry(f"800x600+{x_position}+{y_position}")
        # Configurer les colonnes pour qu'elles s'étirent horizontalement
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # Configurer les lignes pour qu'elles s'étirent verticalement
        for i in range(7):  # Augmenté à 7 pour ajouter une ligne pour le titre
            self.root.rowconfigure(i, weight=1)

        # Ajouter le titre au-dessus des labels
        Label(self.root, text="INSCRIPTION", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=2, pady=(10, 0))

        # Création des labels et entry widgets pour chaque champ du produit
        Label(self.root, text="Nom :", font=("Helvetica", 14)).grid(row=1, column=0, sticky="e", pady=(7, 0))
        self.nom_entry = Entry(self.root)
        self.nom_entry.grid(row=1, column=1, sticky="w", pady=(7, 0), ipady=3)

        Label(self.root, text="Prenom :", font=("Helvetica", 14)).grid(row=2, column=0, sticky="e", pady=(7, 0))
        self.prenom_entry = Entry(self.root)
        self.prenom_entry.grid(row=2, column=1, sticky="w", pady=(7, 0), ipady=3)

        Label(self.root, text="Email :", font=("Helvetica", 14)).grid(row=3, column=0, sticky="e", pady=(7, 0))
        self.email_entry = Entry(self.root)
        self.email_entry.grid(row=3, column=1, sticky="w", pady=(7, 0), ipady=3)

        Label(self.root, text="Mot de passe :", font=("Helvetica", 14)).grid(row=4, column=0, sticky="e", pady=(7, 0))
        self.mot_de_passe_entry = Entry(self.root, show="*")
        self.mot_de_passe_entry.grid(row=4, column=1, sticky="w", pady=(7, 0), ipady=3)


        # Bouton "Cancel"
        cancel_button = Button(self.root, text="Annuler", command=self.root.destroy)
        cancel_button.grid(row=6, column=0, pady=10, sticky="nsew")
        # Bouton "Enregistrer le produit"
        save_button = Button(self.root, text="Enregistrer", command=self.save_user)
        save_button.grid(row=6, column=1, pady=10, sticky="nsew")

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