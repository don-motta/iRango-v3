import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:     #Confirma a conexão com o JSON
    data_json = response.json()     #Salva os dados em uma nova variável
    data_restaurant = {}            #Cria um dicionário para separar os dados
    for item in data_json:
        name_restaurant = item['Company']
        if name_restaurant not in data_restaurant:
            data_restaurant[name_restaurant] = []     

        data_restaurant[name_restaurant].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
            })

else:
    print(f'O erro foi {response.status_code}')

#Criar um arquivo JSON com os dados do restaurante
for name_restaurant, data in data_restaurant.items():  #Para cada 'name_restaurant' no dicionário 'data_restaurants', vou pegar os items e salvar em'data'.
    name_file = f'{name_restaurant}.json'  #Concatena o nome que será utilizado para o arquivo.
    with open(name_file, 'w') as file_restaurant:  #'w' significa "write", o que sera feito com o arquivo.
        json.dump(data, file_restaurant, indent=4)