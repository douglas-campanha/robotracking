import requests
from bs4 import BeautifulSoup

link = "https://www.facebook.com/prefeituramunicipaltaubate"
requisicao = requests.get(link)
print(requisicao)
site = BeautifulSoup(requisicao.text, "html.parser")
titulo = site.find("title")

