#DESAFIO!!
'''
crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo,aonde 
o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta,e a 
realização das operações de saque e deposito do saldo da conta.
'''

import tkinter as tk
from tkinter import messagebox

# Cria a classe ContaBancaria com informações e funções para gerenciar uma conta bancária
class ContaBancaria:
    id_counter = 1  # Conta que vai criar números únicos para cada nova conta

    def __init__(self, nome, cpf):
        self.id = ContaBancaria.id_counter  # Dá um número único para a nova conta
        ContaBancaria.id_counter += 1  # Prepara o próximo número para a próxima conta
        self.nome = nome  # Nome do dono da conta
        self.cpf = cpf  # CPF do dono da conta
        self.saldo = 0.0  # Começa o saldo da conta em 0

    def depositar(self, valor):
        if valor > 0:  # Verifica se o valor do depósito é positivo
            self.saldo += valor  # Adiciona o valor ao saldo da conta
            return f'Depósito de R${valor:.2f} feito com sucesso.'
        else:
            return 'O valor do depósito deve ser positivo.'

    def sacar(self, valor):
        if valor > 0:  # Verifica se o valor do saque é positivo
            if valor <= self.saldo:  # Verifica se há dinheiro suficiente para o saque
                self.saldo -= valor  # Remove o valor do saldo da conta
                return f'Saque de R${valor:.2f} feito com sucesso.'
            else:
                return 'Saldo insuficiente.'  # Informa que não há dinheiro suficiente
        else:
            return 'O valor do saque deve ser positivo.'

    def consultar_saldo(self):
        return self.saldo  # Retorna o saldo atual da conta

# Função para criar uma nova conta
def criar_conta():
    nome = entry_nome.get()  # Pega o nome do dono da conta
    cpf = entry_cpf.get()  # Pega o CPF do dono da conta
    global conta
    conta = ContaBancaria(nome, cpf)  # Cria uma nova conta
    messagebox.showinfo("Conta Criada", f'Conta criada com sucesso! ID: {conta.id}')  # Mostra o número da nova conta

# Função para fazer depósito
def depositar():
    try:
        valor = float(entry_valor.get())  # Pega o valor do depósito
        mensagem = conta.depositar(valor)  # Faz o depósito
        messagebox.showinfo("Resultado", mensagem)  # Mostra o resultado do depósito
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido.")  # Mostra erro se o valor não for válido

# Função para fazer saque
def sacar():
    try:
        valor = float(entry_valor.get())  # Pega o valor do saque
        mensagem = conta.sacar(valor)  # Faz o saque
        messagebox.showinfo("Resultado", mensagem)  # Mostra o resultado do saque
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido.")  # Mostra erro se o valor não for válido

# Função para consultar o saldo
def consultar_saldo():
    saldo = conta.consultar_saldo()  # Pega o saldo da conta
    messagebox.showinfo("Saldo", f'Saldo atual: R${saldo:.2f}')  # Mostra o saldo atual

# Cria a janela principal
root = tk.Tk()
root.title("Sistema Bancário")

# Adiciona os campos e botões à janela
tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="CPF:").pack()
entry_cpf = tk.Entry(root)
entry_cpf.pack()

tk.Button(root, text="Criar Conta", command=criar_conta).pack()

tk.Label(root, text="Valor:").pack()
entry_valor = tk.Entry(root)
entry_valor.pack()

tk.Button(root, text="Depositar", command=depositar).pack()
tk.Button(root, text="Sacar", command=sacar).pack()
tk.Button(root, text="Consultar Saldo", command=consultar_saldo).pack()

# Define a variável conta como vazia até que uma conta seja criada
conta = None

# Inicia a interface gráfica
root.mainloop()
