#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
# Explique detalhadamente por que voce decidiu essa solução e não outra

response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

produtos_maior_30 = []  # aqui cria uma lista vazia para os produtos que têm o preço maior que 30

for loja in response:  # passa por cada loja na lista de lojas
    for produto in loja['produtos']:  # dentro de cada loja, passa a lista de produtos
        if produto['preço'] > 30:  # aqui é feita a verificação se o preço do produto é maior que 30
            produtos_maior_30.append(produto)  # se for, adiciona o produto à lista produtos_maior_30

print(produtos_maior_30)  # imprime a lista final de produtos com preço maior que 30

# Escolhi essa solução por ser clara, simples e eficiente. O código verifica cada loja e seus produtos usando 
# comandos básicos como for e if, o que é fácil de entender e manter. Ele verifica o preço de cada produto uma vez 
# e só adiciona à lista se for maior que R$30, sendo o processo rápido e direto.
