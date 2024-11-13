# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar o CORS
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Transaction, Category, CreditCard
from config import get_config  # Importar a função para obter a configuração
from datetime import datetime

app = Flask(__name__)
app.config.from_object(get_config())  # Carregar a configuração adequada
CORS(app)  # Inicializar o CORS

jwt = JWTManager(app)  # Inicialização do JWT Manager
db.init_app(app)  # Inicialização do SQLAlchemy

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    """Rota principal"""
    return jsonify({'message': 'API de Gestão Financeira'}), 200

@app.route('/register', methods=['POST'])
def register():
    """Rota para registrar um novo usuário"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 409

    user = User(
        username=username,
        password=generate_password_hash(password)
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Rota para autenticar usuário e retornar token JWT"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.username)
    return jsonify({'access_token': access_token}), 200

# Outras rotas permanecem inalteradas...