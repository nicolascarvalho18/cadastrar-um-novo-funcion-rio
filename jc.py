import tkinter as tk
from tkinter import messagebox
import json
import os

# Nome do arquivo JSON para armazenar os dados dos funcionários
arquivo_dados = "funcionarios.json"

# Função para carregar os dados do arquivo JSON
def carregar_dados():
    if os.path.exists(arquivo_dados):
        with open(arquivo_dados, 'r') as f:
            return json.load(f)
    return []

# Função para salvar os dados no arquivo JSON
def salvar_dados(dados):
    with open(arquivo_dados, 'w') as f:
        json.dump(dados, f, indent=4)

# Função para cadastrar um novo funcionário
def cadastrar_funcionario():
    nome = entry_nome.get()
    salario = entry_salario.get()
    telefone = entry_telefone.get()
    cpf = entry_cpf.get()
    email = entry_email.get()
    pix = entry_pix.get()

    if not (nome and salario and telefone and cpf and email and pix):
        messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")
        return

    funcionario = {
        "nome": nome,
        "salario": salario,
        "telefone": telefone,
        "cpf": cpf,
        "email": email,
        "pix": pix
    }

    dados = carregar_dados()
    dados.append(funcionario)
    salvar_dados(dados)
    messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
    limpar_campos()

# Função para limpar os campos do formulário
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_salario.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_pix.delete(0, tk.END)

# Função para buscar um funcionário pelo CPF
def buscar_funcionario():
    cpf = entry_buscar.get()
    dados = carregar_dados()
    for funcionario in dados:
        if funcionario['cpf'] == cpf:
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, funcionario['nome'])
            entry_salario.delete(0, tk.END)
            entry_salario.insert(0, funcionario['salario'])
            entry_telefone.delete(0, tk.END)
            entry_telefone.insert(0, funcionario['telefone'])
            entry_cpf.delete(0, tk.END)
            entry_cpf.insert(0, funcionario['cpf'])
            entry_email.delete(0, tk.END)
            entry_email.insert(0, funcionario['email'])
            entry_pix.delete(0, tk.END)
            entry_pix.insert(0, funcionario['pix'])
            return
    messagebox.showwarning("Atenção", "Funcionário não encontrado!")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cadastro de Funcionários")
janela.geometry("400x400")

# Widgets do formulário de cadastro
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack(pady=5)
entry_nome = tk.Entry(janela)
entry_nome.pack(pady=5)

label_salario = tk.Label(janela, text="Salário:")
label_salario.pack(pady=5)
entry_salario = tk.Entry(janela)
entry_salario.pack(pady=5)

label_telefone = tk.Label(janela, text="Telefone:")
label_telefone.pack(pady=5)
entry_telefone = tk.Entry(janela)
entry_telefone.pack(pady=5)

label_cpf = tk.Label(janela, text="CPF:")
label_cpf.pack(pady=5)
entry_cpf = tk.Entry(janela)
entry_cpf.pack(pady=5)

label_email = tk.Label(janela, text="Email:")
label_email.pack(pady=5)
entry_email = tk.Entry(janela)
entry_email.pack(pady=5)

label_pix = tk.Label(janela, text="Pix:")
label_pix.pack(pady=5)
entry_pix = tk.Entry(janela)
entry_pix.pack(pady=5)

botao_cadastrar = tk.Button(janela, text="Cadastrar Funcionário", command=cadastrar_funcionario)
botao_cadastrar.pack(pady=20)

# Widgets para buscar funcionário
label_buscar = tk.Label(janela, text="Buscar Funcionário pelo CPF:")
label_buscar.pack(pady=5)
entry_buscar = tk.Entry(janela)
entry_buscar.pack(pady=5)
botao_buscar = tk.Button(janela, text="Buscar", command=buscar_funcionario)
botao_buscar.pack(pady=5)

janela.mainloop()