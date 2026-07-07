from models.produto import Produto

class ProdutoService:
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self, codigo, nome, preco, estoque):
        produto = Produto(codigo, nome, preco, estoque)
        self.produtos.append(produto)
    
    def listar_produtos(self):
        for produto in self.produtos:
            print(f"Produto:{produto.nome}, Código:{produto.codigo}, Valor:{produto.preco:.2f}, Estoque:{produto.estoque}")