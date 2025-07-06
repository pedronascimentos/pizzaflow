import json
from .base_service import BaseService

class IfoodMockService(BaseService):
    def __init__(self):
        super().__init__('ifood_pedidos_mock.json')

    def get_pedidos_para_aprovacao(self):
        """Retorna apenas os pedidos que estão aguardando aprovação."""
        todos_pedidos = self._load_data()
        return [p for p in todos_pedidos if p.get('status_aprovacao') == 'aguardando']
    
    def get_pedido_by_id(self, mock_id):
        """Retorna um pedido específico do mock."""
        todos_pedidos = self._load_data()
        for pedido in todos_pedidos:
            if pedido.get('mock_id') == mock_id:
                return pedido
        return None

    def atualizar_status_aprovacao(self, mock_id, novo_status):
        """Atualiza o status de um pedido no arquivo mock."""
        todos_pedidos = self._load_data()
        for pedido in todos_pedidos:
            if pedido.get('mock_id') == mock_id:
                pedido['status_aprovacao'] = novo_status
                break
        self._save_data(todos_pedidos)