from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import time

with sync_playwright() as p:
     navegador = p.chromium.launch(headless=False)
     pagina = navegador.new_page()
     #acessar Twitter
     pagina.goto('https://twitter.com')
     time.sleep(3)
     #preenche o campo de email
     pagina.fill('xpath=//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]', "douglas@campanhadigital.net.br")
     time.sleep(3)
     #clica no botão avançar
     pagina.locator('xpath=//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
     time.sleep(3)
     #aciona o campo nome de ususário ou celular
     pagina.locator('xpath=//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]').click()
     #preenche o campo com o numero do celular
     pagina.fill('xpath=/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[1]', "11988887699")
     time.sleep(3)
     #clica no botão avançar
     pagina.locator('xpath=//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
     time.sleep(3)
     #digita a senha
     pagina.fill('xpath=//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]', "x@#$234x")
     time.sleep(3)
     #clica no botão entrar
     pagina.locator('xpath=//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
     time.sleep(3)
     #clica no botão explore para pesquisar
     pagina.locator('xpath=//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]').click()
     time.sleep(3)
     #pesquisa o termo
     pagina.fill('xpath=//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input', "Campanha Digital")
     time.sleep(3)
     #clica no botão do primeiro termo clicável
     pagina.locator('xpath=/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div/div[3]/div/div').click()
     time.sleep(3)
     #seleciona a página da pesquisa
     pagina.goto('https://twitter.com/campanhad')
     time.sleep(300)
     #configurar para responder uma mensagem


