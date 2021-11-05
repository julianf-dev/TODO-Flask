
from flask import render_template, session, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash

from . import auth
from app.forms import LoginForm
from app.firestore_service import get_user,user_put
from app.models import UserData, UserModel


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        #Vamos a validar si el usuario existe en la BD
        # Como es un metodo de String form debemos traer la Data
        username = login_form.username.data
        password = login_form.password.data

        #Aqui vamosa buscar ese user.document
        user_doc = get_user(username)

        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()['password']
            if password == password_from_db:
                user_data = UserData(username, password)
                user = UserModel(user_data)

                login_user(user)
                flash('Bievenido de nuevo')
                return redirect(url_for('hello'))
            else:
                flash('Los datos no coinciden')
        else:
            flash('El usuario no existe ')
        # los flash son mensajes para los usuarios        
        return redirect(url_for('index'))

    return render_template('login.html', **context)

#Function to register users

@auth.route('signup', methods = ['GET','POST'])
def signup():
    signup_form = LoginForm()
    context = {
        'signup_form' : signup_form
    }

    #Obetenermos el form atraves de POST para validarla

    if signup_form.validate_on_submit():
        #Validamos si el usuario existe
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)
            #Creamos una nueva instancia de UserData
            user_data = UserData(username, password_hash)

            #Llamamaos el metodo para registrar en la base de datos
            user_put(user_data)

            user = UserModel(user_data)

            login_user(user)

            flash('Bievenido')

            return redirect(url_for('hello'))
        else:
            flash('El usuario ya existe')

    return render_template('signup.html', **context)


#Function to logout sessión

@auth.route('/logout')
@login_required
#Creamos la función para el logout
def logout():
    logout_user()
    flash('Regresa Pronto')
    return redirect(url_for('auth.login'))