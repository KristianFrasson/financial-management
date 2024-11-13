# backend/models.py

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Instancia o objeto SQLAlchemy para manipulação do banco de dados

class User(db.Model):
    """Modelo para representar os usuários do sistema"""
    __tablename__ = 'users'  # Nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True)  # Identificador único do usuário
    username = db.Column(db.String(80), unique=True, nullable=False)  # Nome de usuário, único e obrigatório
    password = db.Column(db.String(120), nullable=False)  # Senha criptografada do usuário
    # Relações
    transactions = db.relationship('Transaction', backref='user', lazy=True)  # Relação com as transações
    credit_cards = db.relationship('CreditCard', backref='user', lazy=True)  # Relação com os cartões de crédito

class CreditCard(db.Model):
    """Modelo para representar os cartões de crédito"""
    __tablename__ = 'credit_cards'  # Nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True)  # Identificador único do cartão
    name = db.Column(db.String(80), nullable=False)  # Nome do cartão
    limit = db.Column(db.Float, nullable=False)  # Limite de crédito do cartão
    closing_day = db.Column(db.Integer, nullable=False)  # Dia de fechamento da fatura
    due_day = db.Column(db.Integer, nullable=False)  # Dia de vencimento da fatura
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Referência ao usuário
    # Relações
    transactions = db.relationship('Transaction', backref='credit_card', lazy=True)  # Relação com as transações

class Category(db.Model):
    """Modelo para representar as categorias de transações"""
    __tablename__ = 'categories'  # Nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True)  # Identificador único da categoria
    name = db.Column(db.String(80), nullable=False)  # Nome da categoria
    type = db.Column(db.String(20), nullable=False)  # Tipo da categoria ('income' ou 'expense')
    # Relações
    transactions = db.relationship('Transaction', backref='category', lazy=True)  # Relação com as transações

class Transaction(db.Model):
    """Modelo para representar as transações financeiras"""
    __tablename__ = 'transactions'  # Nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True)  # Identificador único da transação
    amount = db.Column(db.Float, nullable=False)  # Valor da transação
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Data da transação
    description = db.Column(db.String(200))  # Descrição da transação
    installments = db.Column(db.Integer, default=1)  # Número total de parcelas
    current_installment = db.Column(db.Integer, default=1)  # Parcela atual
    recurring = db.Column(db.Boolean, default=False)  # Indica se a transação é recorrente

    # Chaves estrangeiras
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)  # Referência à categoria
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Referência ao usuário
    credit_card_id = db.Column(db.Integer, db.ForeignKey('credit_cards.id'))  # Referência ao cartão de crédito