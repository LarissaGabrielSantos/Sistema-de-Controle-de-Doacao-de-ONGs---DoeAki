import tkinter as tk
from tkinter import messagebox
from interface.janela_principal import abrir_janela_principal

USUARIO_PADRAO = "admin"

def verificar_login(usuario_digitado):
    return usuario_digitado == USUARIO_PADRAO

def iniciar_sistema():
    def ao_clicar_login():
        usuario = entrada_usuario.get()
        if verificar_login(usuario):
            janela_login.destroy()
            abrir_janela_principal()
        else:
            messagebox.showerror("Erro", "Usuário inválido!")

    janela_login = tk.Tk()
    janela_login.title("Login - Sistema de Doações")
    janela_login.geometry("300x150")

    tk.Label(janela_login, text="Usuário:").pack(pady=10)
    entrada_usuario = tk.Entry(janela_login)
    entrada_usuario.pack()

    botao_login = tk.Button(janela_login, text="Entrar", command=ao_clicar_login)
    botao_login.pack(pady=10)

    janela_login.mainloop()