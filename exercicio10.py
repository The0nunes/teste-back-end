#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

from collections import deque

# Criando uma lista FIFO
fifo = deque([1, 2, 3, 4, 5])
fifo.append(6)

print(fifo)
# usei a estrutura de dados deque da biblioteca collections, que é ideal para operações FIFO, adicionando um item que no ex. foi o nº 6,
# com append() mantém a ordem correta dos itens na fila.
