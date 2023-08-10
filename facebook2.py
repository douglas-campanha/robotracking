from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import time

with sync_playwright() as p:
     navegador = p.chromium.launch(headless=False)
     pagina = navegador.new_page()
     #acessar Facebook
     pagina.goto("https://facebook.com")
     time.sleep(3)
     #preenche a campo email
     pagina.fill('xpath=//*[@id="email"]', "douglas@campanhadigital.net.br")
     time.sleep(3)
     #preenche o campo senha
     pagina.fill('xpath=//*[@id="pass"]', "x@#$234x")
     time.sleep(3)
     #clica no botão entrar
     pagina.locator('xpath=/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
     time.sleep(3)
     #preenche o campo de pesquisa com o termo
     pagina.fill('xpath=/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div[1]/div/div/label/input', "Campanha Digital")
     time.sleep(3)
     #aperta enter no teclado
     pagina.keyboard.press("Enter")
     time.sleep(3)
     pagina.screenshot(path="telaFacebook2.jpg", full_page=True)
     time.sleep(5)
     #clica no link da página oficial
     pagina.goto('https://www.facebook.com/CampanhaDigitalOficial')
     time.sleep(3)
     #clica no botão mensagem
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div').click()
     time.sleep(3)
     ##clica na área de input que precisa estar acionada para escrever a mensagem
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div').click()
     #escreve a mensagem
     pagina.fill('xpath=/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p', "Mensagem e ser enviada...")
     time.sleep(300)

