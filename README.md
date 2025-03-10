# Desafio Fullstack: Os Anéis de Poder

## Tecnologias Utilizadas

- **Django**: Framework web para o backend.
- **Django REST Framework**: Biblioteca para criar APIs RESTful.
- **PostgreSQL**: Banco de dados relacional.
- **Bootstrap**: Framework CSS para estilização.
- **JavaScript (Fetch API)**: Para consumir a API e manipular o DOM.
- **HTML**: Estrutura da página web.

## Configuração do Ambiente

### Pré-requisitos

- Python 3.8+
- PostgreSQL

### Passos para Configuração

1. **Clone o repositório:**

    ```sh
    git clone https://github.com/BrunoHenrique00/django-rings.git
    cd django-rings
    ```

2. **Configure o banco de dados PostgreSQL:**

    Crie um banco de dados no PostgreSQL e atualize o arquivo `.env` com as credenciais do banco de dados:

    ```env
    DATABASE_NAME=ring
    DATABASE_USER=postgres
    DATABASE_PASSWORD=1234
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    ```

3. **Aplique as migrações do banco de dados:**

    ```sh
    python manage.py migrate
    ```

4. **Crie um superusuário para acessar o admin do Django:**

   ```sh
    python manage.py createsuperuser
    ```

5. **Inicie o servidor de desenvolvimento:**

    ```sh
    python manage.py runserver
    ```

6. **Acesse a aplicação:**

    Abra o navegador e vá para `http://localhost:8000` para ver a aplicação em execução.

## Como Usar

- **Criar Anel**: Preencha o formulário e clique em "Criar Anel".
- **Atualizar Anel**: Clique no botão "Update" ao lado do anel que deseja atualizar, edite as informações no modal e clique em "Atualizar Anel".
- **Deletar Anel**: Clique no botão "Delete" ao lado do anel que deseja deletar.

## Estrutura do Projeto

- **ring/**: Aplicação Django que contém os modelos, views, serializers e urls.
- **templates/**: Arquivos HTML para a interface do usuário.
- **api/**: Configurações do projeto Django.
