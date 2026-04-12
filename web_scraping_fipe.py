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

for modelo in modelos[:3]:
    modelo_id = modelo["codigo"]
    nome_modelo = modelo["nome"]

    url_anos = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca_id}/modelos/{modelo_id}/anos"
    anos = requests.get(url_anos).json()

    for ano in anos[:2]: 
        ano_id = ano["codigo"]

        url_valor = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca_id}/modelos/{modelo_id}/anos/{ano_id}"
        dados = requests.get(url_valor).json()

        nome = dados["Modelo"]
        ano_nome = dados["AnoModelo"]
        preco = dados["Valor"]

        lista.append(f"{nome} {ano_nome} - {preco}")

with open("fipe_precos.txt", "w", encoding="utf-8") as f:
    for item in lista:
        f.write(item + "\n")

print("Arquivo gerado")
