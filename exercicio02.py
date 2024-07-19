#2-Use o JSON abaixo para capturar o preço do produto B
# explique detalhadamente por que escolheu essa solução e não outra

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {"rua": "Rua Exemplo", "cidade": "Exemplo City"},
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

# pegando/capturando o preço do Produto B
preco_produto_b = next(produto['preço'] for produto in responsejson['produtos'] if produto['nome'] == 'Produto B')
print(preco_produto_b)

# escolhi fazer dessa maneira porque ela é direta, fácil de entender e eficiente,
# ela faz exatamente o que é necessário sem ser complexo desnecessáriamente.