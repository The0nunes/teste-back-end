#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o 
# valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra


lista = [1, 2, 3, 4, 5, 6]

# variável usada para controle
i = 0

while i <= 5 and i < len(lista):
    print(lista[i])
    i += 1

# usei um loop 'while' e uma variável 'i' para imprimir itens da lista. 
# enquanto 'i' for menor ou igual a 5, o loop continua a rodar e imprime os itens. 
# apenas os primeiros 6 itens da lista (ou menos, se a lista tiver menos itens) são impressos.
