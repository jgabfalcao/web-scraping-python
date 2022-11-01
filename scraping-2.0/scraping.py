from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 
#from selenium.webdriver.chrome.options import Options

#options = Options()
#options.add_argument('--headless')
#options.add_argument('window-size=400,800')
produto_nome = input('Qual produto você deseja buscar na Grão de Gente? ---> ')
navegador = webdriver.Chrome()
navegador.get('https://www.graodegente.com.br/')

sleep(2)

input_place = navegador.find_element(By.ID, 'header-search')
input_place.send_keys(produto_nome)
input_place.submit()

sleep(2)

page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')
print(site.prettify())
