% rebase('layout.tpl', title='Gerenciar Funcionários', user=user)

<h1 class="title"  style="color: black">Gerenciar Funcionários</h1>
<div class="columns">
    <div class="column is-two-thirds">
        <div class="box">
            <h2 class="subtitle">Funcionários Cadastrados</h2>
            <table class="table is-fullwidth is-striped is-hoverable">
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>Email</th>
                        <th>Ações</th>
                    </tr>
                </thead>
                <tbody>
                    % for func in funcionarios:
                    <tr>
                        <td>{{ func.nome }}</td>
                        <td>{{ func.email }}</td>
                        <td>
                            <button class="button is-danger is-small">
                                <span class="icon"><i class="fas fa-trash"></i></span>
                                <span>Excluir</span>
                            </button>
                        </td>
                    </tr>
                    % end
                </tbody>
            </table>
        </div>
    </div>
    <div class="column is-one-third">
        <div class="box">
            <h2 class="subtitle">Adicionar Novo Funcionário</h2>
            <form action="/funcionarios/novo" method="post">
                <div class="field">
                    <label class="label">Nome</label>
                    <div class="control">
                        <input class="input" type="text" name="nome" required>
                    </div>
                </div>
                 <div class="field">
                    <label class="label">Email</label>
                    <div class="control">
                        <input class="input" type="email" name="email" required>
                    </div>
                </div>
                 <div class="field">
                    <label class="label">Senha</label>
                    <div class="control">
                        <input class="input" type="password" name="senha" required>
                    </div>
                </div>
                % if error:
                <p class="notification is-danger is-light">{{ error }}</p>
                % end
                <div class="field">
                    <div class="control">
                        <button class="button is-primary is-fullwidth">
                            <span class="icon"><i class="fas fa-user-plus"></i></span>
                            <span>Adicionar</span>
                        </button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>