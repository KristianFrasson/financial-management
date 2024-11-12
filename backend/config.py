# backend/config.py
import os
from datetime import timedelta

class Config:
    """Configuração base"""
    # Configurações do SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configurações de Segurança
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta-desenvolvimento'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-chave-secreta-desenvolvimento'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    
    # Configurações CORS
    CORS_HEADERS = 'Content-Type'
    
    # Configurações de Log
    LOG_LEVEL = 'INFO'

class DevelopmentConfig(Config):
    """Configuração de desenvolvimento"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///financial_dev.db'
    
    # Configurações de Email (para desenvolvimento)
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 8025
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = None
    MAIL_PASSWORD = None

class TestingConfig(Config):
    """Configuração de testes"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///financial_test.db'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    """Configuração de produção"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///financial_prod.db'
    
    # Configurações de Email (para produção)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# Dicionário de configurações
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# Função para obter a configuração atual
def get_config():
    """Retorna a configuração baseada na variável de ambiente FLASK_ENV"""
    return config[os.environ.get('FLASK_ENV') or 'default']