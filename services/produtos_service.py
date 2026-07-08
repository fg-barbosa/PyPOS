import sqlite3
from models.produto import Produto

class ProdutoService:
    def __init__(self):
        self.conn = sqlite3.connect("ecommerce.db")
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

    def cadastrar_produto(self, nome, preco, estoque, categoria, tamanho, cor, imagem_url):
        self.cursor.execute("""
            INSERT INTO produtos (nome, preco, estoque, categoria, tamanho, cor, imagem_url)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nome, preco, estoque, categoria, tamanho, cor, imagem_url))
        self.conn.commit()

    def listar_todos(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

    def listar_por_categoria(self, categoria):
        self.cursor.execute("SELECT * FROM produtos WHERE categoria LIKE ?", (f"%{categoria}%",))
        return self.cursor.fetchall()

    def buscar_por_codigo(self, codigo):
        self.cursor.execute("SELECT * FROM produtos WHERE codigo = ?", (codigo,))
        return self.cursor.fetchone()

    def baixar_estoque(self, codigo, quantidade):
        self.cursor.execute("""
            UPDATE produtos 
            SET estoque = estoque - ? 
            WHERE codigo = ?
        """, (quantidade, codigo))
        self.conn.commit()