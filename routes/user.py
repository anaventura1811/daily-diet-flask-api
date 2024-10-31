from flask import Blueprint, request, jsonify
from database import db
from models.user import User
from flask_login import login_user, logout_user, login_required, current_user
from bcrypt import hashpw, checkpw, gensalt


user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/user', methods=['POST'])
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


@user_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username and password:
        user = User.query.filter_by(username=username).first()
        check_password = checkpw(
            password=str.encode(password),
            hashed_password=str.encode(user.password))
        if user and check_password:
            login_user(user)
            return jsonify({
                "message": "Autenticação realizada com sucesso!"
            })
    return jsonify({"message": "Credenciais inválidas."}), 400


@user_routes.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"})


@user_routes.route('/user/<int:user_id>', methods=['GET'])
@login_required
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({"username": user.username})
    return jsonify({"message": "Usuário não encontrado"}), 404


@user_routes.route('/user/<int:user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    data = request.json
    password = data.get("password")
    user = User.query.get(user_id)

    if user_id != current_user.id and current_user.role != 'admin':
        return jsonify({"message": "Operação não permitida"}), 403

    if user and password:
        if len(password) >= 8 and len(password) <= 14:
            new_password = hashpw(
                password=str.encode(password),
                salt=gensalt())
            user.password = new_password
            db.session.commit()
            return jsonify(
                {"message": f"Usuário {user.username} atualizado com sucesso"}
            )
        else:
            return jsonify(
                {"message": "A senha deve conter no mínimo 8 caracteres"
                 + " e no máximo 14"}
              )
    else:
        return jsonify({"message": "Usuário não encontrado"}), 404


@user_routes.route('/user/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)
    if current_user.role != 'admin':
        return jsonify({"message": "Operação não permitida"}), 403
    if user_id == current_user.id:
        return jsonify({"message": "Deleção não permitida"}), 403
    if user and user_id != current_user.id:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Usuário {user_id} deletado com sucesso"})
    return jsonify({"message": "Usuário não encontrado"}), 404
