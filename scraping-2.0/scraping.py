from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 
import pandas as pd
#from selenium.webdriver.chrome.options import Options

#options = Options()
#options.add_argument('--headless')
#options.add_argument('window-size=400,800')
lista_produtos = []
produto_nome = input('Qual produto você deseja buscar na Grão de Gente? ---> ')
navegador = webdriver.Chrome()
navegador.get('https://www.graodegente.com.br/')

sleep(2)

input_place = navegador.find_element(By.ID, 'header-search')

sleep(2)

input_place.send_keys(produto_nome)

sleep(2)

input_place.submit()

sleep(4)

page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')

lista = site.find('ul', attrs={'class':'grid-list'})
produtos = lista.findAll('li', attrs={'itemprop': 'itemListElement'})

for produto in produtos:
  nm_produto = produto.find('h2', attrs={'class': 'content__name'})
  nm_produto = (nm_produto.text)
  
  qt_itens = produto.find('p', attrs={'class': 'content__qttItens'})
  qt_itens = (qt_itens.text)

  vl_produto = produto.find('p', attrs={'class': 'content__price'}).findAll('span')
  vl_produto_12x = vl_produto[2].text
  vl_produto_boleto = vl_produto[3].text

  link = produto.find('a', attrs={'title': nm_produto})
  link = link['href']

  lista_produtos.append([nm_produto, qt_itens, vl_produto_12x,vl_produto_boleto, 'graodegente.com.br'+ link])#
  colunas_produtos = pd.DataFrame(lista_produtos, columns=['Nome', 'Quantidade', 'Valor 12 vezes','Valor Boleto', 'Link'])#

colunas_produtos.to_excel('produtos.xlsx', index=False)





  