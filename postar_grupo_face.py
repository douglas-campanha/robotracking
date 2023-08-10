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
     #vai até a página do grupo
     pagina.goto('https://www.facebook.com/groups/228701739782644')
     time.sleep(3)
     #clica na barra de publicação do grupo
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div').click()
     time.sleep(3)
     #clica nao input da modal de post
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div').click()
     time.sleep(3)
     #preenche o campo com a frase a ser postada
     pagina.fill('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div', "Frase da postagem, https://campanhadigital.net.br")
     time.sleep(3)
     #clica no botão de postar
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div[1]/div').click()
     time.sleep(3)



     #clica no botão para postar foto ou vídeo
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/div/div[2]').click()
     time.sleep(3)



     
     #clica na foto do perfil para deslogar da conta
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/span/div/div[1]/div').click()
     time.sleep(3)

     #desloga do Facebook
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[6]/div/div[2]').click()
     #loga novamente como avatar
     pagina.goto("https://facebook.com")
     time.sleep(3)
     #preenche a campo email
     pagina.fill('xpath=//*[@id="email"]', "santanathiagosantos00@gmail.com")
     time.sleep(3)
     #preenche o campo senha
     pagina.fill('xpath=//*[@id="pass"]', "santana2022")
     time.sleep(3)
     #clica no botão entrar
     pagina.locator('xpath=/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
     time.sleep(3)
     #acessa outro grupo
     pagina.goto('https://www.facebook.com/groups/228701739782644')
     time.sleep(3)
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div').click()
     time.sleep(3)
     #clica nao input da modal de post
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div').click()
     time.sleep(3)
     #preenche o campo com a frase a ser postada
     pagina.fill('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div', "Frase da postagem com Avatar Tiago Alves Santana, https://vitrinedogoverno.com.br")
     time.sleep(3)
     #clica no botão de postar
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div[1]/div').click()
     time.sleep(3)
     #clica na foto do perfil para deslogar da conta
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/span/div/div[1]/div').click()
     time.sleep(3)
     #loga novamente com o segundo avatar
     pagina.goto("https://facebook.com")
     time.sleep(3)
     #preenche a campo email
     pagina.fill('xpath=//*[@id="email"]', "teresagouveia1969@gmail.com")
     time.sleep(3)
     #preenche o campo senha
     pagina.fill('xpath=//*[@id="pass"]', "Campanha123")
     time.sleep(3)
     #clica no botão entrar
     pagina.locator('xpath=/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
     time.sleep(3)
     pagina.goto('https://www.facebook.com/groups/228701739782644')
     time.sleep(3)
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div').click()
     time.sleep(3)
     #clica nao input da modal de post
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div').click()
     time.sleep(3)
     #preenche o campo com a frase a ser postada
     pagina.fill('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div', "Frase da postagem com Avatar Teresa Gouveia")
     time.sleep(3)
     #clica no botão de postar
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div[1]/div').click()
     time.sleep(3)
     #clica na foto do perfil para deslogar da conta
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/span/div/div[1]/div').click()
     time.sleep(3)
     time.sleep(300)
