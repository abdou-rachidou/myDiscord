# messages.py
from database import Database
import re

class Messages:
    def __init__(self) -> None:
        self.table = 'messages'
        self.database = Database(host='abdou-rachidou-arouna.students-laplateforme.io', user='mydiscord1', password='Vkiy159!2', database='abdou-rachidou-arouna_mydiscord')

    
    def create_message(self, contenu_message, id_utilisateur, id_room):
    
        query = f'INSERT INTO {self.table} (contenu_message, heure_publication, id_utilisateur, room_id) VALUES (%s, CURRENT_TIMESTAMP, %s, %s)'
        params = (contenu_message, id_utilisateur, id_room)
        self.database.executeQuery(query, params)

    def read_messages(self):
        query = f'''
            SELECT m.id_message, m.contenu_message, m.heure_publication, u.nom, u.prenom
            FROM {self.table} m
            JOIN utilisateurs u ON m.id_utilisateur = u.id_utilisateur
        '''
        results = self.database.fetch(query)

        # Vérifier si results est None
        if results is None:
            print("Aucun résultat trouvé dans la base de données.")
            return []

        # Imprimer les résultats pour le débogage
        print("Résultats de la base de données:", results)

        # Convertir les tuples en dictionnaires si nécessaire
        messages = [{'id_message': row[0], 'content': row[1], 'timestamp': row[2], 'sender': f"{row[3]} {row[4]}"}
                    for row in results]

        return messages

        

    def modifier_message(self, id_message, contenu):
        query = f'UPDATE {self.table} SET contenu_message=%s WHERE id_message=%s'
        params = (contenu, id_message)
        self.database.executeQuery(query, params)

    def supprimer_message(self, id_message):
        query = f'DELETE FROM {self.table} WHERE id_message=%s'
        params = (int(id_message),)
        self.database.executeQuery(query, params)

    def get_messages_by_utilisateur(self, id_utilisateur):
        query = f'SELECT * FROM {self.table} WHERE id_utilisateur = %s'
        params = (id_utilisateur,)
        return self.database.fetch(query, params)

    def get_messages_by_canal(self, id_canal):
        query = f'SELECT * FROM {self.table} WHERE id_canal = %s'
        params = (id_canal,)
        return self.database.fetch(query, params)
    
    def get_message_id(self, id_message):
        query = f'DELETE FROM {self.table} WHERE id_message=%s'
        params = (int(id_message),)
        self.database.executeQuery(query, params)
