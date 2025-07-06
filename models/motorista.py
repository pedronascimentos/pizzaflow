import uuid

class Motorista:
    def __init__(self, nome, telefone, motorista_id=None):
        self.id = motorista_id if motorista_id else str(uuid.uuid4())
        self.nome = nome
        self.telefone = telefone

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'telefone': self.telefone
        }