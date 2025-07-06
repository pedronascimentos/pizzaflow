import json
from models.pedido import Pedido
from models.pizza import Pizza
from .base_service import BaseService
from .motorista_service import MotoristaService 
from models.item_pedido import Pizza, Bebida
from .motorista_service import MotoristaService
from .user_service import UserService
ITENS_DB = {
    "p1": Pizza(item_id="p1", nome="Mussarela", preco=40.0),
    "p2": Pizza(item_id="p2", nome="Calabresa", preco=45.0),
    "p3": Pizza(item_id="p3", nome="Frango com Catupiry", preco=50.0),
    
    "b1": Bebida(item_id="b1", nome="Coca-Cola 2L", preco=12.0),
    "b2": Bebida(item_id="b2", nome="Guaraná 2L", preco=10.0),
    "b3": Bebida(item_id="b3", nome="Água com Gás", preco=5.0),
}
class PedidoService(BaseService):
    def __init__(self):
        super().__init__('pedidos.json')
        self.motorista_service = MotoristaService()
        self.user_service = UserService()

    def get_all_pedidos(self):
        data = self._load_data()
        pedidos = []
        for p_data in data:
            itens_obj = []
            for item_data in p_data.get('itens', []):
                item_id = item_data.get('id')
                if item_id in ITENS_DB:
                    itens_obj.append(ITENS_DB[item_id])

            motorista_obj = None
            motorista_id = p_data.get('motorista_id')
            if motorista_id:
                motorista_obj = self.motorista_service.get_by_id(motorista_id)

            funcionario_obj = None
            funcionario_id = p_data.get('funcionario_id')
            if funcionario_id:
                funcionario_obj = self.user_service.get_user_by_id(funcionario_id)


            pedido = Pedido(
                pedido_id=p_data.get('id'),
                cliente_nome=p_data.get('cliente_nome'),
                itens=itens_obj, 
                status=p_data.get('status'),
                data_hora=p_data.get('data_hora'),
                mesa=p_data.get('mesa'),
                motorista=motorista_obj,
                tipo_entrega=p_data.get('tipo_entrega', 'Local'),
                funcionario=funcionario_obj 
            )
            pedidos.append(pedido)
            
        return sorted(pedidos, key=lambda p: p.data_hora, reverse=True)

    def add_pedido(self, pedido):
        pedidos = self._load_data()
        pedidos.append(pedido.to_dict())
        self._save_data(pedidos)

    def assign_employee_to_order(self, pedido_id, funcionario_id):
        """ Atribui um funcionário a um pedido específico. """
        pedidos_data = self._load_data()
        for p_data in pedidos_data:
            if p_data.get('id') == pedido_id:
                p_data['funcionario_id'] = funcionario_id
                break
        self._save_data(pedidos_data)
        
    def update_status(self, pedido_id, new_status):
        pedidos_data = self._load_data()
        for p_data in pedidos_data:
            if p_data.get('id') == pedido_id:
                p_data['status'] = new_status
                break
        self._save_data(pedidos_data)