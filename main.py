from interface.janela_login import iniciar_sistema
from banco_dados.conexao import conectar

if __name__ == "__main__":
    conectar()
    iniciar_sistema()