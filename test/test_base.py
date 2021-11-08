from re import S
from flask_testing import TestCase
from flask import current_app, url_for
from werkzeug.wrappers import response

from main import app

class MainTest(TestCase):
    #Implemetnamos el metodo create app 
    def create_app(self):
        #Con esto flask va a saber que esta en el ambiente de testing
        app.config['TESTING'] = True
        #Con esto evitamos que acceda el token  y poder correr el test
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    
    #primer prueba (Probar que la app existe)

    def test_app_exists(self):
        self.assertIsNotNone(current_app)
    
    #Testing de que haya llegado al modo de test

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
    
    #Vamos a realizar un test de que el index nos redirija a hello.html
    
    def test_index_redirect(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))
    
    #Probamos que hello nos regresa un 200 cuando ahcemos un get

    """ def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response) """
    
    #Vamos a probar mediante un post(se valida el redirect)
    def test_hello_post(self):
        response = self.client.post(url_for('hello'))
        self.assertTrue(response.status_code, 405)

    def test_auth_blueprint_exits(self):
        self.assertIn('auth', self.app.blueprints)
    
    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))
        
        self.assert200(response)
    
    def test_auth_login_template(self):
        self.client.get(url_for('auth.login'))
        self.assertTemplateUsed('login.html')

    def test_auth_login_post(self):
        fake_form = {
            'username' : 'fake',
            'password' : 'fake-password'
        }
        
        response = self.client.post(url_for('auth.login'), data=fake_form)
        self.assertRedirects(response, url_for('index'))
        