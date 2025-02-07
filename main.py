from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que é pra garantir que esta funfando!
    '''
    return {'Hello':'World!'}

@app.get('/api/restaurants/')
def get_restaurants(restaurant: str = Query(None)):
    '''
    Endpoint para visualizar os cardápios dos restaurantes!
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:     #Confirma a conexão com o JSON
        data_json = response.json()     #Salva os dados em uma nova variável
        
        if restaurant is None:
            return {'Data': data_json}
        
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