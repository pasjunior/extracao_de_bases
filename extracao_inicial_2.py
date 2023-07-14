# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, re
import glob
import tkinter as tk
from tkinter import filedialog
import pwinput

def realizar_extracao(url, caminho_exportacao, login, senha, data_inicial, data_final):
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
    driver.implicitly_wait(10)
    base_url = url

    try:
        # Navegar para a URL
        driver.get(url)

        # Preencher informações de login
        driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").click()
        driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").send_keys(login)
        driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").send_keys(senha)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id=\"lbtn\" or @class=\"ui-button ui-widget ui-state-default ui-corner-all ui-state-hover ui-state-focus\"]").click()

        # Navegar para a página de exportação
        time.sleep(1)
        elemento_1 = False
        while not elemento_1:
            try:
                print("Elemento_1")
                driver.find_element(By.XPATH, "//*[@id=\"main\"]/table/tbody/tr/td[2]/div/div[2]/div").click()
                elemento_1 = True
            except:
                driver = webdriver.Chrome(options=chrome_options)
                driver.implicitly_wait(10)
                base_url = url
                driver.get(url)
                driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").click()
                driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").clear()
                time.sleep(1)
                driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").send_keys(login)
                driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").clear()
                time.sleep(1)
                driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").send_keys(senha)
                time.sleep(3)
                driver.find_element(By.XPATH, "//*[@id=\"lbtn\" or @class=\"ui-button ui-widget ui-state-default ui-corner-all ui-state-hover ui-state-focus\"]").click() # Login
                time.sleep(1)
                
        elemento_2 = False
        while not elemento_2:
            try:
                print("Elemento_2")
                driver.find_element(By.XPATH, '//*[@id="main"]/div/button/span').click() # Relatório
                elemento_2 = True
            except:
                driver = webdriver.Chrome(options=chrome_options)
                driver.implicitly_wait(10)
                base_url = url
                driver.get(url)
                driver.find_element(By.XPATH, '//*[@id="lgusuario"]').click()
                driver.find_element(By.XPATH, '//*[@id="lgusuario"]').clear()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="lgusuario"]').send_keys(login)
                driver.find_element(By.XPATH, '//*[@id="lgsenha"]').clear()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="lgsenha"]').send_keys(senha)
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="lbtn" or @class="ui-button ui-widget ui-state-default ui-corner-all ui-state-hover ui-state-focus"]').click() # Login
                time.sleep(5)

            elemento_3 = False
            while not elemento_3:
                try:
                    print("Elemento_3")
                    driver.find_element(By.XPATH, '//*[@id="main"]/table/tbody/tr/td[2]/div/div[2]/div').click()
                    elemento_3 =True
                except:
                    driver = webdriver.Chrome(options=chrome_options)
                    driver.implicitly_wait(10)
                    base_url = url
                    driver.get(url)
                    driver.find_element(By.XPATH, '//*[@id="lgusuario"]').click()
                    driver.find_element(By.XPATH, '//*[@id="lgusuario"]').clear()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="lgusuario"]').send_keys(login)
                    driver.find_element(By.XPATH, '//*[@id="lgsenha"]').clear()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="lgsenha"]').send_keys(senha)
                    time.sleep(3)
                    driver.find_element(By.XPATH, '//*[@id="lbtn" or @class="ui-button ui-widget ui-state-default ui-corner-all ui-state-hover ui-state-focus"]').click()
                    time.sleep(1)
                    
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/button/span").click()  # //*[@id="usercont2"]/a[4]/div

        # Preencher datas de filtro
        driver.find_element(By.XPATH, "//*[@id=\"data1\"]").click()
        driver.find_element(By.XPATH, "//*[@id=\"data1\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"data1\"]").send_keys(data_inicial)
        driver.find_element(By.XPATH, "//*[@id=\"hora1\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"hora1\"]").send_keys("00:00")
        driver.find_element(By.XPATH, "//*[@id=\"data2\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"data2\"]").send_keys(data_final)
        driver.find_element(By.XPATH, "//*[@id=\"hora2\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"hora2\"]").send_keys("23:59") 

        # Clicar no botão de exportação
        driver.find_element(By.XPATH, "//*[@id=\"exportar-button\"]/span[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"ui-id-3\"]").click()
        driver.find_element(By.XPATH, "//*[@id=\"main\"]/div[5]/button/span").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id=\"usercont2\"]/a[4]/div").click()
        time.sleep(3)


        # Esperar o download ser concluído (aguardar até 20 segundos)
        download_path = caminho_exportacao
        arquivo_exportado_padrao = os.path.join(download_path, "mens-*.csv")
        arquivo_encontrado = glob.glob(arquivo_exportado_padrao)
        if arquivo_encontrado:
            file_name = arquivo_encontrado[0]
            file_path = os.path.join(download_path, file_name)
            wait_time = 0
            while not os.path.exists(file_path) and wait_time < 20:
                time.sleep(1)
                wait_time += 1

            # Renomear o arquivo baixado
            if os.path.exists(file_path):
                arquivo_renomeado = os.path.join(download_path, empresa + "-" + data_inicial + " a " + data_final + " TK.csv")
                os.rename(file_path, arquivo_renomeado)
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
empresas = ["EAC", "EBO", "EMG", "EMS", "EMT", "ENF", "EPB", "ERO", "ESE", "ESS", "ETO"] # ["EAC", "EBO", "EMG", "EMS", "EMT", "ENF", "EPB", "ERO", "ESE", "ESS", "ETO"]
login = "psouto" #input("Digite o login: ")
senha = "M*02052018h" # pwinput.pwinput(prompt='Digite sua senha: ')
data_inicial = "01.06.2023" #input("Digite a data inicial (formato dd.mm.aaaa): ")
data_final = "30.06.2023" #input("Digite a data final (formato dd.mm.aaaa): ")

for empresa in empresas:
    url = "https://webcorp.tww.com.br/energisa/" + empresa + "SACTK"
    print("ENDEREÇO: ", url)
    realizar_extracao(url, caminho_exportacao, login, senha, data_inicial, data_final)
