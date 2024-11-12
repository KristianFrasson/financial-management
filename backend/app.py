# backend/app.py
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Transaction, Category, CreditCard
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financial.db'  # Configuração do banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'dev-key')  # Chave secreta para JWT

jwt = JWTManager(app)  # Inicialização do JWT Manager
db.init_app(app)  # Inicialização do SQLAlchemy

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Rota para registrar um novo usuário"""
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 409
    
    user = User(
        username=data['username'],
        password=generate_password_hash(data['password'])
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Rota para autenticar usuário e retornar token JWT"""
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401
    
    access_token = create_access_token(identity=user.username)
    return jsonify({'access_token': access_token}), 200

@app.route('/transactions', methods=['POST'])
@jwt_required()
def create_transaction():
    """Rota para criar uma nova transação financeira"""
    current_user = get_jwt_identity()  # Obtém o usuário atual a partir do token JWT
    user = User.query.filter_by(username=current_user).first()
    data = request.get_json()
    amount = data.get('amount')
    date = data.get('date')
    description = data.get('description')
    category_id = data.get('category_id')

    # Converter a data de string para objeto datetime
    date_obj = datetime.strptime(date, '%Y-%m-%d')

    # Criar nova transação
    new_transaction = Transaction(
        amount=amount,
        date=date_obj,
        description=description,
        category_id=category_id,
        user_id=user.id
    )
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({'msg': 'Transação criada com sucesso'}), 201

@app.route('/transactions', methods=['GET'])
@jwt_required()
def get_transactions():
    """Rota para listar todas as transações do usuário autenticado"""
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    transactions = Transaction.query.filter_by(user_id=user.id).all()
    result = []
    for transaction in transactions:
        result.append({
            'id': transaction.id,
            'amount': transaction.amount,
            'date': transaction.date.strftime('%Y-%m-%d'),
            'description': transaction.description,
            'category': transaction.category.name
        })
    return jsonify(result), 200

# Outras rotas para atualizar e deletar transações podem ser adicionadas posteriormente