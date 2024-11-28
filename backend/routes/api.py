# backend/routes/api.py

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

api_bp = Blueprint('api', __name__)

@api_bp.route('/category-analysis', methods=['GET'])
@jwt_required()
def category_analysis():
    # Exemplo de dados; substitua pelos dados reais
    data = [
        {'category': 'Alimentação', 'value': 500},
        {'category': 'Transporte', 'value': 300},
        {'category': 'Educação', 'value': 200},
    ]
    return jsonify(data), 200