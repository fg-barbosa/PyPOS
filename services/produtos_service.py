from database.conexao import conectar
from models.produto import Produto

class ProdutoService:
    def __init__(self):
        self.conn = conectar()
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                estoque INTEGER NOT NULL,
                categoria TEXT NOT NULL,
                tamanho TEXT,
                cor TEXT,
                imagem_url TEXT
            )
        """)
        self.conn.commit()

    def transformar_em_produto(self, dados):
        if dados is None:
            return None

        return Produto(
            dados[0],
            dados[1],
            dados[2],
            dados[3],
            dados[4],
            dados[5],
            dados[6],
            dados[7]
        )


    def cadastrar_produto(self, nome, preco, estoque, categoria, tamanho, cor, imagem_url):
        self.cursor.execute("""
            INSERT INTO produtos (nome, preco, estoque, categoria, tamanho, cor, imagem_url)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nome, preco, estoque, categoria, tamanho, cor, imagem_url))
        self.conn.commit()

    def listar_todos(self):
        self.cursor.execute("SELECT * FROM produtos")
        resultados = self.cursor.fetchall()

        produtos = []

        for dados in resultados:
            produto = self.transformar_em_produto(dados)
            produtos.append(produto)

        return produtos

    def listar_por_categoria(self, categoria):
        self.cursor.execute("SELECT * FROM produtos WHERE categoria LIKE ?", (f"%{categoria}%",))
        resultados = self.cursor.fetchall()

        produtos = []

        for dados in resultados:
            produto = self.transformar_em_produto(dados)
            produtos.append(produto)

        return produtos

    def atualizar_produto(self, codigo, nome, preco, estoque, categoria, tamanho, cor, imagem_url):
        produto = self.buscar_por_codigo(codigo)

        if produto is None:
            return False
        
        self.cursor.execute("""
            UPDATE produtos
            SET nome = ?, preco = ?, estoque = ?, categoria = ?, tamanho = ?, cor = ?, imagem_url = ?
            WHERE codigo = ?
        """, (nome, preco, estoque, categoria, tamanho, cor, imagem_url, codigo))

        self.conn.commit()
        return True

    def buscar_por_codigo(self, codigo):
        self.cursor.execute("SELECT * FROM produtos WHERE codigo = ?", (codigo,))
        dados = self.cursor.fetchone()
        return self.transformar_em_produto(dados)

    def excluir_produto(self, codigo):
        produto = self.buscar_por_codigo(codigo)

        if produto is None:
            return False

        self.cursor.execute("""
            DELETE FROM produtos
            WHERE codigo = ?
        """, (codigo,))

        self.conn.commit()
        return True

    def adicionar_estoque(self, codigo, quantidade):
        produto = self.buscar_por_codigo(codigo)

        if produto is None: 
            return False

        self.cursor.execute("""
            UPDATE produtos
            SET estoque = estoque + ?
            WHERE codigo = ?
        """, (quantidade, codigo))

        self.conn.commit()
        return True

    def baixar_estoque(self, codigo, quantidade):
        produto = self.buscar_por_codigo(codigo)

        if produto is None:
            return "produto_nao_encontrado"

        estoque_atual = produto.estoque

        if quantidade > estoque_atual:
            return "estoque_insuficiente"

        self.cursor.execute("""
            UPDATE produtos
            SET estoque = estoque - ?
            WHERE codigo = ?
        """, (quantidade, codigo))

        self.conn.commit()
        return "ok"

    def listar_estoque_baixo(self, limite=5):
        self.cursor.execute("""
            SELECT * FROM produtos
            WHERE estoque <= ?
        """, (limite,))

        resultados = self.cursor.fetchall()

        produtos = []

        for dados in resultados:
            produto = self.transformar_em_produto(dados)
            produtos.append(produto)

        return produtos