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

def get_user(user_id):
    return db.collection('users').document(user_id).get()

#User put (esto es para enviar información a la BD)
def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password' : user_data.password })

# traer los todos
def get_todos(user_id):
    return db.collection('users').document(user_id).collection('todos').get()

#We create the puts to send a database (se recibe el user_id porque va a estar en la coleccion del usuario)
#Y tambiens e envia la descricion del todo
def put_todo(userd_id , description):
    #COn esto llamaos la bd
    todos_collection_ref = db.collection('users').document(userd_id).collection('todos')
    #y ahora agregamos al documento de la coleccion 'todos'
    todos_collection_ref.add({'description':description})




