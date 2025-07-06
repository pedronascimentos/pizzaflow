import bottle
from config import STATIC_DIR

app = bottle.Bottle()

def load_app(app_instance):
    """
    Carrega os controllers (rotas) da aplicação.
    """
    from controllers import auth_controller, kanban_controller, user_controller 
    @app_instance.route('/static/<filepath:path>')
    def server_static(filepath):
        return bottle.static_file(filepath, root=STATIC_DIR)

# load_app(app)