import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from utilisateurs import Utilisateurs

class PageConnexion:
    def __init__(self, root):
        self.root = root
        self.root.title("Page de Connexion")
        self.utilisateur = Utilisateurs()

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
        for i in range(5):
            self.root.rowconfigure(i, weight=1)

        # Ajouter le titre au-dessus des labels
        Label(self.root, text="CONNEXION", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=2, pady=(10, 30))

        # Création des labels et entry widgets pour chaque champ
        Label(self.root, text="Email :", font=("Helvetica", 14)).grid(row=1, column=0, sticky="e", pady=(7, 0))
        self.email_entry = Entry(self.root)
        self.email_entry.grid(row=1, column=1, sticky="w", pady=(7, 0), padx=(0, 20), ipady=3)

        Label(self.root, text="Mot de passe :", font=("Helvetica", 14)).grid(row=2, column=0, sticky="e", pady=(7, 0))
        self.mot_de_passe_entry = Entry(self.root, show="*")
        self.mot_de_passe_entry.grid(row=2, column=1, sticky="w", pady=(7, 0), padx=(0, 20), ipady=3)

        # Bouton "Se Connecter"
        connecter_button = Button(self.root, text="Se Connecter", command=lambda: self.action("connecter"))
        connecter_button.grid(row=4, column=1, pady=10, sticky="nsew")

        # Bouton "Annuler"
        annuler_button = Button(self.root, text="Annuler", command=lambda: self.action("annuler"))
        annuler_button.grid(row=4, column=0, pady=10, sticky="nsew")

    def action(self, action_type):
        if action_type == "connecter":
            self.se_connecter()
        elif action_type == "annuler":
            self.annuler()

    def se_connecter(self):
        email = self.email_entry.get()
        mot_de_passe = self.mot_de_passe_entry.get()

        # Valider les données avant de les envoyer à la base de données
        if not self.utilisateur.validation_email(email):
            messagebox.showerror("Erreur", "Adresse email invalide.")
            return

        if not self.utilisateur._validation_password(mot_de_passe):
            messagebox.showerror("Erreur", "Mot de passe invalide.")
            return
        
        # Appel de la méthode pour se connecter
        is_connected = self.utilisateur.connexion(email, mot_de_passe)
        if is_connected:
            messagebox.showinfo("Succès", "Connexion réussie.")
            # Ajoutez ici la logique pour ce que vous souhaitez faire après une connexion réussie.
        else:
            messagebox.showerror("Erreur", "Connexion échouée. Vérifiez vos informations de connexion.")
        
    def annuler(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PageConnexion(root)
    root.mainloop()