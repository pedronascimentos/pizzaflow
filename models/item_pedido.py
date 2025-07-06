# models/item_pedido.py
from abc import ABC, abstractmethod

class ItemPedido(ABC):
    def __init__(self, item_id, nome, preco):
        self._id = item_id
        self._nome = nome
        self._preco = float(preco)

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco

    @abstractmethod
    def get_tipo(self):
        """ Retorna o tipo do item (ex: 'pizza', 'bebida'). """
        pass

    def to_dict(self):
        """ Converte o item para um dicionário para salvar em JSON. """
        return {
            'id': self.id,
            'nome': self.nome,
            'preco': self.preco,
            'tipo': self.get_tipo()
        }

class Pizza(ItemPedido):
    """ Classe Pizza que herda de ItemPedido. """
    def get_tipo(self):
        return 'pizza'

class Bebida(ItemPedido):
    """ Classe Bebida que herda de ItemPedido. """
    def get_tipo(self):
        return 'bebida'