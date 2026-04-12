import requests

url_marcas = "https://parallelum.com.br/fipe/api/v1/carros/marcas"
marcas = requests.get(url_marcas).json()

marca_id = None

for marca in marcas:
    if marca["nome"].lower() == "honda":
        marca_id = marca["codigo"]

url_modelos = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca_id}/modelos"
modelos = requests.get(url_modelos).json()["modelos"]

lista = []

for modelo in modelos[:15]:  
    nome = modelo["nome"]
    lista.append(nome)

with open("fipe_carros.txt", "w", encoding="utf-8") as f:
    for item in lista:
        f.write(item + "\n")

print("Arquivo gerado")