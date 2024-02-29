import tkinter as tk
from tkinter import ttk
import customtkinter
from chatroom import ChatRoom
from utilisateurs import Utilisateurs
from messages import Messages

ROUGE = "red"
BLEUE = "blue"
ROSE = "pink"
VERT = "green"
GRIS = "grey"
BLANC_F = "whitesmoke"
BLANC = "white"
NOIR = "black"

class ChatPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.chatroom = ChatRoom()
        self.user = Utilisateurs()
        self.message = Messages()
        self.title("My Discord App")
        self.geometry("1100x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)


    
        # Utilisez un widget Text au lieu d'une Listbox
        self.message_text = tk.Text(self, wrap=tk.WORD, selectbackground="lightgrey", height=15, width=50, font=("Arial", 16))
        self.message_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


        # Ajouter une barre de défilement verticale à la liste
        scrollbar = tk.Scrollbar(self, command=self.message_text.yview)
        scrollbar.grid(row=0, column=1, pady=10, sticky="ns")  # Utilisez la colonne suivante (column=1)

        # Configurer la Listbox pour utiliser la scrollbar
        self.message_text.config(yscrollcommand=scrollbar.set)

        # Entrée de texte pour saisir le message
        self.message_entry = tk.Text(self, wrap=tk.WORD, height=5, width=50, font=("Arial", 17))
        self.message_entry.grid(row=1, padx=10, pady=10)

        # Bouton pour envoyer le message
        send_button = customtkinter.CTkButton(self, text="Envoyer", command=self.send_message)
        send_button.grid(row=2, column=0, pady=10, )

        # Lancer la méthode afficher_message après un court délai
        self.after(1, self.afficher_message)

    def afficher_message(self):
        # Effacer le contenu actuel de la Listbox
        self.message_text.delete("1.0", tk.END)
        # Récupérer la liste des messages depuis la base de données
        messages_list = self.message.read_messages()

        # Ajouter chaque message à la Listbox
        for message in messages_list:
            # Format du message avec nom et date au-dessus
            formatted_message = f"{message['content']}\n\n"

            # Utiliser la méthode insert de la Listbox pour ajouter des éléments
            self.message_text.insert(tk.END, f"{message['sender']} - {message['timestamp']}\n{formatted_message}")

            # Faites défiler vers le bas pour voir les derniers messages
            self.message_text.yview(tk.END)

    def send_message(self):
        # Récupérer le contenu du message depuis l'entrée de texte
        contenu_message = self.message_entry.get("1.0", tk.END).strip()

        # Définir une valeur par défaut pour la salle de chat
        default_room_id = "4"

        # Vérifier si le contenu du message n'est pas vide
        if not contenu_message:
            print("Le contenu du message est vide.")
        elif self.chatroom.get_current_room() is None:
            # Utiliser la valeur par défaut si aucune salle de chat n'est sélectionnée
            print("Aucune salle de chat sélectionnée. Utilisation de la salle par défaut.")
            room_id = default_room_id
        else:
            # Utiliser la salle de chat actuelle
            room_id = self.chatroom.get_current_room()

        # Vous pouvez utiliser les instances d'Utilisateurs et ChatRoom pour récupérer les informations
        current_user_id = "3"

        # Utilisez la méthode get_room_name_by_id pour obtenir dynamiquement le nom de la salle actuelle
        room_name = "Club de Volley ball"
        

        # Ajoutez des impressions pour vérifier les valeurs
        print(f"contenu_message: {contenu_message}")
        print(f"current_user_id: {current_user_id}")
        print(f"room_id: {room_id}")
        print(f"room_name: {room_name}")

        # Effacer le contenu du widget de texte
        self.message_entry.delete("1.0", tk.END)

        # Créer le message en utilisant le contenu, l'utilisateur actuel, le nom de la salle, etc.
        self.message.create_message(contenu_message, current_user_id, room_id)


app = ChatPage()
app.mainloop()