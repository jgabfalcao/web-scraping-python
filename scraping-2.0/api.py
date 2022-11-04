import requests
import os

os.system('clear')

cep = input('Digite o CEP: ')

response = requests.get('https://viacep.com.br//ws/' + cep + '/json/')

os.system('clear')

data = response.json()

print('CEP: ', data['cep'])
print('Rua: ', data['logradouro'])
print('Estado: ', data['uf'])
print('Cidade: ', data['localidade'])
print('Bairro: ', data['bairro'])

