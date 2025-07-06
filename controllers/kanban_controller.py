import json
from bottle import template, redirect, request, response
from app import app
import random
from services.ifood_mock_service import IfoodMockService
from services.motorista_service import MotoristaService
from services.pedido_service import PedidoService, ITENS_DB
from models.pedido import Pedido
from .auth_controller import get_current_user
from services.user_service import UserService 

pedido_service = PedidoService()
ifood_service = IfoodMockService()
motorista_service = MotoristaService()
user_service = UserService() # Instancie

@app.get('/api/ifood/liberar-proximo')
def liberar_proximo_pedido_ifood():
    user = get_current_user()
    if not user:
        response.status = 401
        return {'status': 'error', 'message': 'Não autenticado'}

    todos_pedidos_mock = ifood_service._load_data()
    
    proximo_pedido = None
    for p in todos_pedidos_mock:
        if p.get('status_aprovacao') == 'nao_liberado':
            proximo_pedido = p
            break
            
    if not proximo_pedido:
        print("Fim da lista de mocks. Reiniciando o ciclo para a demo.")
        for p in todos_pedidos_mock:
            p['status_aprovacao'] = 'nao_liberado'
        
        proximo_pedido = todos_pedidos_mock[0]
    
    
    # Muda o status para 'aguardando' para que ele apareça na Inbox
    proximo_pedido['status_aprovacao'] = 'aguardando'
    ifood_service._save_data(todos_pedidos_mock)
    
    response.content_type = 'application/json'
    return json.dumps(proximo_pedido)

@app.route('/ifood')
def ifood_inbox():
    user = get_current_user()
    if not user:
        return redirect('/login')

    pedidos_pendentes = ifood_service.get_pedidos_para_aprovacao()
    
    return template('ifood_inbox', 
                    user=user,
                    pedidos=pedidos_pendentes,
                    num_ifood=len(pedidos_pendentes))


@app.post('/ifood/processar')
def processar_pedido_ifood():
    user = get_current_user()
    if not user:
        return redirect('/login')

    mock_id = request.forms.get('mock_id')
    action = request.forms.get('action')

    if action == 'aceitar':
        mock_pedido = ifood_service.get_pedido_by_id(mock_id)
        if not mock_pedido:
            return "Erro: Pedido mock não encontrado."


        itens_obj = []
        nomes_dos_itens = mock_pedido.get('pizzas_nomes', []) 
        
        # Procura cada item pelo nome no nosso banco de dados mock
        for nome_item in nomes_dos_itens:
            for item_no_db in ITENS_DB.values():
                if item_no_db.nome == nome_item:
                    itens_obj.append(item_no_db)
        
        # Associa um motorista aleatório
        motoristas = motorista_service.get_all()
        motorista_aleatorio = random.choice(motoristas) if motoristas else None


        novo_pedido = Pedido(
            cliente_nome=mock_pedido['cliente_nome'].replace(' (iFood)', ''),
            itens=itens_obj,
            tipo_entrega='iFood',
            motorista=motorista_aleatorio
        )
        
        pedido_service.add_pedido(novo_pedido)
        ifood_service.atualizar_status_aprovacao(mock_id, 'aceito')
        return redirect('/')

    elif action == 'recusar':
        ifood_service.atualizar_status_aprovacao(mock_id, 'recusado')
        return redirect('/ifood')

    return "Ação inválida."

@app.route('/')
def kanban_board():
    user = get_current_user()
    if not user:
        return redirect('/login')

    todos_pedidos = pedido_service.get_all_pedidos()
    funcionarios = [u for u in user_service.get_all_users() if u.tipo == 'funcionario']
    pedidos_por_status = {status: [] for status in Pedido.STATUS_CHOICES}
    for pedido in todos_pedidos:
        pedidos_por_status[pedido.status].append(pedido)

    num_pendentes_ifood = len(ifood_service.get_pedidos_para_aprovacao())

    return template('kanban', 
                    user=user, 
                    pedidos=pedidos_por_status,
                    status_list=Pedido.STATUS_CHOICES,
                    num_ifood=num_pendentes_ifood,
                    funcionarios=funcionarios 
                   )
                   
@app.route('/pedidos/novo', method=['GET', 'POST'])
def novo_pedido():
    user = get_current_user()
    if not user:
        return redirect('/login')

    if request.method == 'POST':
        cliente = request.forms.get('cliente_nome')
        item_ids = request.forms.getall('itens')
        

        if not cliente or not item_ids:
            pizzas = [item for item in ITENS_DB.values() if item.get_tipo() == 'pizza']
            bebidas = [item for item in ITENS_DB.values() if item.get_tipo() == 'bebida']
            return template('pedido_form', 
                            error="Cliente e pelo menos um item são obrigatórios.", 
                            pizzas=pizzas, 
                            bebidas=bebidas, 
                            user=user)

        itens_obj = [ITENS_DB[item_id] for item_id in item_ids if item_id in ITENS_DB]
        
        novo_pedido_obj = Pedido(cliente_nome=cliente, itens=itens_obj)
        pedido_service.add_pedido(novo_pedido_obj)
        return redirect('/')

    # Separa os itens para mostrar nos selects do formulário
    pizzas_disponiveis = [item for item in ITENS_DB.values() if item.get_tipo() == 'pizza']
    bebidas_disponiveis = [item for item in ITENS_DB.values() if item.get_tipo() == 'bebida']
    
    return template('pedido_form', 
                    error=None, 
                    pizzas=pizzas_disponiveis, 
                    bebidas=bebidas_disponiveis, 
                    user=user)

@app.post('/pedidos/atribuir-funcionario')
def atribuir_funcionario():
    user = get_current_user()
    if not user:
        return redirect('/login')

    pedido_id = request.forms.get('pedido_id')
    funcionario_id = request.forms.get('funcionario_id')

    if pedido_id and funcionario_id:
        pedido_service.assign_employee_to_order(pedido_id, funcionario_id)
    
    return redirect('/')

@app.post('/pedidos/mover')
def mover_pedido():
    user = get_current_user()
    if not user:
        response.status = 401 # Unauthorized
        return json.dumps({'status': 'error', 'message': 'Não autorizado'})
    
    pedido_id = request.forms.get('pedido_id')
    novo_status = request.forms.get('novo_status')
    
    try:
        if pedido_id and novo_status:
            pedido_service.update_status(pedido_id, novo_status)
            response.content_type = 'application/json'
            return json.dumps({'status': 'success'})
    except Exception as e:
        response.status = 500 # Internal Server Error
        return json.dumps({'status': 'error', 'message': str(e)})

    response.status = 400 # Bad Request
    return json.dumps({'status': 'error', 'message': 'Dados inválidos'})