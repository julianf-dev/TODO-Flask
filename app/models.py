from os import stat
from flask_login import UserMixin
from .firestore_service import get_user

class UserData:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        ;param user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password

    # Implementamos un Query de un userModel-
    # Va a enviar un userloader o un username y se va
    # A retornar un UserModel que es el que va a usar
    # flask-login para validar la sessión

    @staticmethod
    def query(user_id):
        user_doc = get_user(user_id)
        #instanciamos userData
        user_data = UserData(
            username = user_doc.id,
            password=user_doc.to_dict()['password']
        )

        #Ahora vamos a crear un UserModel
        return UserModel(user_data)