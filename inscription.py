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
        self.root.geometry("800x600")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - 800) // 2
        y_position = (screen_height - 600) // 2
        self.root.geometry(f"800x600+{x_position}+{y_position}")

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        for i in range(7):
            self.root.rowconfigure(i, weight=1)

        self.root.configure(bg="#313339")

        Label(self.root, text="Page d'inscription", font=("Helvetica", 20), bg="#313339", fg="white").grid(row=0, column=0, columnspan=3, pady=(10, 0))

        self.ajouter_logo()

        label_styles = {"font": ("Helvetica", 18), "bg": "#313339", "fg": "#8A8E92"}
        entry_styles = {"font": ("Helvetica", 16), "bg": "#424549", "fg": "white"}

        self.nom_entry = Entry(self.root, **entry_styles)
        self.nom_entry.grid(row=2, column=1, pady=(7, 0), ipady=5, sticky="ew")
        
        self.prenom_entry = Entry(self.root, **entry_styles)
        self.prenom_entry.grid(row=3, column=1, pady=(7, 0), ipady=5, sticky="ew")
        
        self.email_entry = Entry(self.root, **entry_styles)
        self.email_entry.grid(row=4, column=1, pady=(7, 0), ipady=5, sticky="ew")
        
        self.mot_de_passe_entry = Entry(self.root, show="*", **entry_styles)
        self.mot_de_passe_entry.grid(row=5, column=1, pady=(7, 0), ipady=5, sticky="ew")

        button_styles = {"bg": "#5F70BE", "fg": "white", "font": ("Helvetica", 16), "bd": 0, "relief": tk.FLAT, "border": 0}
        

        button_width = max(len("Annuler"), len("Enregistrer"))

        cancel_button = Button(self.root, text="Annuler", command=self.root.destroy, width=button_width, **button_styles)
        cancel_button.grid(row=7, column=0, pady=15, padx=10,ipady=5 ,sticky="nsew")
        
        save_button = Button(self.root, text="Enregistrer", command=self.save_user, width=button_width, **button_styles)
        save_button.grid(row=7, column=2, pady=15, padx=10, ipady=5, sticky="nsew")

        self.configure_placeholder()

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
        logo_label.grid(row=1, column=0, columnspan=3, pady=(20, 0))

    def init_placeholder(self, entry, placeholder_text):
        entry.insert(0, placeholder_text)
        entry.config(fg="grey")

        def on_entry_click(event):
            if entry.get() == placeholder_text:
                entry.delete(0, tk.END)
                entry.config(fg="white")

        def on_focus_out(event):
            if entry.get() == "":
                entry.insert(0, placeholder_text)
                entry.config(fg="grey")

        entry.bind("<FocusIn>", on_entry_click)
        entry.bind("<FocusOut>", on_focus_out)

    def configure_placeholder(self):
        self.init_placeholder(self.nom_entry, "Nom")
        self.init_placeholder(self.prenom_entry, "Prénom")
        self.init_placeholder(self.email_entry, "Email")
        self.init_placeholder(self.mot_de_passe_entry, "Mot de passe")

    def save_user(self):
        nom = self.nom_entry.get()
        prenom = self.prenom_entry.get()
        email = self.email_entry.get()
        mot_de_passe = self.mot_de_passe_entry.get()

        if not self.utilisateur.validation_email(email):
            messagebox.showerror("Erreur", "Adresse email invalide.")
            return
    
        if not self.utilisateur._validation_password(mot_de_passe):
            messagebox.showerror("Erreur", "Mot de passe invalide.")
            return

        add_result = self.utilisateur.Create_utilisateur(nom, prenom, email, mot_de_passe)
        self.root.destroy()

        if add_result:
            messagebox.showinfo("Succès", "Votre inscription est complète.")
        else:
            messagebox.showerror("Erreur", "Une erreur s'est produite lors de l'inscription.")