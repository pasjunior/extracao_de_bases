import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import glob
import pySmartDL
import tkinter as tk
from tkinter import filedialog

def realizar_extracao_SACTK(url, caminho_exportacao, login, senha, data_inicial, data_final):
    # Configurar as opções do Chrome
    chrome_options = Options()
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
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='lgusuario']").send_keys(login)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='lgsenha']").send_keys(senha)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='lbtn']").click()

        # Navegar para a página de exportação
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='main']/table[1]/tbody/tr/td[2]/div/div[2]/div/b").click()  #  //*[@id="main"]/table[1]/tbody/tr/td[2]/div/div[2]/div/b
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='main']/div/button/span").click()

        # Preencher datas de filtro
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='data1']").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='data1']").send_keys(data_inicial)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='hora1']").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='hora1']").send_keys("00:00")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='data2']").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='data2']").send_keys(data_final)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='hora2']").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='hora2']").send_keys("23:59")

        # Clicar no botão de exportação
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='exportar-button']/span").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='ui-id-3']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='main']/div[5]/button/span").click()
        time.sleep(15)

        # Esperar o download ser concluído
        caminho_download = caminho_exportacao
        arquivo_exportado_padrao = os.path.join(caminho_download, "mens-*.csv")

        while True:
            arquivo_encontrado = glob.glob(arquivo_exportado_padrao)
            if arquivo_encontrado and arquivo_completo(arquivo_encontrado[0]):
                nome_arquivo = arquivo_encontrado[0]
                caminho_arquivo = os.path.join(caminho_download, nome_arquivo)

                # Usar pySmartDL para monitorar o progresso do download
                obj = pySmartDL.SmartDL(url, dest=caminho_arquivo)
                obj.start(blocking=False)

                # Aguardar até que o download seja concluído
                while not obj.isFinished():
                    time.sleep(1)

                # Renomear o arquivo baixado
                arquivo_renomeado = os.path.join(caminho_download, empresa + "-" + data_inicial + " a " + data_final + " TK.csv")
                os.rename(caminho_arquivo, arquivo_renomeado)
                print(f"Arquivo renomeado para: {os.path.basename(arquivo_renomeado)}")
                break
            time.sleep(1)

    finally:
        # Encerrar o driver do Chrome
        driver.quit()

def arquivo_completo(caminho_arquivo):
    """
    Verifica se o arquivo no caminho especificado está completamente baixado.
    Retorna True se o arquivo existe e não possui a extensão .crdownload, caso contrário, retorna False.
    """
    if os.path.exists(caminho_arquivo):
        return not caminho_arquivo.endswith(".crdownload")
    return False

# Abrir caixa de diálogo para o usuário escolher o diretório de exportação
root = tk.Tk()
root.withdraw()
caminho_exportacao = filedialog.askdirectory().replace("/", "\\")

# Variáveis globais
empresas = ["EAC", "EBO", "EMS", "EMT", "ENF", "EPB", "ERO", "ESE", "ESS", "ETO"] # ["EAC", "EBO", "EMG", "EMS", "EMT", "ENF", "EPB", "ERO", "ESE", "ESS", "ETO"]
login = "psouto" #input("Digite o login: ")
senha = "M*02052018h" # pwinput.pwinput(prompt='Digite sua senha: ')
data_inicial = "01.06.2023" #input("Digite a data inicial (formato dd.mm.aaaa): ")
data_final = "30.06.2023" #input("Digite a data final (formato dd.mm.aaaa): ")

for empresa in empresas:
    url = "https://webcorp.tww.com.br/energisa/" + empresa + "SACTK"
    print("AQUI", url)
    realizar_extracao_SACTK(url, caminho_exportacao, login, senha, data_inicial, data_final)
