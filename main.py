from fastapi import FastAPI, Query
import requests

#Criar uma endpoint API usando FastAPI 

app = FastAPI()

@app.get('/api/restaurants/')  #O caminho que o recurso irá acessar
def get_restaurants(restaurant: str = Query(None)):  #tipo do argumento 'string'. 'Query' é uma propriedade do Fast API para inserir o nome do restaurante usando '?restaurant=<nome do restaurante>'.'None' que será o valor default.
    #Abaixo é uma Doc string do endpoint. Utilize "<endereço do servidor>/docs" no browser para consultar a documentação do projeto.
    '''
    Endpoint para visualizar os cardápios dos restaurantes!  
    '''
    
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:     #Confirma a conexão com o JSON
        data_json = response.json()     #Salva os dados em uma nova variável
        
        if restaurant is None:
            return {'Dados': data_json}
        
        data_restaurant = []            #Cria um dicionário para separar os dados
        for item in data_json:
            if item['Company'] == restaurant:
                data_restaurant.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                    })
                
        return {'Restaurante': restaurant, 'Cardápio': data_restaurant}

    else:
        return {'Erro':f'{response.status_code} - {response.text}'}