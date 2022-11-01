from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://www.graodegente.com.br/')

sleep(3)

elemento = navegador.find_element(By.ID,'header-search')
elemento.send_keys('144712')
sleep(1.2)
click_button = navegador.find_element(By.ID, 'searchSubmit')
click_button.click()







