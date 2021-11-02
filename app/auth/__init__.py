from flask import Blueprint

#Es como una aplicación de flask, ayuda para modulizar más

auth = Blueprint('auth', __name__, url_prefix='/auth')

#El url prefijo quiere decir que todas las rutas que comienzen co auth seran redirigdas}

from . import views