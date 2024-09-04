from flask import request, jsonify
from flask_restx import Resource
from app.produto.dtos.produto_dto import ProdutoDTO
from app.produto.services.produto_service import ProdutoService

api = ProdutoDTO.api
produto = ProdutoDTO.produto


@api.route("/")
class ProdutoList(Resource):
    @api.doc("list_produtos")
    @api.marshal_list_with(produto)
    def get(self):
        """Lista todos os produtos"""
        return ProdutoService.get_all_produtos()

    @api.expect(produto)
    @api.doc("create_produto")
    def post(self):
        """Cria um novo produto"""
        data = request.json
        produto_id = ProdutoService.create_produto(data)
        return jsonify({"_id": str(produto_id), **data})


@api.route("/<id>")
@api.response(404, "Produto não encontrado")
@api.param("id", "O identificador do produto")
class Produto(Resource):
    @api.doc("get_produto")
    @api.marshal_with(produto)
    def get(self, id):
        """Obtém um produto pelo ID"""
        produto = ProdutoService.get_produto_by_id(id)
        if produto:
            return produto
        return {"message": "Produto não encontrado"}, 404

    @api.expect(produto)
    @api.doc("update_produto")
    def patch(self, id):
        """Atualiza um produto pelo ID"""
        data = request.json
        ProdutoService.update_produto(id, data)
        return jsonify({"msg": "Produto atualizado"})

    @api.doc("delete_produto")
    def delete(self, id):
        """Deleta um produto pelo ID"""
        ProdutoService.delete_produto(id)
        return jsonify({"msg": "Produto deletado"})
