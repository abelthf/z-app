# services/orders/project/config.py
import os



class BaseConfig:
    """Configuración báse"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # nuevo


class DevelopmentConfig(BaseConfig):
    """Configuración de desarrollo"""
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # nuevo
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL' + db_path)  # nuevo
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL' + db_path)  # nuevo
    pass


class TestingConfig(BaseConfig):
    """Configuración de prueba"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')  # nuevo


class ProductionConfig(BaseConfig):
    """Configuración de producción"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # nuevo
