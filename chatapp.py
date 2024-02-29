import tkinter as tk
from tkinter import ttk
import customtkinter
from chatroom import ChatRoom
from utilisateurs import Utilisateurs



class ChatRoomPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.chatroom = ChatRoom()
        self.user = Utilisateurs()
        self.title("My Discord App")
        self.geometry("1100x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # Créer un Label pour afficher le titre "Chat"
        title_label = tk.Label(self, text="Chats", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, padx=90, pady=10, sticky="nw")

        # Créer une Listbox
        self.listbox = tk.Listbox(self, font=("Helvetica", 14))
        self.listbox.grid(row=0, column=0, padx=5, pady=45, sticky="nw")

        # Ajouter des éléments à la Listbox
        salles_chat = self.chatroom.obtenir_salles_chat()
        for _, room_name in salles_chat:
            self.listbox.insert(tk.END, room_name)

        # Ajuster la taille de la Listbox
        self.listbox.config(width=25, height=15)  # Ajustez ces valeurs selon vos préférences


        # Créer un Label pour le titre "Créer un nouveau chat"
        title_new_chat_label = tk.Label(self, text="Créer un nouveau chat :", font=("Helvetica", 14, "bold"), pady=10)
        title_new_chat_label.grid(row=1, column=0, padx=15, pady=0, sticky="nw")

    
        # Créer un Entry pour le nom de la nouvelle salle de chat avec style
        entry_new_chat = tk.Entry(self, font=("Helvetica", 15), bg='white', bd=2, relief="solid")
        entry_new_chat.grid(row=1, column=0, padx=15, pady=40, sticky="nw")

        def button_callback():
            self.chatroom.creer_salle_chat()

        button = customtkinter.CTkButton(self, text="Valider", command=button_callback)
        button.grid(row=1, column=0, padx=30, pady=70, sticky="nw")

