# services/orders/project/config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../data.sqlite')

class BaseConfig:
    """Configuración báse"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # nuevo


class DevelopmentConfig(BaseConfig):
    """Configuración de desarrollo"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + db_path  # nuevo


class TestingConfig(BaseConfig):
    """Configuración de prueba"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')  # nuevo


class ProductionConfig(BaseConfig):
    """Configuración de producción"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # nuevo
