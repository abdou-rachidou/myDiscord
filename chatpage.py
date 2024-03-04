import tkinter as tk
import customtkinter
from chatroom import ChatRoom
from utilisateurs import Utilisateurs
from messages import Messages



class ChatPage(customtkinter.CTk):
    def __init__(self, room_name=None, current_user_id=None):
        super().__init__()

        self.chatroom = ChatRoom()
        self.user = Utilisateurs()
        self.message = Messages()
        self.title("My Discord App")
        self.geometry("1100x600")

        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate window position to center it on the screen
        x_position = (screen_width - 1100) // 2
        y_position = (screen_height - 600) // 2

        # Set window geometry to be centered
        self.geometry(f"1100x600+{x_position}+{y_position}")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)


    
        self.message_text = tk.Text(self, wrap=tk.WORD, selectbackground="lightgrey", height=15, width=50, font=("Arial", 16))
        self.message_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.message_text.config(state=tk.DISABLED)  # Rendre le widget Text en lecture seule


        # Ajouter une barre de défilement verticale à la liste
        scrollbar = tk.Scrollbar(self, command=self.message_text.yview)
        scrollbar.grid(row=0, column=1, pady=10, sticky="ns")  # Utilisez la colonne suivante (column=1)

        # Configurer la Listbox pour utiliser la scrollbar
        self.message_text.config(yscrollcommand=scrollbar.set)

        # Entrée de texte pour saisir le message
        self.message_entry = tk.Text(self, wrap=tk.WORD, height=5, width=50, font=("Arial", 17))
        self.message_entry.insert("1.0", "Tapez votre message ici")
        self.message_entry.bind("<FocusIn>", self.clear_placeholder)
        self.message_entry.bind("<FocusOut>", self.restore_placeholder)
        self.message_entry.grid(row=1, padx=10, pady=10)

        # Bouton pour envoyer le message
        send_button = customtkinter.CTkButton(self, text="Envoyer", command=self.send_message)
        send_button.grid(row=2, column=0, pady=10, )

        self.current_user_id = current_user_id  # Stockez l'ID de l'utilisateur


        # Lancer la méthode afficher_message après un court délai
        self.after(1, self.afficher_message)

    def afficher_message(self):
        # Récupérer la liste des messages depuis la base de données
        messages_list = self.message.read_messages()

        # Effacer le contenu actuel du widget Text
        self.message_text.config(state=tk.NORMAL)  # Autoriser les modifications pour effacer le contenu
        self.message_text.delete("1.0", tk.END)
        self.message_text.config(state=tk.DISABLED)  # Revenir en mode lecture seule

        # Ajouter chaque message au widget Text
        for message in messages_list:
            # Format du message avec nom et date au-dessus
            formatted_message = f"{message['content']}\n\n"

            # Utiliser la méthode insert du widget Text pour ajouter des éléments
            self.message_text.config(state=tk.NORMAL)  # Autoriser les modifications pour ajouter du texte
            self.message_text.insert(tk.END, f"{message['sender']} - {message['timestamp']}\n{formatted_message}")
            self.message_text.config(state=tk.DISABLED)  # Revenir en mode lecture seule

            # Faites défiler vers le bas pour voir les derniers messages
            self.message_text.yview(tk.END)


    def clear_placeholder(self, event):
        current_content = self.message_entry.get("1.0", "end-1c")
        if current_content == "Tapez votre message ici":
            self.message_entry.delete("1.0", tk.END)
            self.message_entry.config(fg='black')  # Change la couleur du texte pour distinguer du texte saisi


    def restore_placeholder(self, event):
        current_content = self.message_entry.get("1.0", "end-1c")
        if not current_content.strip():
            self.set_placeholder()

    def set_placeholder(self):
        self.message_entry.delete("1.0", tk.END)
        self.message_entry.insert("1.0", "Tapez votre message ici")
        self.message_entry.config(fg='blue')  # Change la couleur du texte pour distinguer du texte saisi


    def send_message(self):
        # Récupérer le contenu du message depuis l'entrée de texte
        contenu_message = self.message_entry.get("1.0", tk.END).strip()

        # Vérifier si le contenu du message est égal au placeholder
        if contenu_message == "Tapez votre message":
            print("Le contenu du message est vide.")
            return  # Ne rien faire si le contenu est égal au placeholder

        # Définir une valeur par défaut pour la salle de chat
        default_room_id = "1"

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

            # Utiliser la méthode get_current_user_id pour obtenir automatiquement l'ID de l'utilisateur
            current_user_id = self.user.recuperer_id_utilisateur()
            print(current_user_id)
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
        self.afficher_message()