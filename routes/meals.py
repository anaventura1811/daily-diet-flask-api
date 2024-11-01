from flask import Blueprint, request, jsonify
from database import db
from flask_login import login_required, current_user
from models.meal import Meal
from datetime import datetime

meal_routes = Blueprint('meal_routes', __name__)


@meal_routes.route('/meals', methods=['POST'])
@login_required
def create_meal():
    data = request.json

    if data:
        title = data.get("title")
        description = data.get("description")
        in_diet = data.get("in_diet") > 0
        owner_id = current_user.id
        meal = Meal(
            title=title,
            description=description,
            in_diet=in_diet,
            owner_id=owner_id)

        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Refeição registrada com sucesso"})
    return jsonify(
        {"message": "Dados inválidos. Não foi possível cadastrar a refeição"}
        ), 400


@meal_routes.route('/meals', methods=['GET'])
@login_required
def get_meals():
    meals_query = Meal.query.filter_by(owner_id=current_user.id).all()
    if meals_query:
        meals = [meal.to_dict() for meal in meals_query]
        return jsonify({
            "meals": meals,
            "total_results": len(meals),
        })
    else:
        return jsonify({
            "message": "Não há refeições cadastradas para este usuário"
        }), 404


@meal_routes.route('/meals/<int:meal_id>', methods=['GET'])
@login_required
def get_meal(meal_id):
    meal_query = Meal.query.filter_by(
        owner_id=current_user.id, id=meal_id).first()
    if meal_query:
        return jsonify(meal_query.to_dict())
    return jsonify({"message": "Refeição não encontrada"}), 404


@meal_routes.route('/meals/<int:meal_id>', methods=['PUT'])
@login_required
def update_meal(meal_id):
    meal_query = Meal.query.filter_by(
        owner_id=current_user.id, id=meal_id).first()
    data = request.json
    title = data.get("title")
    description = data.get("description")
    in_diet = data.get("in_diet", meal_query.in_diet)
    if meal_query:
        meal_query.in_diet = in_diet
        if title:
            meal_query.title = title
        if description:
            meal_query.description = description
        if in_diet or title or description:
            meal_query.last_updated = datetime.now()
        db.session.commit()
        return jsonify(
            {"message": f"Refeição {meal_query.title} atualizada com sucesso"})
    else:
        return jsonify({
            "message": "Refeição não encontrada"
        }), 404


@meal_routes.route('/meals/<int:meal_id>', methods=['DELETE'])
@login_required
def delete_meal(meal_id):
    meal = Meal.query.filter_by(
        owner_id=current_user.id, id=meal_id).first()
    if meal.id:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": f"Refeição {meal_id} excluída com sucesso"})
    return jsonify({"message": "Refeição não encontrada"}), 404
