import sqlite3

sqlite3.connect("ecommerce.db")

def conectar():
    conexao = sqlite3.connect("ecommerce.db")
    return conexao
    conn.execute("PRAGMA foreign_keys = ON")
    return execute