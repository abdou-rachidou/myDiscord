import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from utilisateurs import Utilisateurs
import os
from PIL import Image, ImageTk
from chatapp import ChatRoomPage

class PageConnexion:
    def __init__(self, root):
        self.root = root
        self.utilisateur = Utilisateurs()
        self.createPageConnexion()

    def createPageConnexion(self):
        self.root.title("Page de Connexion")
        self.root.configure(bg="#313339")
        self.root.geometry("800x600")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - 800) // 2
        y_position = (screen_height - 600) // 2
        self.root.geometry(f"800x600+{x_position}+{y_position}")

        self.root.columnconfigure(0, weight=1)

        for i in range(5):
            self.root.rowconfigure(i, weight=1)

        Label(self.root, text="Page de connexion", font=("Helvetica", 20), bg="#313339", fg="white").grid(row=0, column=0, pady=(10, 30), padx=(0, 10), sticky="n")

        # Appeler la méthode pour ajouter le logo
        self.ajouter_logo()

        entry_styles = {"font": ("Helvetica", 15), "bg": "#424549", "fg": "white"}

        self.email_entry = Entry(self.root, **entry_styles)
        self.email_entry.grid(row=1, column=0, pady=(7, 0), padx=(0, 10), ipady=3, sticky="n")
        self.init_placeholder(self.email_entry, "Email")

        self.mot_de_passe_entry = Entry(self.root, show="*", **entry_styles)
        self.mot_de_passe_entry.grid(row=2, column=0, pady=(7, 0), padx=(0, 10), ipady=3, sticky="n")
        self.init_placeholder(self.mot_de_passe_entry, "Mot de passe")

        button_frame = tk.Frame(self.root, bg="#313339")
        button_frame.grid(row=3, column=0, pady=0, sticky="nsew")

        button_width = 15  # Ajustez la largeur des boutons ici

        connecter_button = Button(button_frame, text="Se Connecter", command=lambda: self.action("connecter"), bg="#5F70BE", fg="white", font=("Helvetica", 18),
                                activebackground="#212225", activeforeground="white", width=button_width)
        connecter_button.grid(row=0, column=0, padx=(100, 100), sticky="nsew")

        annuler_button = Button(button_frame, text="Annuler", command=lambda: self.action("annuler"), bg="#5F70BE", fg="white", font=("Helvetica", 18),
                                activebackground="#212225", activeforeground="white", width=button_width)
        annuler_button.grid(row=0, column=1, padx=(100, 100), sticky="nsew")

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        # Configure la dernière ligne pour utiliser tout l'espace disponible
        self.root.rowconfigure(4, weight=0)
        
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
        logo_label.grid(row=0, column=0, columnspan=3, pady=(20, 0))

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

    def action(self, action_type):
        if action_type == "connecter":
            self.se_connecter()
        elif action_type == "annuler":
            self.annuler()

    def se_connecter(self):
        email = self.email_entry.get()
        mot_de_passe = self.mot_de_passe_entry.get()

        if not self.utilisateur.validation_email(email):
            messagebox.showerror("Erreur", "Adresse email invalide.")
            return

        if not self.utilisateur._validation_password(mot_de_passe):
            messagebox.showerror("Erreur", "Mot de passe invalide.")
            return

        is_connected = self.utilisateur.connexion(email, mot_de_passe)
        if is_connected:
            messagebox.showinfo("Succès", "Connexion réussie.")
            self.ouvrir_pagechatroom()  # Appel de la nouvelle méthode
            self.annuler()
            # Ajoutez ici la logique pour ce que vous souhaitez faire après une connexion réussie.
        else:
            messagebox.showerror("Erreur", "Connexion échouée. Vérifiez vos informations de connexion.")

    def ouvrir_pagechatroom(self): 
        chatroompage = ChatRoomPage()  # Passez la fenêtre en tant que parent


    def annuler(self):
        self.root.destroy()

# Instanciation de l'application
root = tk.Tk()
app = PageConnexion(root)
root.mainloop()