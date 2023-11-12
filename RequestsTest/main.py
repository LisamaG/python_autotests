import requests

token = '4ade5b391ecfdc15e62a1f9aa73d82c4'

response = requests.post(url='https://api.pokemonbattle.me:9104//pokemons', json = {
    "name": "Kiba",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type': 'application/json','trainer_token': token},)

print(response.text)


response_name = requests.put(url='https://api.pokemonbattle.me:9104//pokemons', json = {
    "pokemon_id": "18900",
    "name": "New Name",
    "photo" : "https://dolnikov.ru/pokemons/albums/009.png"
}, headers = {'Content-Type': 'application/json','trainer_token': token},)

print(response_name.text)

response_pokebol = requests.post(url='https://api.pokemonbattle.me:9104//trainers/add_pokeball', json = {
    "pokemon_id": "18900"
}, headers = {'Content-Type': 'application/json','trainer_token': token},)

print(response_pokebol.text)

