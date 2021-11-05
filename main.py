#variable de ambiente: set FLASK_APP=main.py
import unittest
from flask import  request, render_template, make_response, redirect,session
from flask_login import login_required, current_user

from app import create_app
from app.firestore_service import  get_todos, get_users
#Instanciamos nuestra app
app = create_app()
""" todos =  ['Comprar café', 'Envíar solicitud de compra', 'Entregar video'] """


#command line interfaces
@app.cli.command()
def test():
    #Implemetnacion unitest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(tests)

#Manage erros . (Error handler)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

#Manage erroes. (Error handler)
@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

#va a ir a la ruta hello
@app.route('/')
def index():
    user_ip = request.remote_addr
    #Creamos una respuesta
    response = make_response(redirect('/hello'))
    """ #Creamos una cookin para obtener la ip desde la cookie del navegador
    response.set_cookie('user_ip', user_ip) """
    session['user_ip'] = user_ip
    return response

# Creamos nuestra primera ruta
# Debemos especificar los parametros con permisos(get y post)
@app.route('/hello', methods=['GET'])
@login_required
#Los decaoradores en python tienen orden (protejemos la ruta dell login)
def hello():
    user_ip = session.get('user_ip')
    #Le estamos diciendo que busque en templates el fichero de hello.html y enviamos la variable
    username = current_user.id

    context = { 
        'user_ip' : user_ip,
        #Si el username se encuentra en firebase traer los todo
        'todos' : get_todos(user_id=username),
        'username' : username 
        }

    #Para no pasar todas las variables la almacenamos en una variable cotext y la pasamos como varios argumentos
    return render_template('hello.html',  **context)

if __name__ == '__main__':
    app.run()


#Macros (Pedazos de codigo reutilizables en el codigo) (ver templates/macros.html)