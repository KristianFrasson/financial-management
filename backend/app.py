# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db
from config import get_config
from routes.auth import auth_bp

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(get_config())  # Carregar a configuração adequada
CORS(app)  # Inicializar o CORS

jwt = JWTManager(app)  # Inicialização do JWT Manager
db.init_app(app)  # Inicialização do SQLAlchemy

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

# Registrar o blueprint de autenticação
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'API de Gestão Financeira'}), 200