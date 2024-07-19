#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos.
# cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. 
# Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra

import requests

def contar_tasks():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = response.json()
    completadas = sum(1 for task in tasks if task['completed'])
    pendentes = sum(1 for task in tasks if not task['completed'])
    return completadas, pendentes

completadas, pendentes = contar_tasks()
print(f'Tarefas completadas: {completadas}')
print(f'Tarefas pendentes: {pendentes}')

# a função contar_tasks() pede dados para uma API, recebe a resposta em formato JSON e conta quantas tarefas foram feitas
# e quantas estão pendentes. Ela usa uma forma simples e direta para fazer isso, aproveitando as ferramentas da biblioteca
# requests para lidar com os dados da API.
