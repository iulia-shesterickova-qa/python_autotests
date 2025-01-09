import requests


URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'aa2010f4ac09997032effd6916e7b1de'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Жужка",
    "photo_id": 920
}

body_new_name = {
    "pokemon_id": "186083",
    "name": "Гунька",
    "photo_id": 820
}

body_pokeball = {
    "pokemon_id": "186083"
}

response_create = requests.post(url = f'{URL}pokemons' , headers = HEADER, json = body_create)
print(response_create.text)

'''response_new_name = requests.put(url = f'{URL}pokemons' , headers = HEADER, json = body_new_name)
print(response_new_name.text)'''

'''response_pokeball = requests.post(url = f'{URL}trainers/add_pokeball' , headers = HEADER, json = body_pokeball)
print(response_pokeball.text)'''