import requests

response = requests.get('https://www.graodegente.com.br/')

print('Status code: ', response.status_code)
print ('Header')
print(response.headers)

print('\nContent')
print(response.content)