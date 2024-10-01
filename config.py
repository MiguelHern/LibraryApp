import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')  # Se crea el archivo 'app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clave secreta para sesiones y seguridad
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mi_clave_secreta_super_segura')
