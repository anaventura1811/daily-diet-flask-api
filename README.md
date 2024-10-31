# Daily Diet

**Daily Diet** é uma API desenvolvida em Python com Flask, que permite gerenciar informações sobre a dieta diária de usuários. O app utiliza Flask para criação de rotas, SQLAlchemy como ORM para interações com o banco de dados MySQL e bcrypt para criptografar senhas.

## Funcionalidades

### Autenticação de Usuário
A API fornece rotas de autenticação que incluem:
- **Criação de usuário**: Cria um novo usuário com username e senha criptografada.
- **Login**: Autentica o usuário usando Flask Login.
- **Logout**: Finaliza a sessão do usuário.
- **Atualização de usuário**: Permite atualizar as informações do usuário.
- **Deleção de usuário**: Exclui o usuário do sistema.

### Gerenciamento de Refeições
A API possui funcionalidades específicas para o gerenciamento de refeições:
1. **Registrar uma refeição**: Permite o registro de uma refeição com as informações:
    - Nome da refeição
    - Descrição
    - Data e hora de atualização
    - Indicação se a refeição está dentro ou não da dieta
2. **Editar uma refeição**: Permite modificar todas as informações acima listadas de uma refeição existente.
3. **Apagar uma refeição**: Exclui uma refeição específica do banco de dados.
4. **Listar todas as refeições de um usuário**: Exibe todas as refeições registradas por um usuário.
5. **Visualizar uma única refeição**: Exibe detalhes de uma refeição específica.

## Tecnologias Utilizadas
- **Flask**: Framework web utilizado para desenvolvimento das rotas da API.
- **Python**: Linguagem de programação utilizada.
- **SQLAlchemy**: ORM utilizado para a manipulação do banco de dados.
- **bcrypt**: Biblioteca utilizada para criptografar senhas de usuários.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/daily-diet-flask-api.git
    cd daily-diet-flask-api
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente (exemplo em `.env.example`).

5. Execute as migrações do banco de dados:
    ```bash
    flask db upgrade
    ```

6. Inicie o servidor:
    ```bash
    flask run
    ```

## Rotas da API

### Autenticação
- `POST /user` - Cadastrar um novo usuário.
- `POST /login` - Login de usuário.
- `POST /logout` - Logout do usuário.
- `PUT /user` - Atualizar informações do usuário.
- `DELETE /user` - Excluir usuário.

### Refeições
- `POST /meals` - Registrar uma nova refeição.
- `PUT /meals/<int:id>` - Editar uma refeição existente.
- `DELETE /meals/<int:id>` - Apagar uma refeição.
- `GET /meals` - Listar todas as refeições de um usuário.
- `GET /meals/<int:id>` - Visualizar uma única refeição.


## Licença
Este projeto está licenciado sob a licença MIT.
