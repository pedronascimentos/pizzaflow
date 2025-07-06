import json
import os
from config import DATA_DIR

class BaseService:
    def __init__(self, filename):
        self._filepath = os.path.join(DATA_DIR, filename)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self._filepath):
            with open(self._filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_data(self):
        try:
            with open(self._filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError):
            return []

    def _save_data(self, data):
        with open(self._filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)