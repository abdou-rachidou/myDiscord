import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def executeQuery(self, query, params=None):
        try:
            self.connect()
            self.cursor.execute(query, params or ())
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'exécution de la requête : {err}")
            self.connection.rollback()
        finally:
            self.disconnect()

    def fetch(self, query, params=None):
        try:
            self.connect()
            self.cursor.execute(query, params or ())
            result = self.cursor.fetchall()
            # Ajoutez des impressions pour débogage
            print("Résultats de la base de données:", result)
            return result if result is not None else []
        
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'exécution de la requête : {err}")
        finally:
            self.disconnect()