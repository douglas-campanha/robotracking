from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
     navegador = p.chromium.launch(headless=False)
     pagina = navegador.new_page()
     pagina.goto("https://www.linkedin.com/home/")
     pagina.fill('xpath=//*[@id="session_key"]', "douglas@campanhadigital.net.br")
     pagina.fill('xpath=//*[@id="session_password"]', "x@#$234x")
     pagina.locator('xpath=//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button').click()
     pagina.fill('xpath=//*[@id="global-nav-typeahead"]/input', "sou pré candidato a prefeito")
     pagina.keyboard.down("Enter")
     #pagina.locator('xpath=//*[@id="SFMkukraT/KdaciSLmY6RA=="]/div/ul[1]/li[3]/a').click()
     pagina.goto('https://www.linkedin.com/search/results/all/?keywords=sou%20pr%C3%A9%20candidato%20a%20prefeito&origin=SWITCH_SEARCH_VERTICAL&sid=x3y')
     pagina.locator('xpath=/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/div/ul[2]/li[1]/div/div/div[3]/div/div[2]/span[2]/span/div[1]/button').click()
     pagina.locator('xpath=//*[@id="ember371"]/div[2]/form/div/div/div[1]/div/div/div/div/div[1]/p').fill("teste")
     time.sleep(10)
     pagina.screenshot(path="telaLinkedin.jpg", full_page=True)
