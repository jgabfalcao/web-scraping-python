import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'
produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')
#class="andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default"

produto = site.find('div' , attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default'})

titulo = produto.find('h2' , attrs={'class': 'ui-search-item__title shops__item-title'})
titulo = (titulo.text)

preco = produto.find('span' , attrs={'class': 'price-tag-amount'})
preco = (preco.text)

print(titulo)
print(preco)






