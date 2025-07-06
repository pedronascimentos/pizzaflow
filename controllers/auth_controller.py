from bottle import request, response, redirect, template
from app import app
from services.user_service import UserService
from models.user import Funcionario

user_service = UserService()

@app.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        user = user_service.get_user_by_email(email)
        if user and user.verificar_senha(senha):
            response.set_cookie("user_email", user.email, secret="SECRET_KEY_GOES_HERE", path='/')
            return redirect('/')
        else:
            return template('login', error="E-mail ou senha inválidos.")
    return template('login', error=None)

@app.route('/logout')
def logout():
    response.delete_cookie("user_email", path='/')
    redirect('/login')

def get_current_user():
    user_email = request.get_cookie("user_email", secret="SECRET_KEY_GOES_HERE")
    if user_email:
        return user_service.get_user_by_email(user_email)
    return None