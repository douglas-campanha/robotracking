from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
     navegador = p.chromium.launch(headless=False)
     pagina = navegador.new_page()
     pagina.goto("https://twitter.com/i/flow/login/")
     pagina.fill('xpath=//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input', "douglas@campanhadigital.net.br")
     pagina.locator('xpath=//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
     pagina.fill('xpath=//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input', "x@#$234x")
     pagina.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
     pagina.goto('https://twitter.com/search?q=sou%20pr%C3%A9%20canditato%20a%20prefeito&src=typed_query')
     pagina.locator('xpath=//*[@id="id__9ydrlwhx8g"]/div[1]/div/div/div[1]').click()
     pagina.keyboard.down("Enter")
     time.sleep(10)
     pagina.screenshot(path="telaTwitter.jpg", full_page=True)
