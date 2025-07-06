<!DOCTYPE html>
<html lang="pt-br" class="has-navbar-fixed-top">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title or 'PizzaFlow' }}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0.0/css/bulma.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <nav class="navbar is-fixed-top is-dark" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <a class="navbar-item" href="/">
                <i class="fas fa-pizza-slice fa-lg mr-2"></i>
                <strong class="is-size-4">PizzaFlow</strong>
            </a>
        </div>
        <div class="navbar-menu">
            <div class="navbar-start">
                <a class="navbar-item" href="/">
                    <span class="icon"><i class="fas fa-columns"></i></span>
                    <span>Kanban de Pedidos</span>
                </a>
                <a class="navbar-item" href="/pedidos/novo">
                    <span class="icon"><i class="fas fa-plus-circle"></i></span>
                    <span>Novo Pedido</span>
                </a>
                <a class="navbar-item" href="/ifood">
                    <span class="icon"><i class="fas fa-receipt"></i></span>
                    <span>Inbox iFood</span>
                    <span id="ifood-badge" class="tag is-danger is-rounded ml-2 {{ '' if 'num_ifood' in globals() and num_ifood > 0 else 'is-hidden' }}">
                        {{ num_ifood if 'num_ifood' in globals() else 0 }}
                    </span>
                </a>
                % if user and user.tipo == 'admin':
                <a class="navbar-item" href="/funcionarios">
                    <span class="icon"><i class="fas fa-users-cog"></i></span>
                    <span>Funcionários</span>
                </a>
                % end
            </div>
            <div class="navbar-end">
                % if user:
                <div class="navbar-item">
                    <div class="buttons">
                        <span class="button is-primary is-light">
                            <span class="icon"><i class="fas fa-user"></i></span>
                            <span>Olá, {{ user.nome }} ({{ user.tipo }})</span>
                        </span>
                        <a href="/logout" class="button is-danger">
                            <span class="icon"><i class="fas fa-sign-out-alt"></i></span>
                            <span>Sair</span>
                        </a>
                    </div>
                </div>
                % end
            </div>
        </div>
    </nav>

    <main class="section">
        <div class="container is-fluid">
            {{!base}}
        </div>
    </main>

    <script src="https://cdn.jsdelivr.net/npm/sortablejs@latest/Sortable.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/toastify-js"></script>
    <script src="/static/js/main.js?v=1.2"></script>
</body>
</html>
</body>
</html>