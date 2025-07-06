import uuid
from datetime import datetime

class Pedido:
    STATUS_CHOICES = ['Pendente', 'Em Preparo', 'No Forno', 'Pronto para Entrega', 'Finalizado']

    def __init__(self, cliente_nome, itens, pedido_id=None, status='Pendente', data_hora=None, 
                 mesa=None, tipo_entrega='Local', motorista=None, funcionario=None):
        self.id = pedido_id if pedido_id else str(uuid.uuid4())
        self.cliente_nome = cliente_nome
        self.itens = itens 
        
        if status not in self.STATUS_CHOICES:
            raise ValueError(f"Status inválido: {status}")
        self.status = status
        self.data_hora = data_hora if data_hora else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.mesa = mesa
        self.tipo_entrega = tipo_entrega
        self.motorista = motorista
        self.funcionario = funcionario 

    def calcular_total(self):
        return sum(item.preco for item in self.itens)

    def to_dict(self):
        return {
            'id': self.id,
            'cliente_nome': self.cliente_nome,
            'itens': [item.to_dict() for item in self.itens],
            'status': self.status,
            'data_hora': self.data_hora,
            'total': self.calcular_total(),
            'mesa': self.mesa,
            'tipo_entrega': self.tipo_entrega,
            'motorista_id': self.motorista.id if self.motorista else None,
            'funcionario_id': self.funcionario.id if self.funcionario else None
        }