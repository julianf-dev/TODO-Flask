from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

#login
class LoginForm(FlaskForm):
    #We will create fields
    #Validor de datos de la libreria (data required)
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    #la libreria lo va ecryptar (Existen muchos tipos devalidadores(Longitud etc))
    password = PasswordField('Passowrd', validators=[DataRequired()])
    #una acción para envíar
    submit = SubmitField('Envíar')


class TodoForm(FlaskForm):
    #Plantilla de los FlaskForm
    description = StringField('Descripción',validators=[DataRequired()])
    submit = SubmitField('Crear')

#Aqui hacemos el botón para borrar y esta forma la enviaremos a los diferentes parametros
class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Borrar')

class UpdateTodoForm(FlaskForm):
    submit  = SubmitField('Actualizar')