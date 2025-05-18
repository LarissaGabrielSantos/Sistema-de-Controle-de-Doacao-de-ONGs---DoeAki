from banco_dados.conexao import conectar

def inserir_doacao(nome, item, quantidade, data, obs):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO doacoes (nome_doador, item_doado, quantidade, data_doacao, observacoes) VALUES (?, ?, ?, ?, ?)",
                   (nome, item, quantidade, data, obs))
    conn.commit()
    conn.close()

def listar_doacoes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doacoes")
    dados = cursor.fetchall()
    conn.close()
    return dados

def editar_doacao(id, nome, item, quantidade, data, obs):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE doacoes SET nome_doador=?, item_doado=?, quantidade=?, data_doacao=?, observacoes=? WHERE id=?",
                   (nome, item, quantidade, data, obs, id))
    conn.commit()
    conn.close()

def remover_doacao(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM doacoes WHERE id=?", (id,))
    conn.commit()
    conn.close()