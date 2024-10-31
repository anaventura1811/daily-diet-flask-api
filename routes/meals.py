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
        meals = []
        for meal in meals_query:
            formatted_meal = {
              "id": meal.id,
              "title": meal.title,
              "description": meal.description,
              "created_at": meal.created_at,
              "last_updated": meal.last_updated,
              "in_diet": meal.in_diet,
              "owner_id": meal.owner_id,
            }
            meals.append(formatted_meal)
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
        meal = {
            "title": meal_query.title,
            "id": meal_query.id,
            "description": meal_query.description,
            "created_at": meal_query.created_at,
            "last_updated": meal_query.last_updated,
            "in_diet": meal_query.in_diet,
            "owner_id": meal_query.owner_id
        }
        return jsonify(meal)
    return jsonify({"message": "Refeição não encontrada"}), 404


@meal_routes.route('/meals/<int:meal_id>', methods=['PUT'])
def update_meal(meal_id):
    data = request.json
    title = data.get("title")
    description = data.get("description")
    in_diet = data.get("in_diet")
    meal_query = Meal.query.filter_by(
        owner_id=current_user.id, id=meal_id).first()
    if meal_query:
        if in_diet:
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
