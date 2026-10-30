import time
import requests
from bs4 import BeautifulSoup

# armazena o site numa variável
site = "https://www.dicio.com.br/"

# cores para uso em textos 
CIANO = "\033[36m"
RESET = "\033[0m"
ROXO = "\033[35m"
AZUL = "\033[34m"

print("📚 Dicionário\n")

# inicia um cronômetro
inicio = time.perf_counter()

# faz o loop principal
dicio = True
while dicio:
    # pede ao usuário que digite uma palavra
    palavra = input(ROXO + "Digite uma palavra: " + RESET)
    print("\n")
    # indica que está buscando a palavra digitada
    print(AZUL + "Buscando", palavra, "em", site + palavra + "/", "\n" + RESET)

    # faz um requests ao site armazenado 
    site1 = requests.get(site) 
    resultado = requests.get(site + palavra + "/")

    soup = BeautifulSoup(resultado.text, "html.parser")
    significado = soup.find("h2", class_="tit-significado")
    
    # imprime o resultado na tela
    for significados in soup.find_all("p", class_="significado"):
        if significados:
            print(significado.text, "\n")
            print(significados.text, "\n")
        else:
            print("Palavra não encontrada. ")

fim = time.perf_counter()

# contabiliza quantos segundos a pesquisa levou para ser executada, impreme e volta ao loop principal
tempo_total = fim - inicio

print("Essa pesquisa levou", tempo_total, "segundos.")
