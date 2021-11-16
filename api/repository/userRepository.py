from models.user import User
from models.response import Response
from db.db import connect

class UserRepository():
    def get_users(self):
        conn = connect()
        sql = '''
        SELECT 
        idutilisateur,
        nom, 
        prenom,
        adresse, 
        codepostal, 
        ville,
        pays,
        telephone,
        mail,
        username,
        password
        FROM utilisateur
        '''
        cursor = conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        liste = [User(**element) for element in res]
        for user in liste:
            if(user.identreprise != None):
                entreprise = entrepriseRepository.get_entreprise_by_id(
                    user.identreprise)
                user.entreprise = entreprise
            if(user.idclient != None):
                client = clientRepository.get_client_by_id(user.idclient)
                user.client = client
        utilisateurs = {
            "utilisateurs": liste,
            "nb_row": len(liste)
        }
        return utilisateurs

    def get_user_by_idutilisateur(self, idutilisateur):
        conn = connect()
        sql = '''
        SELECT 
        idutilisateur, 
        nom, 
        prenom,
        adresse, 
        codepostal, 
        ville,
        pays,
        telephone,
        mail,
        username,
        password
        FROM utilisateur
        where idutilisateur = :idutilisateur'''

        cursor = conn.cursor()
        cursor.execute(sql, {"idutilisateur": idutilisateur})
        user = User(**cursor.fetchone())
        return user

    def get_user_by_username(self, username):
        conn = connect()
        sql = '''
        SELECT 
        idutilisateur,  
        nom, 
        prenom,
        adresse, 
        codepostal, 
        ville,
        pays,
        telephone,
        mail,
        username,
        password
        FROM utilisateur
        where username = :username'''

        cursor = conn.cursor()
        cursor.execute(sql, {"username": username})
        user = User(**cursor.fetchone())
        return user

    def change_password(self, idutilisateur, password):
        conn = connect()
        sql = """
        UPDATE utilisateur
        SET password = :password
        WHERE idutilisateur = :idutilisateur"""

        cursor = conn.cursor()

        cursor.execute(sql, {
            "password": password,
            "idutilisateur": idutilisateur,
        })

        conn.commit()

        return {
            "success": True,
            "message": "Mot de passe modifié"
        }

    def usernameExists(self, username: str):
        conn = connect()
        sql = """
        SELECT count(idutilisateur) AS nbutilisateurs
        FROM utilisateur
        WHERE username like :username"""

        cursor = conn.cursor()
        cursor.execute(sql, {"username": username})
        nbutilisateurs = cursor.fetchone()["nbutilisateurs"]
        if nbutilisateurs > 0:
            return {"success": False, "message": username + " déjà présent en base"}
        return {"success": True, "message": username + " non présent en base"}
        