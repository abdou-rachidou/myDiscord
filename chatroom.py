from database import Database

class ChatRoom:
    def __init__(self):
        self.table = 'chatroom'
        self.database = Database(host='abdou-rachidou-arouna.students-laplateforme.io', user='mydiscord1', password='Vkiy159!2', database='abdou-rachidou-arouna_mydiscord')
        self.current_room_id = None


    def creer_salle_chat(self, room_name):
        query = "INSERT INTO chatroom (room_name) VALUES (%s)"
        params = (room_name,)
        self.database.executeQuery(query, params)


    def obtenir_salles_chat(self):
        query = "SELECT * FROM chatroom"
        resultats = self.database.fetch(query)

        # Traitez les résultats
        for _, room_name in resultats:
            print(room_name)

        # Retournez tous les résultats après avoir parcouru la boucle
        return resultats

    def salle_chat_existe(self, room_name):
        query = "SELECT COUNT(*) as count FROM chatroom WHERE room_name = %s"
        params = (room_name,)
        result = self.database.executeQuery(query, params)
        return result['count'] > 0
    
    def change_room(self, new_room_id):
        self.current_room_id = new_room_id

    def get_current_room(self):
        return self.current_room_id
    
    def get_current_room_name(self, room_name):
        # À définir en fonction de votre logique de récupération de l'ID de la salle par le nom
        query = f'SELECT id FROM {self.table} WHERE room_name = %s'
        params = (room_name,)
        result = self.database.fetch(query, params)

        if result:
            return result[0][0]  # Récupère l'ID depuis la première colonne de la première ligne
        else:
            return None  # Ou une valeur par défaut si la salle de chat n'est pas trouvée
        
    def get_room_name_by_id(self, room_id):
        query = f'SELECT room_name FROM {self.table} WHERE id = %s'
        params = (room_id,)
        result = self.database.fetch(query, params)

        if result:
            return result[0][0]  # Récupère le nom depuis la première colonne de la première ligne
        else:
            return None  # Ou une valeur par défaut si la salle de chat n'est pas trouvée