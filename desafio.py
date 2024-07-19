#DESAFIO!!
'''
crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo,aonde 
o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta,e a 
realização das operações de saque e deposito do saldo da conta.
'''

# cria a classe ContaBancaria com detalhes e ações para uma conta bancária
class ContaBancaria:
    id_counter = 1  # conta que vai gerar IDs automáticos para cada nova conta

    # função que começa a classe e define os detalhes da conta
    def __init__(self, nome, cpf):
        self.id = ContaBancaria.id_counter  # dá um ID único para a nova conta
        ContaBancaria.id_counter += 1  # aumenta o contador para o próximo ID
        self.nome = nome  # nome da pessoa com a conta
        self.cpf = cpf  # CPF da pessoa com a conta
        self.saldo = 0.0  # começa o saldo da conta em 0

    # função para adicionar dinheiro à conta
    def depositar(self, valor):
        if valor > 0:  # checa se o valor do depósito é positivo
            self.saldo += valor  # adiciona o valor ao saldo da conta
            print(f'Depósito de R${valor:.2f} feito com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

    # função para retirar dinheiro da conta
    def sacar(self, valor):
        if valor > 0:  # checa se o valor do saque é positivo
            if valor <= self.saldo:  # checa se há saldo suficiente para o saque
                self.saldo -= valor  # subtrai o valor do saldo da conta
                print(f'Saque de R${valor:.2f} feito com sucesso.')
            else:
                print('Saldo insuficiente.')  # avisa que não há saldo suficiente
        else:
            print('O valor do saque deve ser positivo.')

    # função para mostrar o saldo da conta
    def consultar_saldo(self):
        return self.saldo  # retorna o saldo atual da conta

# função para criar uma nova conta
def criar_conta():
    nome = input('Digite o nome do titular: ')  # pede o nome do titular da conta
    cpf = input('Digite o CPF do titular: ')  # pede o CPF do titular da conta
    conta = ContaBancaria(nome, cpf)  # cria uma nova conta
    print(f'Conta criada com sucesso! ID: {conta.id}')  # mostra o ID da nova conta
    return conta  # retorna a conta criada

# função que exibe o menu e lida com as escolhas do usuário
def menu():
    conta = criar_conta()  # cria uma nova conta
    while True:  # loop que continua até o usuário escolher sair
        print('\nMenu:')
        print('1. Depositar')  # opção para fazer um depósito
        print('2. Sacar')  # opção para fazer um saque
        print('3. Consultar Saldo')  # opção para ver o saldo
        print('4. Sair')  # opção para sair do programa

        opcao = input('Escolha uma opção: ')  # pede para o usuário escolher uma opção

        if opcao == '1':  # se o usuário escolher a opção de depósito
            valor = float(input('Digite o valor do depósito: '))  # pede o valor do depósito
            conta.depositar(valor)  # faz o depósito
        elif opcao == '2':  # se o usuário escolher a opção de saque
            valor = float(input('Digite o valor do saque: '))  # pede o valor do saque
            conta.sacar(valor)  # faz o saque
        elif opcao == '3':  # se o usuário escolher a opção de saldo
            print(f'Saldo atual: R${conta.consultar_saldo():.2f}')  # mostra o saldo atual
        elif opcao == '4':  # se o usuário escolher sair
            print('Saindo...')  # informa que está saindo
            break  # sai do loop e termina o programa
        else:
            print('Opção inválida. Tente novamente.')  # informa que a opção escolhida não é válida

# começa o programa chamando a função menu quando o script é executado diretamente
if __name__ == "__main__":
    menu()
