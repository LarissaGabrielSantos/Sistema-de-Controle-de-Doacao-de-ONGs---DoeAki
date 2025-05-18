import tkinter as tk
from tkinter import ttk
from banco_dados.operacoes import listar_doacoes

def abrir_relatorio():
    janela_relatorio = tk.Toplevel()
    janela_relatorio.title("Relatório de Doações")
    janela_relatorio.geometry("700x400")

    colunas = ("ID", "Nome", "Item", "Quantidade", "Data", "Observações")
    tabela = ttk.Treeview(janela_relatorio, columns=colunas, show="headings")
    for col in colunas:
        tabela.heading(col, text=col)
        tabela.column(col, minwidth=0, width=100)
    tabela.pack(expand=True, fill="both", padx=10, pady=10)

    for linha in listar_doacoes():
        tabela.insert("", "end", values=linha)