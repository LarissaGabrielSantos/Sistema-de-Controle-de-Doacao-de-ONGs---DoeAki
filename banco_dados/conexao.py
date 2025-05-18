import sqlite3

def conectar():
    conexao = sqlite3.connect("doacoes.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS doacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_doador TEXT,
            item_doado TEXT,
            quantidade INTEGER,
            data_doacao TEXT,
            observacoes TEXT
        );
    """)
    conexao.commit()
    return conexao