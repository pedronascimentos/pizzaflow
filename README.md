# PizzaFlow - Painel de Gestão para Pizzarias

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Bottle](https://img.shields.io/badge/Bottle-0.12-green?style=for-the-badge&logo=bottle)
![Bulma](https://img.shields.io/badge/Bulma-1.0-purple?style=for-the-badge&logo=bulma)

Projeto final da disciplina de Programação Orientada a Objetos, que consiste em uma aplicação web para gestão do fluxo de produção de uma pizzaria. O sistema utiliza um painel Kanban interativo para visualização e gerenciamento de pedidos em tempo real.

## Funcionalidades Principais

* **Painel Kanban Interativo:** Visualização do fluxo de pedidos com colunas de status e funcionalidade de arrastar e soltar (Drag & Drop).
* **Simulação de Pedidos Externos:** Módulo de "Inbox" que simula a chegada de pedidos da plataforma iFood, com fluxo de aprovação e integração automática ao Kanban (Pedidos do Ifood Mockados).
* **Gestão de Pedidos:** Criação de pedidos locais (com múltiplas pizzas e bebidas) e atribuição de funcionários a cada pedido.
* **Autenticação e Níveis de Permissão:** Sistema de login e distinção entre usuários `Admin` (com acesso a painéis de gerenciamento) e `Funcionario`.
* **Modelagem OO:** O projeto aplica os quatro pilares da Programação Orientada a Objetos (Abstração, Encapsulamento, Herança e Polimorfismo) para modelar as entidades do sistema.

## Diferenciais em Relação ao Template Base

* **Interface Dinâmica:** Uso de JavaScript para criar uma experiência de usuário rica com Drag & Drop, modais e notificações assíncronas, além de um simples CRUD.
* **Arquitetura OO:** Implementação de Classes Base Abstratas (`ItemPedido`, `User`) para garantir um design extensível e demonstrar polimorfismo.
* **Múltiplas Relações entre Modelos:** Demonstração de composição (Pedido contém Itens) e associação (Pedido é atribuído a um Funcionário).

## Diagrama de Classes (UML)

O diagrama abaixo ilustra a arquitetura do sistema e as relações entre as principais classes.

```mermaid
classDiagram
    class User {
        <<Abstract>>
        -String _id
        -String _nome
        -String _email
        +id: property
        +nome: property
        +verificar_senha(senha)
    }
    class Admin {
        +obter_permissoes()
    }
    class Funcionario {
        +obter_permissoes()
    }
    class ItemPedido {
        <<Abstract>>
        -String _id
        -String _nome
        -float _preco
        +id: property
        +nome: property
        +preco: property
        +get_tipo()*
    }
    class Pizza {
        +get_tipo()
    }
    class Bebida {
        +get_tipo()
    }
    class Pedido {
        -String id
        -String cliente_nome
        -String status
        -List~ItemPedido~ itens
        -Funcionario funcionario
        -Motorista motorista
        +calcular_total()
    }
    class Motorista {
        -String id
        -String nome
    }

    User <|-- Admin
    User <|-- Funcionario
    ItemPedido <|-- Pizza
    ItemPedido <|-- Bebida

    Pedido "1" *-- "1..*" ItemPedido : contém
    Pedido "1" o-- "0..1" Funcionario : atribuído a
    Pedido "1" o-- "0..1" Motorista : entregue por
````


## Estrutura do Projeto

```
pizzaflow/
├── app.py              # Ponto de entrada e configuração do Bottle
├── main.py             # Inicialização da aplicação
├── requirements.txt    # Dependências do projeto
├── README.md           # Este arquivo
├── controllers/        # Camada de controle (rotas e lógica de requisição)
│   ├── auth_controller.py
│   ├── kanban_controller.py
│   └── user_controller.py
├── models/             # Camada de modelo (entidades e regras de negócio)
│   ├── item_pedido.py
│   ├── motorista.py
│   ├── pedido.py
│   └── user.py
├── services/           # Camada de serviço (lógica de persistência)
│   ├── base_service.py
│   ├── ifood_mock_service.py
│   ├── motorista_service.py
│   ├── pedido_service.py
│   └── user_service.py
├── views/              # Camada de visão (templates HTML)
│   ├── *.tpl
├── static/             # Arquivos estáticos
│   ├── css/style.css
│   ├── js/main.js
│   └── img/ifood_logo.svg
└── data/               # Arquivos de dados JSON
    ├── *.json
```

## Instalação e Execução

**1. Pré-requisitos:**

  * Python 3.8 ou superior

**2. Clone o repositório:**

```bash
git clone https://github.com/pedronascimentos/epf-pizzaflow
cd SEU_REPOSITORIO
```

**3. Crie e ative um ambiente virtual:**

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**4. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**5. Execute a aplicação:**

```bash
python main.py
```

**6. Acesse o sistema:**

  * Abra seu navegador e acesse: `http://localhost:8080`
  * **Login Admin:** `admin@pizzaflow.com` / `admin`
  * **Login Funcionário:** `maria@pizzaflow.com` / `123`

-----

*Este projeto foi desenvolvido por [Pedro Nascimentos](mailto:nascimento.monteiro@aluno.unb.br) e Luccas Rodrigues como parte da avaliação da disciplina de Programação Orientada a Objetos.*
