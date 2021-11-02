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