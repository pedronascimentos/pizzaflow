% rebase('layout.tpl', title='Inbox iFood', user=user)

<h1 class="title" style="color: black">
    <span class="icon"><i class="fas fa-inbox"></i></span>
    Caixa de Entrada iFood
</h1>
<p class="subtitle">
    Pedidos aguardando sua aprovação.
</p>

% if not pedidos:
<div class="notification is-success">
    Tudo certo por aqui! Nenhum pedido pendente.
</div>
% else:
    % for pedido in pedidos:
    <div class="box">
        <div class="level">
            <div class="level-left">
                <div class="level-item">
                    <div>
                        <p class="heading">Cliente</p>
                        <p class="title is-5">{{ pedido['cliente_nome'] }}</p>
                    </div>
                </div>
                 <div class="level-item">
                    <div>
                        <p class="heading">Endereço</p>
                        <p class="subtitle is-6">{{ pedido['endereco'] }}</p>
                    </div>
                </div>
            </div>
            <div class="level-right">
                <div class="level-item">
                     <form action="/ifood/processar" method="post" style="margin-right: 8px;">
                        <input type="hidden" name="mock_id" value="{{ pedido['mock_id'] }}">
                        <input type="hidden" name="action" value="aceitar">
                        <button type="submit" class="button is-success">
                            <span class="icon"><i class="fas fa-check"></i></span>
                            <span>Aceitar</span>
                        </button>
                    </form>
                </div>
                <div class="level-item">
                    <form action="/ifood/processar" method="post">
                        <input type="hidden" name="mock_id" value="{{ pedido['mock_id'] }}">
                        <input type="hidden" name="action" value="recusar">
                        <button type="submit" class="button is-danger">
                             <span class="icon"><i class="fas fa-times"></i></span>
                            <span>Recusar</span>
                        </button>
                    </form>
                </div>
            </div>
        </div>
        <hr style="margin: 1rem 0;">
        <p><strong>Itens do Pedido:</strong></p>
        <ul>
            % for pizza_nome in pedido['pizzas_nomes']:
            <li>{{ pizza_nome }}</li>
            % end
        </ul>
    </div>
    % end
% end