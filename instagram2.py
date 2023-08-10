from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import time

with sync_playwright() as p:
     navegador = p.chromium.launch(headless=False)
     pagina = navegador.new_page()
     #acessa o site do Instagram
     pagina.goto("https://instagram.com")
     time.sleep(3)
     #preenche o campo de email
     pagina.fill('//*[@id="loginForm"]/div/div[1]/div/label/input', "robo@robotracking.com.br")
     time.sleep(3)
     #preenche o campo de senha
     pagina.fill('//*[@id="loginForm"]/div/div[2]/div/label/input', "x@#$234x")
     time.sleep(3)
     #clica no botão entrar
     pagina.locator('xpath=//*[@id="loginForm"]/div/div[3]/button/div').click()
     time.sleep(3)
     #clica no "agora não"
     pagina.locator('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
     time.sleep(3)
     #clica no "agora não" mais uma vez
     pagina.locator('xpath=/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
     time.sleep(3)
     #clica em pesquisar
     pagina.locator('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]').click()
     time.sleep(3)
     #escre ev o termo a ser pesquisado
     pagina.fill('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input', "Campanha Digital")
     time.sleep(3)
     #aperta enter no teclado
     pagina.keyboard.press("Enter")
     time.sleep(3)
     #clica no primeiro termo encontrado
     pagina.locator('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div').click()
     time.sleep(3)
     #clica em enviar mensagem
     pagina.locator('xpath=/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div').click()
     time.sleep(500)
