from models.user import Admin, Funcionario
from .base_service import BaseService

class UserService(BaseService):
    def __init__(self):
        super().__init__('users.json')

    def get_all_users(self):
        data = self._load_data()
        users = []
        for user_data in data:
            if user_data['tipo'] == 'admin':
                users.append(Admin(user_data['id'], user_data['nome'], user_data['email'], user_data['senha']))
            else:
                users.append(Funcionario(user_data['id'], user_data['nome'], user_data['email'], user_data['senha']))
        return users

    def get_user_by_email(self, email):
        users = self.get_all_users()
        for user in users:
            if user.email == email:
                return user
        return None

    def add_user(self, user):
        users = self._load_data()
        users.append(user.to_dict())
        self._save_data(users)

    def get_user_by_id(self, user_id):
        """ Busca um user pelo seu ID. """
        users = self.get_all_users()
        for user in users:
            if user.id == user_id:
                return user
        return None