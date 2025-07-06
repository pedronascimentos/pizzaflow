from .base_controller import BaseController
from services.user_service import UserService
from bottle import request, response, redirect, template, Bottle
from app import app
from models.user import Funcionario
from .auth_controller import get_current_user

user_service = UserService()

def admin_only(func):
    def wrapper(*args, **kwargs):
        user = get_current_user()
        if not user or user.tipo != 'admin':
            return redirect('/login')
        return func(*args, **kwargs, user=user)
    return wrapper

@app.route('/funcionarios')
@admin_only
def listar_funcionarios(user):
    # SOMENTE USUÁRIOS, NÃO É PRA MOSTRAR OUTROS ADMINS!!!!!!
    funcionarios = [u for u in user_service.get_all_users() if u.tipo == 'funcionario']
    return template('funcionarios', user=user, funcionarios=funcionarios, error=None)

@app.post('/funcionarios/novo')
@admin_only
def adicionar_funcionario(user):
    nome = request.forms.get('nome')
    email = request.forms.get('email')
    senha = request.forms.get('senha')
    if not nome or not email or not senha:
        funcionarios = [u for u in user_service.get_all_users() if u.tipo == 'funcionario']
        return template('funcionarios', user=user, funcionarios=funcionarios, error="Todos os campos são obrigatórios.")

    novo_func = Funcionario(user_id=None, nome=nome, email=email, senha=senha)
    user_service.add_user(novo_func)
    return redirect('/funcionarios')


    
class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.user_service = UserService()


    def setup_routes(self):
        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)

    def list_users(self):
        users = self.user_service.get_all()
        return self.render('users', users=users)

    def add_user(self):
        if request.method == 'GET':
            return self.render('user_form', user=None, action="/users/add")
        else:
            # POST - salvar usuário
            self.user_service.save()
            self.redirect('/users')

    def edit_user(self, user_id):
        user = self.user_service.get_by_id(user_id)
        if not user:
            return "Usuário não encontrado"

        if request.method == 'GET':
            return self.render('user_form', user=user, action=f"/users/edit/{user_id}")
        else:
            # POST - salvar edição
            self.user_service.edit_user(user)
            self.redirect('/users')


    def delete_user(self, user_id):
        self.user_service.delete_user(user_id)
        self.redirect('/users')


user_routes = Bottle()
user_controller = UserController(user_routes)
