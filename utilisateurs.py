from database import Database
import re


class Utilisateurs:

    def __init__(self) -> None:
        self.table = 'utilisateurs'
        self.database = Database(host='abdou-rachidou-arouna.students-laplateforme.io', user='mydiscord1', password='Vkiy159!2', database='abdou-rachidou-arouna_mydiscord')

    def Create_utilisateur(self, nom, prenom, email, mot_de_passe):
        # Validation des données utilisateur
        if not self.validation_email(email): 
            raise ValueError("Adresse email invalide.")
        if not self._validation_password(mot_de_passe):
            raise ValueError("Mot de passe invalide.")

        # Insertion des données dans la base de données
        query = f'INSERT INTO {self.table} (nom, prenom, email, mot_de_passe) VALUES (%s, %s, %s, %s)'
        params = (nom, prenom, email, mot_de_passe)
    
        try:
            self.database.executeQuery(query, params)
            return True  # Succès
        except Exception as e:
            # Gestion des erreurs
            print(f"Erreur lors de la création de l'utilisateur : {e}")
            return False  # Échec

        
    def Read(self):
        query = f'SELECT * FROM {self.table}'
        return self.database.fetch(query)
    
    def Modifier(self, id, nom, prenom, email, mot_de_passe):
        query = f'UPDATE {self.table} SET nom=%s, prenom=%s, email=%s, mot_de_passe=%s WHERE id=%s'
        params = (nom, prenom, email, mot_de_passe, id)
        self.database.executeQuery(query, params)

    
    def Delete(self, id_utilisateur):
        query = f'DELETE FROM {self.table} WHERE id=%s'
        params = (int(id_utilisateur),)
        self.database.executeQuery(query, params)

    def get_utilisateur_by_nom(self, nom):
        query = f'SELECT * FROM {self.table} WHERE nom = %s'
        params = (nom,)
        return self.database.fetch(query, params)
    
    def get_utilisateur_by_prenom(self, prenom):
        query = f'SELECT * FROM {self.table} WHERE prenom = %s'
        params = (prenom,)
        return self.database.fetch(query, params)
    
    def get_utilisateur_by_email(self, email):
        query = f'SELECT * FROM {self.table} WHERE email = %s'
        params = (email,)
        return self.database.fetch(query, params)
    
    def validation_email(self, email):
        # Expression régulière pour valider l'adresse email
        pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
        # Validation de l'adresse email en utilisant l'expression régulière
        if re.match(pattern, email):
            return True
        else:
            print(f"Adresse email invalide : {email}")
            return False

        
    def _validation_password(self, mot_de_passe):
        # Vérifier la longueur du mot de passe
        if len(mot_de_passe) < 8:
            return False
        
        # Vérifier la complexité du mot de passe (par exemple, au moins une lettre majuscule, une lettre minuscule et un chiffre)
        has_uppercase = any(char.isupper() for char in mot_de_passe)
        has_lowercase = any(char.islower() for char in mot_de_passe)
        has_digit = any(char.isdigit() for char in mot_de_passe)
        
        if not (has_uppercase and has_lowercase and has_digit):
            return False 
        return True
    
    def connexion(self, email, mot_de_passe):
        # Valider les données avant de les envoyer à la base de données
        if not self.validation_email(email):
            raise ValueError("Adresse email invalide.")
        
        if not self._validation_password(mot_de_passe):
            raise ValueError("Mot de passe invalide.")

        # Vérifier si l'utilisateur existe dans la base de données
        query = f'SELECT * FROM {self.table} WHERE email = %s AND mot_de_passe = %s'
        params = (email, mot_de_passe)
        result = self.database.fetch(query, params)

        if result:
            return True  # Connexion réussie
        else:
            return False  # Échec de la connexion