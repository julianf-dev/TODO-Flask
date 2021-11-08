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
    todos_collection_ref.add({'description':description, 'done':False})
    #El done nos ayuara a saber cuando la tearea este lista o no

#vamos a referencias 

def delete_todo(user_id, todo_id):
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.delete()
    
def update_todo(user_id, todo_id, done):
    #transformamos la variable a booleana para que cambia cuando llegue al DB
    todo_done = not bool(done)
    todo_ref = _get_todo_ref(user_id, todo_id)
    #Actualizamos que no es un done
    todo_ref.update({'done': todo_done})

def _get_todo_ref(user_id, todo_id):
    return db.document('users/{}/todos/{}'.format(user_id, todo_id))
