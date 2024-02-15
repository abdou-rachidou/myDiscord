# messages.py
from database import Database

class Messages:
    def __init__(self) -> None:
        self.table = 'messages'
        self.database = Database(host='localhost', user='root', password='Wendya30@', database='store')

    def create_message(self, contenu, id_utilisateur, id_canal):
        query = f'INSERT INTO {self.table} (contenu_message, id_utilisateur, id_canal) VALUES (%s, %s, %s)'
        params = (contenu, id_utilisateur, id_canal)
        self.database.executeQuery(query, params)

    def read_messages(self, id_canal):
        query = f'SELECT * FROM {self.table} WHERE id_canal = %s'
        params = (id_canal,)
        return self.database.fetch(query, params)

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