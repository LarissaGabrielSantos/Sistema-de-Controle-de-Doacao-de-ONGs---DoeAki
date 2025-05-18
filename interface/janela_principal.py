import tkinter as tk
from tkinter import messagebox, ttk
from banco_dados.operacoes import inserir_doacao, listar_doacoes, editar_doacao, remover_doacao
from relatorios.visualizar import abrir_relatorio

def abrir_janela_principal():
    def cadastrar():
        inserir_doacao(
            entrada_nome.get(),
            entrada_item.get(),
            int(entrada_quantidade.get()),
            entrada_data.get(),
            entrada_obs.get()
        )
        listar()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Doação cadastrada com sucesso!")

    def listar():
        for i in tabela.get_children():
            tabela.delete(i)
        for linha in listar_doacoes():
            tabela.insert("", "end", values=linha)

    def editar():
        item = tabela.focus()
        if item:
            valores = tabela.item(item, "values")
            editar_doacao(
                valores[0],
                entrada_nome.get(),
                entrada_item.get(),
                int(entrada_quantidade.get()),
                entrada_data.get(),
                entrada_obs.get()
            )
            listar()
            limpar_campos()
            messagebox.showinfo("Sucesso", "Doação atualizada!")
          

    def excluir():
        item = tabela.focus()
        if item:
            valores = tabela.item(item, "values")
            remover_doacao(valores[0])
            listar()
            limpar_campos()
            messagebox.showinfo("Sucesso", "Doação removida!")

    def preencher_campos(evento):
        item = tabela.focus()
        valores = tabela.item(item, "values")
        entrada_nome.delete(0, tk.END)
        entrada_nome.insert(0, valores[1])
        entrada_item.delete(0, tk.END)
        entrada_item.insert(0, valores[2])
        entrada_quantidade.delete(0, tk.END)
        entrada_quantidade.insert(0, valores[3])
        entrada_data.delete(0, tk.END)
        entrada_data.insert(0, valores[4])
        entrada_obs.delete(0, tk.END)
        entrada_obs.insert(0, valores[5])

    def limpar_campos():
        entrada_nome.delete(0, tk.END)
        entrada_item.delete(0, tk.END)
        entrada_quantidade.delete(0, tk.END)
        entrada_data.delete(0, tk.END)
        entrada_obs.delete(0, tk.END)

    janela = tk.Tk()
    janela.title("Doe Aki")
    janela.geometry("800x600")

    tk.Label(janela, text="Nome do Doador").grid(row=0, column=0)
    entrada_nome = tk.Entry(janela)
    entrada_nome.grid(row=0, column=1)

    tk.Label(janela, text="Item Doado").grid(row=1, column=0)
    entrada_item = tk.Entry(janela)
    entrada_item.grid(row=1, column=1)

    tk.Label(janela, text="Quantidade").grid(row=2, column=0)
    entrada_quantidade = tk.Entry(janela)
    entrada_quantidade.grid(row=2, column=1)

    tk.Label(janela, text="Data da Doação").grid(row=3, column=0)
    entrada_data = tk.Entry(janela)
    entrada_data.grid(row=3, column=1)

    tk.Label(janela, text="Observações").grid(row=4, column=0)
    entrada_obs = tk.Entry(janela)
    entrada_obs.grid(row=4, column=1)

    tk.Button(janela, text="Cadastrar", command=cadastrar).grid(row=5, column=0)
    tk.Button(janela, text="Editar", command=editar).grid(row=5, column=1)
    tk.Button(janela, text="Excluir", command=excluir).grid(row=5, column=2)
    tk.Button(janela, text="Relatórios", command=abrir_relatorio).grid(row=5, column=3)

    colunas = ("ID", "Nome", "Item", "Quantidade", "Data", "Observações")
    tabela = ttk.Treeview(janela, columns=colunas, show="headings")
    for col in colunas:
        tabela.heading(col, text=col)
        tabela.column(col, minwidth=0, width=100)
    tabela.grid(row=6, column=0, columnspan=4, padx=10, pady=10)
    tabela.bind("<Double-1>", preencher_campos)

    listar()
    janela.mainloop()