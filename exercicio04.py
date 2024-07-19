#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela

lista = ["   joao   ","   maria   ","  joana  "]

# removendo os espaços em branco e criando uma nova lista
lista_sem_espacos = [item.strip() for item in lista]

print(lista_sem_espacos)
# usei o método strip para remover os espaços em branco que tem em cada string na lista.
