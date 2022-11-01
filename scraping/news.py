from random import betavariate
import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')
#Guardando o conteúdo em uma variável
content = response.content

#Conversão do content em um metódo BeautifulSoup para acessar aquilo que tenho interesse na página
site = BeautifulSoup(content, 'html.parser')

##Buscar especifica da tag HTML (attrs - atributo)
noticia = site.find('div', attrs={'class': 'feed-post-body'})

#Obtendo o conteúdo da tag A dentro do scraping da tag div com a classe denominada
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
#obter somente o texto dessa tag
print(titulo.text)
print(subtitulo.text)


