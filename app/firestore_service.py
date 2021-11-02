import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# De esta manera obtenemos la credencia de login
credential = credentials.ApplicationDefault()

# inicializamos
firebase_admin.initialize_app(credential)

# Creamps la nueva instancia para comunicarnos cn la bas de datos
db = firestore.client()

# Traer todo lo de los usuarios
def get_users():
    # Vamos a retornar los datos en la colección
    return db.collection('users').get()

# traer los todos
def get_todos(user_id):
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()