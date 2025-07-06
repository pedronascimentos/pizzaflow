% rebase('layout.tpl', title='Novo Pedido', user=user)

<div class="columns is-centered">
    <div class="column is-half">
        <h1 class="title"  style="color: black">Criar Novo Pedido</h1>
        <div class="box">
            <form action="/pedidos/novo" method="post">
                <div class="field">
                    <label class="label">Nome do Cliente</label>
                    <div class="control has-icons-left">
                        <input class="input" type="text" name="cliente_nome" placeholder="Ex: João da Silva">
                        <span class="icon is-small is-left"><i class="fas fa-user"></i></span>
                    </div>
                </div>
                <div class="field">
                    <label class="label">Pizzas</label>
                    <div class="control">
                        <div class="select is-multiple is-fullwidth">
                            <select name="itens" multiple size="4">
                                % for item in pizzas:
                                <option value="{{ item.id }}">{{ item.nome }} - R$ {{ "%.2f" % item.preco }}</option>
                                % end
                            </select>
                        </div>
                    </div>
                </div>

                <div class="field">
                    <label class="label">Bebidas</label>
                    <div class="control">
                        <div class="select is-multiple is-fullwidth">
                            <select name="itens" multiple size="4">
                                % for item in bebidas:
                                <option value="{{ item.id }}">{{ item.nome }} - R$ {{ "%.2f" % item.preco }}</option>
                                % end
                            </select>
                        </div>
                    </div>
                    <p class="help">Segure Ctrl (ou Cmd) para selecionar mais de um item.</p>
                </div>
                <div class="field is-grouped">
                    <div class="control">
                        <button class="button is-primary">
                            <span class="icon"><i class="fas fa-check"></i></span>
                            <span>Criar Pedido</span>
                        </button>
                    </div>
                    <div class="control">
                        <a href="/" class="button is-light">Cancelar</a>
                    </div>
                </div>
                </form>
        </div>
    </div>
</div>