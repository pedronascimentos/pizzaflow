import uuid
from abc import ABC, abstractmethod

class User(ABC):
    """
    Classe base abstrata para usuários. ABSTRAÇÃO
    """
    def __init__(self, user_id, nome, email, senha, tipo):
        self._id = user_id if user_id else str(uuid.uuid4())
        self._nome = nome
        self._email = email
        self._senha = senha # Ainda sem hash (Implementar posteriormente!)
        self._tipo = tipo

    # ENCAPSULAMENTO através de properties
    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email
    
    @property
    def tipo(self):
        return self._tipo

    def verificar_senha(self, senha):
        return self._senha == senha

    # POLIMORFISMO
    @abstractmethod
    def obter_permissoes(self):
        """Retorna uma lista de permissões para o usuário."""
        pass

    def to_dict(self):
        """Converte o objeto para um dicionário, útil para salvar em JSON."""
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self._senha, 
            'tipo': self.tipo
        }

class Admin(User):
    """
(HERANÇA)
    """
    def __init__(self, user_id, nome, email, senha):
        super().__init__(user_id, nome, email, senha, 'admin')


    def obter_permissoes(self):
        return ['gerenciar_pedidos', 'gerenciar_funcionarios', 'ver_dashboard']

class Funcionario(User):
    """
    Classe para usuários Funcionários. (HERANÇA)
    """
    def __init__(self, user_id, nome, email, senha):
        super().__init__(user_id, nome, email, senha, 'funcionario')

    # (POLIMORFISMO)
    def obter_permissoes(self):
        return ['gerenciar_pedidos', 'ver_dashboard']