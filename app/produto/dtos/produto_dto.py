from flask_restx import Namespace, fields

class ProdutoDTO:
    api = Namespace('produtos', description='Operações com produtos')
    produto = api.model('Produto', {
        'name': fields.String(required=True, description='O nome do produto'),
        'description': fields.String(required=True, description='A descrição do produto')
    })
