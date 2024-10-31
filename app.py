from flask import Flask, request, jsonify
from database import db
from models.user import User
from models.meal import Meal
from flask_login import LoginManager, current_user
from flask_login import login_user, logout_user, login_required
from bcrypt import hashpw, checkpw, gensalt
from dotenv import load_dotenv
import os

load_dotenv()

'''
  Regras da aplicação
    1. Deve ser possível registrar uma refeição feita,
    com as seguintes informações:
      - Nome
      - Descrição
      - Data e hora
      - Está dentro ou não da dieta
    2. Deve ser possível editar uma refeição,
    podendo alterar todos os dados acima
    3. Deve ser possível apagar uma refeição
    4. Deve ser possível listar todas as refeições de um usuário
    5. Deve ser possível visualizar uma única refeição
    6. As informações devem ser salvas em um banco de dados
'''

app = Flask(__name__)
uri = os.getenv('DB_URL')
secret_key = os.getenv('SECRET_KEY')

app.config['SECRET_KEY'] = secret_key
app.config['SQL_ALCHEMY_DATABASE_URI'] = uri

login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'


# View de autenticação/login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    if data:
        username = data.get("username")
        password = data.get("password")
        if (username
                and password
                and len(password) >= 8
                and len(password) <= 14):
            password_hashed = hashpw(
                password=str.encode(password), salt=gensalt())
            user = User(
                username=username,
                password=password_hashed,
                role="user")
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": "Usuário cadastrado com sucesso"})
    return jsonify(
        {"message": "Dados inválidos. Não foi possível cadastrar o usuário"}
        ), 400


if __name__ == '__main__':
    app.run(debug=True)
