# backend/config.py
import os
from datetime import timedelta

class Config:
    """Configuração base"""
    # Configurações do SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configurações de Segurança
    SECRET_KEY = os.environ.get('SECRET_KEY', 'chave-secreta-desenvolvimento')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-chave-secreta-desenvolvimento')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

    # Configurações CORS
    CORS_HEADERS = 'Content-Type'

class DevelopmentConfig(Config):
    """Configuração de desenvolvimento"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///financial_dev.db'

class TestingConfig(Config):
    """Configuração de testes"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///financial_test.db'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    """Configuração de produção"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///financial_prod.db')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config():
    """Retorna a configuração baseada na variável de ambiente FLASK_ENV"""
    env = os.environ.get('FLASK_ENV', 'default')
    return config.get(env, Config)