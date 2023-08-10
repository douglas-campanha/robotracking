from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import time
import PySimpleGUIWeb as sg

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
     #vai até a página do grupo 1
     pagina.goto('https://www.facebook.com/groups/228701739782644')
     time.sleep(3)
     #clica na barra de publicação do grupo
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div').click()
     time.sleep(3)
     #clica no input da modal de post
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div').click()
     time.sleep(3)
     #preenche o campo com a frase a ser postada
     pagina.fill('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div', "Frase da postagem, https://www.facebook.com/reel/220013200818277")
     time.sleep(3)
     #clica no botão de postar
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div[1]/div').click()
     time.sleep(3)
     #vai até a página do grupo 2
     pagina.goto('https://www.facebook.com/groups/786826446415081/')
     time.sleep(3)
     #clica na barra de publicação do grupo
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div').click()
     time.sleep(3)
     #clica no input da modal de post
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div').click()
     time.sleep(3)
     #preenche o campo com a frase a ser postada
     pagina.fill('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div', "Frase da postagem, https://www.facebook.com/reel/220013200818277")
     time.sleep(3)
     #clica no botão de postar
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div[1]/div').click()
     time.sleep(3)
     #vai até a página do grupo 2
     pagina.goto('https://www.facebook.com/groups/269032155774915/')
     time.sleep(3)
     #clica na barra de publicação do grupo
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div').click()
     time.sleep(3)
     #clica no input da modal de post
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div').click()
     time.sleep(3)
     #preenche o campo com a frase a ser postada
     pagina.fill('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div', "Frase da postagem, https://www.facebook.com/reel/220013200818277")
     time.sleep(3)
     #clica no botão de postar
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div[1]/div').click()
     time.sleep(3)
     #vai até a página do grupo 3
     pagina.goto('https://www.facebook.com/groups/178473068402619/')
     time.sleep(3)
     #clica na barra de publicação do grupo
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div').click()
     time.sleep(3)
     #clica no input da modal de post
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div').click()
     time.sleep(3)
     #preenche o campo com a frase a ser postada
     pagina.fill('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div', "Frase da postagem, https://www.facebook.com/reel/220013200818277")
     time.sleep(3)
     #clica no botão de postar
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div[1]/div').click()
     time.sleep(3)
     #vai até a página do grupo 3
     pagina.goto('https://www.facebook.com/groups/227686793517410/')
     time.sleep(3)
     #clica na barra de publicação do grupo
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div').click()
     time.sleep(3)
     #clica no input da modal de post
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div').click()
     time.sleep(3)
     #preenche o campo com a frase a ser postada
     pagina.fill('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div', "Frase da postagem, https://www.facebook.com/reel/220013200818277")
     time.sleep(3)
     #clica no botão de postar
     pagina.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div[1]/div').click()
     time.sleep(300)
