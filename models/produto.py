class Produto:
    def __init__(self, codigo, nome, preco, estoque, categoria, tamanho=None, cor=None, imagem_url=None):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.categoria = categoria
        self.tamanho = tamanho
        self.cor = cor
        self.imagem_url = imagem_url