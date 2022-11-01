import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []
url_base = 'https://lista.mercadolivre.com.br/'
produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div' , attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default'})

for produto in produtos:
  titulo = produto.find('h2' , attrs={'class': 'ui-search-item__title shops__item-title'})
  titulo = (titulo.text)
  preco = produto.find('span' , attrs={'class': 'price-tag-amount'})
  preco = (preco.text)
  link = produto.find('a', attrs={'class': 'ui-search-link'})
  link = link['href']
  lista_produtos.append([titulo, preco, link])
  colunas_produtos = pd.DataFrame(lista_produtos, columns=['Nome' , 'Valor', 'Link do Produto'])


#*! EXIBIÇÃO !*#
print(colunas_produtos)







