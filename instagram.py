from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import time



with sync_playwright() as p:
     navegador = p.chromium.launch(headless=False)
     pagina = navegador.new_page()
     pagina.goto("https://www.instagram.com/")
     pagina.fill('xpath=//*[@id="loginForm"]/div/div[1]/div/label/input', "douglas@campanhadigital.net.br")
     pagina.fill('xpath=//*[@id="loginForm"]/div/div[2]/div/label/input', "x@#$234x")
     pagina.locator('xpath=//*[@id="loginForm"]/div/div[3]/button').click()
     pagina.locator('xpath=//*[@id="mount_0_0_bS"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div').click()

     pagina.screenshot(path="telaInstagram.jpg", full_page=True)
     pagina.locator('button:has-text("Comment"), button:has-text("Comment")').click()


     time.sleep(200)
