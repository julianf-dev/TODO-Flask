from . import auth
from app.forms import LoginForm
from flask import render_template, session, flash, redirect, url_for


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        # Como es un metodo de String form debemos traer la Data
        username = login_form.username.data
        #Vamos a agregar la sessión(esta ruta va  avalidar cuando se envia unpost y valida la forma)
        session['username'] = username
        # los flash son mensajes para los usuarios
        flash('Nombre de usuario registro con exito')
        
        return redirect(url_for('index'))

    return render_template('login.html', **context)
