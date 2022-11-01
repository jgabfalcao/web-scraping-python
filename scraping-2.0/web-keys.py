from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br/')

sleep(3)

elemento = navegador.find_element(By.TAG_NAME,'input')
elemento.send_keys('Grão de Gente')
sleep(1)

action_enter = ActionChains(navegador)
action_enter.send_keys(Keys.ENTER).perform()
