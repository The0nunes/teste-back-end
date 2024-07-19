#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana", "joao", "ricardo", "joao"]

# Substitui todos os "joao" por "maria" usando o list comprehension
lista = ['maria' if item == 'joao' else item for item in lista] # se o 'item' dentro da lista for igual a joao ele será substituído por maria

print(lista)

# é uma maneira fácil e eficaz para fazer substituições em listas.
