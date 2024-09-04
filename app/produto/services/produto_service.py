from app import mongo
from app.produto.models.produto_model import ProdutoModel
from bson.objectid import ObjectId  # Para manipular ObjectId

class ProdutoService:
    @staticmethod
    def get_all_produtos():
        produtos = mongo.produtos.find()  # Usando a coleção 'produtos'
        return [{"_id": str(produto["_id"]), "name": produto["name"], "description": produto["description"]} for produto in produtos]

    @staticmethod
    def get_produto_by_id(produto_id):
        produto = mongo.produtos.find_one({"_id": ObjectId(produto_id)})  # Usando ObjectId para a query
        if produto:
            produto['_id'] = str(produto['_id'])  # Converter ObjectId para string
        return produto

    @staticmethod
    def create_produto(data):
        produto = ProdutoModel(**data)
        result = mongo.produtos.insert_one(produto.to_dict())
        return result.inserted_id

    @staticmethod
    def update_produto(produto_id, data):
        mongo.produtos.update_one({"_id": ObjectId(produto_id)}, {"$set": data})

    @staticmethod
    def delete_produto(produto_id):
        mongo.produtos.delete_one({"_id": ObjectId(produto_id)})
