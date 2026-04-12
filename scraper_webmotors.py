from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Configuração do Edge
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Edge(
    service=Service(EdgeChromiumDriverManager().install()),
    options=options
)

url = "https://www.webmotors.com.br/carros-usados/sp"
driver.get(url)

# Espera os elementos carregarem (melhor que time.sleep)
wait = WebDriverWait(driver, 15)

carros = wait.until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "h2"))
)

dados = []

for carro in carros[:10]:
    texto = carro.text.strip()
    if texto:  # evita itens vazios
        dados.append([texto])

driver.quit()

# Salvar CSV
with open("carros.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["titulo"])
    writer.writerows(dados)

print("Funcionou!")