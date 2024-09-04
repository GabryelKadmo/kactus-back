from flask import Flask
from flask_restx import Api
from pymongo import MongoClient

mongo = None

def create_app():
    app = Flask(__name__)
    
    # Configuração do MongoDB usando pymongo
    client = MongoClient("mongodb+srv://gabryelkadmo:kYIrFjENI8iYPdPa@kactus-store.hwdpq.mongodb.net/?retryWrites=true&w=majority&appName=kactus-store")
    global mongo
    mongo = client.kactus  # Acesso ao banco de dados 'meubanco'

    # Configuração da API Flask-RESTx
    api = Api(app, version='1.0', title='Kactus API',
              description='API modular com Flask e MongoDB')
    
    from app.produto.controllers.produto_controller import api as produto_ns
    api.add_namespace(produto_ns, path='/produtos')

    return app
