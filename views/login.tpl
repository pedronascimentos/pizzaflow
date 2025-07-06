% rebase('layout.tpl', title='Login', user=None)

<section class="hero is-fullheight-with-navbar">
    <div class="hero-body">
        <div class="container has-text-centered">
            <div class="column is-4 is-offset-4">
                <h3 class="title has-text-black">Login - PizzaFlow</h3>
                <hr class="login-hr">
                <p class="subtitle has-text-black">Faça o login para continuar.</p>
                <div class="box">
                    <form action="/login" method="post">
                        <div class="field">
                            <div class="control">
                                <input class="input is-large" type="email" name="email" placeholder="Seu E-mail" autofocus="">
                            </div>
                        </div>
                        <div class="field">
                            <div class="control">
                                <input class="input is-large" type="password" name="senha" placeholder="Sua Senha">
                            </div>
                        </div>
                        <button class="button is-block is-primary is-large is-fullwidth">Entrar <i class="fa fa-sign-in" aria-hidden="true"></i></button>
                    </form>
                    % if error:
                        <p class="has-text-danger mt-4">{{ error }}</p>
                    % end
                </div>
            </div>
        </div>
    </div>
</section>