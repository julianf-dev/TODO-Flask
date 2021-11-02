from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config
from .auth import auth

#Se crea e inicializa la aplicación  y la keysecret se importa desde config

def create_app():
    
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)
    #Registramos o creamos el blueprint
    app.register_blueprint(auth)

    return app