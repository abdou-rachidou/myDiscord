# canaux.py
from database import Database

class Canaux:
    def __init__(self) -> None:
        self.table = 'canaux'
        self.database = Database(host='localhost', user='root', password='Wendya30@', database='mydiscord')

    def create_canal(self, nom, type_canal, id_serveur, public):
        query = f'INSERT INTO {self.table} (nom_canal, type_canal, id_serveur, public) VALUES (%s, %s, %s, %s)'
        params = (nom, type_canal, id_serveur, public)
        self.database.executeQuery(query, params)

    def read_canaux(self, id_serveur):
        query = f'SELECT * FROM {self.table} WHERE id_serveur = %s'
        params = (id_serveur,)
        return self.database.fetch(query, params)

    def modifier_canal(self, id_canal, nom, type_canal, public):
        query = f'UPDATE {self.table} SET nom_canal=%s, type_canal=%s, public=%s WHERE id_canal=%s'
        params = (nom, type_canal, public, id_canal)
        self.database.execute_query(query, params)

    def supprimer_canal(self, id_canal):
        query = f'DELETE FROM {self.table} WHERE id_canal=%s'
        params = (int(id_canal),)
        self.database.execute_query(query, params)

    def get_canal_by_nom(self, nom):
        query = f'SELECT * FROM {self.table} WHERE nom_canal = %s'
        params = (nom,)
        return self.database.fetch(query, params)

    def get_canal_by_type(self, type_canal):
        query = f'SELECT * FROM {self.table} WHERE type_canal = %s'
        params = (type_canal,)
        return self.database.fetch(query, params)
