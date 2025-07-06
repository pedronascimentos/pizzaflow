class Pizza:
    def __init__(self, nome, ingredientes, preco, pizza_id=None):
        self.id = pizza_id
        self.nome = nome
        self.ingredientes = ingredientes
        self.preco = float(preco)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'ingredientes': self.ingredientes,
            'preco': self.preco
        }