# variable de ambiente: set FLASK_APP=main.py
import unittest
from flask import request, render_template, make_response, redirect, session
from flask.helpers import flash, url_for
from flask_login import login_required, current_user

from app import create_app
from app.firestore_service import get_todos, put_todo, delete_todo, update_todo
from app.forms import DeleteTodoForm, TodoForm, UpdateTodoForm
# Instanciamos nuestra app
app = create_app()
""" todos =  ['Comprar café', 'Envíar solicitud de compra', 'Entregar video'] """


# command line interfaces
@app.cli.command()
def test():
    # Implemetnacion unitest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(tests)

# Manage erros . (Error handler)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

# Manage erroes. (Error handler)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

# va a ir a la ruta hello


@app.route('/')
def index():
    user_ip = request.remote_addr
    # Creamos una respuesta
    response = make_response(redirect('/hello'))
    """ #Creamos una cookin para obtener la ip desde la cookie del navegador
    response.set_cookie('user_ip', user_ip) """
    session['user_ip'] = user_ip
    return response

# Creamos nuestra primera ruta
# Debemos especificar los parametros con permisos(get y post)


@app.route('/hello', methods=['GET', 'POST'])
@login_required
# Los decaoradores en python tienen orden (protejemos la ruta dell login)
def hello():
    user_ip = session.get('user_ip')
    # Le esta48mos diciendo que busque en templates el fichero de hello.html y enviamos la variable
    username = current_user.id

    # Creamos una nueva instancia de los formularios de TodoForm
    todo_form = TodoForm()

    # Agregamos la forma del delete
    delete_form = DeleteTodoForm()

    # Agregamos el form del upadte
    update_form = UpdateTodoForm()

    context = {
        'user_ip': user_ip,
        # Si el username se encuentra en firebase traer los todo
        'todos': get_todos(user_id=username),
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'update_form' : update_form,
    }

    # Vamos a recibir lo del todo_form
    if todo_form.validate_on_submit():
        # No se puede pponer un argumento sin nombre después de otro que si tiene nombre
        # Lo que hacemos es enviar el id de usuario y la data o información del todo form del usuario
        put_todo(userd_id=username, description=todo_form.description.data)

        flash('La tarea se creo correctamente')

        # redirijimos el usuario de nuevo a hello

        return redirect(url_for('hello'))

    # Para no pasar todas las variables la almacenamos en una variable cotext y la pasamos como varios argumentos
    return render_template('hello.html', **context)


# La ruta para validar las tareas (Rutas dinamicas de flask)
@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)

    return redirect(url_for('hello'))

@app.route('/todos/update/<todo_id>,<int:done>', methods=['POST'])
def update(todo_id, done):
    #Este paremtro se va forzar que sea un número
    user_id = current_user.id 
    #Estamos obteniendo el switch de la respuesta
    update_todo(user_id = user_id,todo_id=todo_id, done= done)
# Macros (Pedazos de codigo reutilizables en el codigo) (ver templates/macros.html)
    return redirect(url_for('hello'))
