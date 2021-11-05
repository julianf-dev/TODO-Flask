from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .config import Config
from .auth import auth
from .models import UserData, UserModel

#Se crea e inicializa la aplicación  y la keysecret se importa desde config

#Instaniciamos la clase de login manager
login_manger = LoginManager()
#indicamos la ruta que queremos que maneje (esto es para proteger la ruta)
login_manger.login_view = 'auth.login'

#Implementamos la función looad_user de flask
@login_manger.user_loader
def load_user(username):
    return UserModel.query(username)

def create_app():
    
    app = Flask(__name__)

    bootstrap = Bootstrap(app)

    app.config.from_object(Config)
    #Inicializamos la app de login
    login_manger.init_app(app)
    #Registramos o creamos el blueprint
    app.register_blueprint(auth)

    return app