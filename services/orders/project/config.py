# services/orders/project/config.py


class BaseConfig:
    """Configuración báse"""
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Configuración de desarrollo"""
    pass


class TestingConfig(BaseConfig):
    """Configuración de prueba"""
    TESTING = True


class ProductionConfig(BaseConfig):
    """Configuración de producción"""
    pass
