# main.py

import tkinter as tk  # Importa a biblioteca Tkinter para a interface gráfica
from tkinter import messagebox, simpledialog  # Importa funções de diálogo do Tkinter
from utils.cupom import gerar_cupom_fiscal  # Importa a função gerar_cupom_fiscal do módulo cupom

# Definindo os produtos com seus códigos e descrições
produtos = {
    123: 'Camisa estampada',
    124: 'Camisa social manga longa',
    125: 'Calça jeans'
}

# Definindo as vendas com código do produto, quantidade e valor unitário
venda = [
    (123, 3, 25.55),
    (124, 2, 79.99),
    (125, 1, 99.99)
]

# Função para mostrar o cupom fiscal em uma mensagem
def mostrar_cupom():
    cupom = gerar_cupom_fiscal(produtos, venda)  # Gera o cupom fiscal
    messagebox.showinfo("Cupom Fiscal", cupom)  # Exibe o cupom em uma caixa de mensagem

# Função para adicionar uma nova venda
def adicionar_venda():
    # Solicita o código do produto, quantidade e valor unitário ao usuário
    codigo = simpledialog.askinteger("Entrada", "Digite o código do produto:")
    quantidade = simpledialog.askinteger("Entrada", "Digite a quantidade:")
    valor = simpledialog.askfloat("Entrada", "Digite o valor unitário:")

    # Verifica se os valores inseridos são válidos
    if codigo and quantidade and valor:
        venda.append((codigo, quantidade, valor))  # Adiciona a nova venda à lista de vendas
        messagebox.showinfo("Info", "Venda adicionada com sucesso!")  # Exibe mensagem de sucesso
    else:
        messagebox.showerror("Erro", "Dados inválidos!")  # Exibe mensagem de erro

# Configuração da interface gráfica
root = tk.Tk()  # Cria a janela principal do Tkinter
root.title("Gerador de Cupom Fiscal")  # Define o título da janela

frame = tk.Frame(root)  # Cria um frame dentro da janela principal
frame.pack(padx=10, pady=10)  # Adiciona padding ao frame

# Cria e adiciona o botão para mostrar o cupom fiscal
button_mostrar = tk.Button(frame, text="Mostrar Cupom Fiscal", command=mostrar_cupom)
button_mostrar.pack(pady=5)

# Cria e adiciona o botão para adicionar uma nova venda
button_adicionar = tk.Button(frame, text="Adicionar Venda", command=adicionar_venda)
button_adicionar.pack(pady=5)

# Inicia o loop principal do Tkinter
root.mainloop()
