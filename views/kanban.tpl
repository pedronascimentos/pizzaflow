% rebase('layout.tpl', title='Kanban de Pedidos', user=user, num_ifood=num_ifood)

<div id="assign-employee-modal" class="modal">
    <div class="modal-background"></div>
    <div class="modal-card">
        <header class="modal-card-head">
            <p class="modal-card-title">Atribuir Funcionário</p>
            <button class="delete" aria-label="close"></button>
        </header>
        <section class="modal-card-body">
            <form id="assign-form" action="/pedidos/atribuir-funcionario" method="post">
                <input type="hidden" name="pedido_id" id="modal-pedido-id">
                <div class="field">
                    <label class="label">Selecione o Funcionário</label>
                    <div class="control">
                        <div class="select is-fullwidth">
                            <select name="funcionario_id">
                                % for func in funcionarios:
                                <option value="{{ func.id }}">{{ func.nome }}</option>
                                % end
                            </select>
                        </div>
                    </div>
                </div>
            </form>
        </section>
        <footer class="modal-card-foot">
            <button class="button is-success" form="assign-form" type="submit">Salvar</button>
            <button class="button" id="cancel-assign">Cancelar</button>
        </footer>
    </div>
</div>

<div class="kanban-board">
    % for status in status_list:
    <div class="kanban-column">
        <h2 class="title is-4 has-text-centered mb-4">{{ status }}</h2>
        <div class="kanban-cards" data-status="{{ status }}">
            % for pedido in pedidos[status]:
            <div class="card mb-4" data-id="{{ pedido.id }}">
                <header class="card-header">
                    <p class="card-header-title is-size-6">
                        {{ pedido.cliente_nome }}
                    </p>
                    <button class="card-header-icon assign-employee-btn" aria-label="Atribuir funcionário">
                        <span class="icon">
                            <i class="fas fa-plus"></i>
                        </span>
                    </button>
                </header>
                <div class="card-content">
                    <div class="content">
                        <ul>
                            % for item in pedido.itens:
                                <li>
                                    % if item.get_tipo() == 'pizza':
                                    <span class="icon is-small"><i class="fas fa-pizza-slice"></i></span>
                                    % else:
                                    <span class="icon is-small"><i class="fas fa-wine-bottle"></i></span>
                                    % end
                                    <span>{{ item.nome }}</span>
                                </li>
                            % end
                        </ul>
                        <p><strong>Total: R$ {{ "%.2f" % pedido.calcular_total() }}</strong></p>
                        
                        <div class="tags are-small">
                            % if pedido.tipo_entrega == 'iFood':
                            <span class="tag is-danger">
                                <img src="/static/img/ifood_logo.svg" class="ifood-logo" alt="iFood Logo">
                                <span>iFood</span>
                            </span>
                            % else:
                            <span class="tag is-info">
                                <span class="icon"><i class="fas fa-store"></i></span>
                                <span>Local</span>
                            </span>
                            % end
                            
                            % if pedido.mesa:
                            <span class="tag is-dark">Mesa: {{ pedido.mesa }}</span>
                            % end
                            
                            % if pedido.motorista:
                            <span class="tag is-link is-light">{{ pedido.motorista.nome }}</span>
                            % end

                            % if pedido.funcionario:
                                <span class="tag is-primary is-light">
                                    <span class="icon is-small"><i class="fas fa-user-check"></i></span>
                                    <span>{{ pedido.funcionario.nome }}</span>
                                </span>
                            % end
                        </div>
                    </div>
                </div>
                <footer class="card-footer">
                    <span class="card-footer-item has-text-grey-light is-size-7">
                        Arraste para mover
                    </span>
                </footer>
            </div>
            % end
        </div>
    </div>
    % end
</div>