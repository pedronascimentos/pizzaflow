% rebase('login_layout.tpl', title='Login')

<div class="columns is-centered is-vcentered" style="min-height: 80vh;">
    <div class="column is-4">
        
        <div class="has-text-centered mb-5">
            <a class="is-size-2 has-text-dark" href="/">
                <span class="icon is-large"><i class="fas fa-pizza-slice"></i></span>
                <strong class="is-size-3">PizzaFlow</strong>
            </a>
            <p class="is-size-5 has-text-grey">Gestão de Pedidos</p>
        </div>

        <div class="box">
            <form action="/login" method="post">
                <div class="field">
                    <label class="label">E-mail</label>
                    <div class="control has-icons-left">
                        <input class="input" type="email" name="email" placeholder="seu@email.com" autofocus="">
                        <span class="icon is-small is-left"><i class="fas fa-envelope"></i></span>
                    </div>
                </div>

                <div class="field">
                    <label class="label">Senha</label>
                    <div class="control has-icons-left">
                        <input class="input" type="password" name="senha" placeholder="Sua Senha">
                        <span class="icon is-small is-left"><i class="fas fa-lock"></i></span>
                    </div>
                </div>
                
                % if error:
                <p class="help is-danger mb-3">{{ error }}</p>
                % end

                <div class="field mt-5">
                    <div class="control">
                         <button class="button is-primary is-fullwidth is-medium">Entrar</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>