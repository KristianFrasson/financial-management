# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from models import db
from config import get_config
from routes.auth import auth_bp
from routes.api import api_bp  # Importação adicionada

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(get_config())  # Carregar a configuração adequada
CORS(app)  # Inicializar o CORS
CORS(app, resources={r"/*": {"origins": "https://probable-palm-tree-vxwx9v564j9hp95-3000.app.github.dev/"}})

jwt = JWTManager(app)  # Inicialização do JWT Manager
db.init_app(app)  # Inicialização do SQLAlchemy

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

# Registrar os blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/user-info', methods=['GET'])
@jwt_required()
def user_info():
    """Rota protegida que retorna informações do usuário."""
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200