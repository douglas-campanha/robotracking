from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import time



with sync_playwright() as p:
     navegador = p.chromium.launch(headless=False)
     pagina = navegador.new_page()
     pagina.goto("https://www.tiktok.com/login/phone-or-email?enter_from=homepage_hot&enter_method=click_top_bar&hide_close_btn=1&is_modal=1&lang=pt-BR&redirect_url=https%3A%2F%2Fwww.tiktok.com%2F&type=")
     pagina.locator('xpath=/html/body/div[1]/div/div[2]/div[1]/form/div[1]/a').click()
     time.sleep(5)
     pagina.fill('xpath=/html/body/div[1]/div/div[2]/div[1]/form/div[1]/input', "atendimento@campanhadigital.net.br")
     time.sleep(5)
     pagina.fill('xpath=//*[@id="loginContainer"]/div[1]/form/div[2]/div/input', "12345678")
     time.sleep(5)
     pagina.locator('xpath=/html/body/div[1]/div/div[2]/div[1]/form/button').click()
     pagina.screenshot(path="telaTikTok.jpg", full_page=True)
     pagina.locator('button:has-text("Comment"), button:has-text("Comment")').click()


     time.sleep(20)
