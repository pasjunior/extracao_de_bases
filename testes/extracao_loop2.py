import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, re
import glob
import tkinter as tk
from tkinter import filedialog
import pwinput

def realizar_extracao_SACTK(url, caminho_exportacao, login, senha, data_inicial, data_final):
    # Configurar as opções do Chrome
    chrome_options = Options()
    #chrome_options.add_argument("--headless") # Executa o Chrome em modo headless, sem abrir uma janela do navegador
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": caminho_exportacao,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # Inicializar o driver do Chrome
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    base_url = url

    try:
        # Navegar para a URL
        driver.get(url)

        # Preencher informações de login
        driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").click()
        driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").clear()
        driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").send_keys(login)
        driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").clear()
        driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").send_keys(senha)
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id=\"lbtn\" or @class=\"ui-button ui-widget ui-state-default ui-corner-all ui-state-hover ui-state-focus\"]").click()

        # Navegar para a página de exportação
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id=\"main\"]/table[1]/tbody/tr/td[2]/div/div[2]/div").click()
        driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/button/span").click()

        # Preencher datas de filtro
        driver.find_element(By.XPATH, "//*[@id=\"data1\"]").click()
        driver.find_element(By.XPATH, "//*[@id=\"data1\"]").clear()
        driver.find_element(By.XPATH, "//*[@id=\"data1\"]").send_keys(data_inicial)
        driver.find_element(By.XPATH, "//*[@id=\"hora1\"]").clear()
        driver.find_element(By.XPATH, "//*[@id=\"hora1\"]").send_keys("00:00")
        driver.find_element(By.XPATH, "//*[@id=\"data2\"]").clear()
        driver.find_element(By.XPATH, "//*[@id=\"data2\"]").send_keys(data_final)
        driver.find_element(By.XPATH, "//*[@id=\"hora2\"]").clear()
        driver.find_element(By.XPATH, "//*[@id=\"hora2\"]").send_keys("23:59")

        # Clicar no botão de exportação
        driver.find_element(By.XPATH, "//*[@id=\"exportar-button\"]/span[2]").click()
        driver.find_element(By.XPATH, "//*[@id=\"ui-id-3\"]").click()
        driver.find_element(By.XPATH, "//*[@id=\"main\"]/div[5]/button/span").click() 
        time.sleep(10)
                
        # Esperar o download ser concluído
        caminho_download = caminho_exportacao
        arquivo_exportado_padrao = os.path.join(caminho_download, "mens-*.csv")
        arquivo_encontrado = glob.glob(arquivo_exportado_padrao)
        #wait = WebDriverWait(driver, 10)
        #wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '.csv')]")))
        if arquivo_encontrado:
            nome_arquivo = arquivo_encontrado[0]
            caminho_arquivo = os.path.join(caminho_download, nome_arquivo)
            # while os.path.exists(os.path.join(caminho_download, "mens-*.csv.crdownload")):
            #   time.sleep(1)
                
            # Renomear o arquivo baixado
            if os.path.exists(caminho_arquivo):
                arquivo_renomeado = os.path.join(caminho_download, empresa + "-" + data_inicial + " a " + data_final + " TK.csv")
                os.rename(caminho_arquivo, arquivo_renomeado)
                print(f"Arquivo renomeado para: {os.path.basename(arquivo_renomeado)}")
            else:
                print("O arquivo não foi baixado com o nome especificado.")
        else:
            print("Nenhum arquivo foi encontrado para download.")

    finally:
        # Encerrar o driver do Chrome
        driver.quit()

# Abrir caixa de diálogo para o usuário escolher o diretório de exportação
root = tk.Tk()
root.withdraw()
caminho_exportacao = filedialog.askdirectory().replace("/", "\\")

# Variáveis globais
empresas = ["EAC", "EBO"] # "EAC", "EBO", "EMG", "EMS", "EMT", "ENF", "EPB", "ERO", "ESE", "ESS", "ETO"]
login = "psouto" #input("Digite o login: ")
senha = "M*02052018h" # pwinput.pwinput(prompt='Digite sua senha: ')
data_inicial = "01.06.2023" #input("Digite a data inicial (formato dd.mm.aaaa): ")
data_final = "30.06.2023" #input("Digite a data final (formato dd.mm.aaaa): ")
#sleep = 15 # APAGAR DEPOIS DE AJUSTAR

for empresa in empresas:
    url = "https://webcorp.tww.com.br/energisa/" + empresa + "SAC"
    print("AQUI", url)
    realizar_extracao_SACTK(url, caminho_exportacao, login, senha, data_inicial, data_final)