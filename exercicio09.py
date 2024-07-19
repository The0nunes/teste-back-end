#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra


import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.json()

for user in users:
    nome = user.get('name')
    username = user.get('username')
    email = user.get('email')
    rua = user['address'].get('street')
    numero = user['address'].get('suite')
    print(f"Nome: {nome}, Username: {username}, Email: {email}, Rua: {rua}, Número: {numero}")

# usei a função 'get()' para evitar erros ao acessar chaves que podem não existir, retornando 'None' ou um valor padrão.
# Isso torna o código mais seguro e confiável.


