from .base_service import BaseService
from models.motorista import Motorista

class MotoristaService(BaseService):
    def __init__(self):
        super().__init__('motoristas.json')

    def get_all(self):
        data = self._load_data()
        return [Motorista(**m_data) for m_data in data]

    def get_by_id(self, motorista_id):
        for motorista in self.get_all():
            if motorista.id == motorista_id:
                return motorista
        return None