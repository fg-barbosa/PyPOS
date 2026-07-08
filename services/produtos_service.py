from database.conexao import conectar

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

    def atualizar_produto(self, codigo, nome, preco, estoque, categoria, tamanho, cor, imagem_url):
        produto = self.buscar_por_codigo(codigo)

        if produto is None:
            print("Produto não encontrado.")
            return
        
        self.cursor.execute("""
            UPDATE produtos
            SET nome = ?, preco = ?, estoque = ?, categoria = ?, tamanho = ?, cor = ?, imagem_url = ?
            WHERE codigo = ?
        """, (nome, preco, estoque, categoria, tamanho, cor, imagem_url, codigo))

        self.conn.commit()
        print("Produto atualizado com sucesso!")

    def buscar_por_codigo(self, codigo):
        self.cursor.execute("SELECT * FROM produtos WHERE codigo = ?", (codigo,))
        return self.cursor.fetchone()

    def excluir_produto(self, codigo):
        produto = self.buscar_por_codigo(codigo)

        if produto is None:
            print("Produto não encontrado.")
            return

        self.cursor.execute("""
            DELETE FROM produtos
            WHERE codigo = ?
        """, (codigo,))

        self.conn.commit()
        print("Produto excluído com sucesso!")

    def adicionar_estoque(self, codigo, quantidade):
        produto = self.buscar_por_codigo(codigo)

        if produto is None:
            print("Produto não encontrado.")
            return

        self.cursor.execute("""
            UPDATE produtos
            SET estoque = estoque + ?
            WHERE codigo = ?
        """, (quantidade, codigo))

        self.conn.commit()
        print("Estoque atualizado com sucesso!")

    def baixar_estoque(self, codigo, quantidade):
        produto = self.buscar_por_codigo(codigo)

        if produto is None:
            print("Produto não encontrado.")
            return

        estoque_atual = produto[3]

        if quantidade > estoque_atual:
            print("Estoque insuficiente.")
            return

        self.cursor.execute("""
            UPDATE produtos
            SET estoque = estoque - ?
            WHERE codigo = ?
        """, (quantidade, codigo))

        self.conn.commit()
        print("Estoque baixado com sucesso!")

    def listar_estoque_baixo(self, limite=5):
        self.cursor.execute("""
            SELECT * FROM produtos
            WHERE estoque <= ?
        """, (limite,))

        return self.cursor.fetchall()