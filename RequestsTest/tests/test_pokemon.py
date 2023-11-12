import requests
import pytest 

host = 'https://api.pokemonbattle.me:9104'
token = '4ade5b391ecfdc15e62a1f9aa73d82c4'

def test_status_code():
    response = requests.get(f'{host}/trainers',params= {'trainer_id' : 2638})
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers',params= {'trainer_id' : 2638})
    assert response.json()['trainer_name'] == 'Lisa'

@pytest.mark.parametrize('key, value', [('name','Kiba'),
                                      ('trainer_id', '2638'),
                                      ('attack', '1.0')])
    
def test_parts_of_answer(key,value):
        response = requests.get(f'{host}/pokemons', params= {'trainer_id': 2638})
        assert response.json()[0][key] == value