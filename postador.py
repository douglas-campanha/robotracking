from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get('https://facebook.com')
navegador.find_element('xpath', '//*[@id="email"]').send_keys("douglas@campanhadigital.net.br")
navegador.find_element('xpath', '//*[@id="passContainer"]').send_keys("x@#$234x")
navegador.find_element('xpath', '//*[@id="u_0_5_xx"]').click()




