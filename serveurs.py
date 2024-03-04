# serveurs.py
from database import Database

class Serveurs:
    def __init__(self) -> None:
        self.table = 'serveurs'
        self.database = Database(host='localhost', user='root', password='Wendya30@', database='mydiscord')

    def create_serveur(self, nom, description, id_createur):
        query = f'INSERT INTO {self.table} (nom_serveur, description_serveur, id_createur) VALUES (%s, %s, %s)'
        params = (nom, description, id_createur)
        self.database.executeQuery(query, params)

    def read_serveurs(self):
        query = f'SELECT * FROM {self.table}'
        return self.database.fetch(query)

    def modifier_serveur(self, id_serveur, nom, description):
        query = f'UPDATE {self.table} SET nom_serveur=%s, description_serveur=%s WHERE id_serveur=%s'
        params = (nom, description, id_serveur)
        self.database.execute_query(query, params)

    def supprimer_serveur(self, id_serveur):
        query = f'DELETE FROM {self.table} WHERE id_serveur=%s'
        params = (int(id_serveur),)
        self.database.execute_query(query, params)

    def get_serveur_by_nom(self, nom):
        query = f'SELECT * FROM {self.table} WHERE nom_serveur = %s'
        params = (nom,)
        return self.database.fetch(query, params)

    def get_serveur_by_createur(self, id_createur):
        query = f'SELECT * FROM {self.table} WHERE id_createur = %s'
        params = (id_createur,)
        return self.database.fetch(query, params)