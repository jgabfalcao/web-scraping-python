from random import betavariate
import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []
response = requests.get('https://g1.globo.com/')

content = response.content
site = BeautifulSoup(content, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias: 
  titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
  #print(titulo.text)
  #print(titulo['href']) #link da noticia
  subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

  if (subtitulo):
    #print(subtitulo.text)
    #para criar um lista 
    lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
  else:
    lista_noticias.append([titulo.text, '', titulo['href']])

#Criação da variável para fazer a exibição em colunas
news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])

#Exportação para outro arquivo (index=false para não salvar o numero da linha)
news.to_excel('noticias.xlsx', index=False)




