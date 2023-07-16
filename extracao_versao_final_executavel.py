# python -m venv venv -> código para criar o ambiente virtual
# venv\Scripts\activate -> código para ativar o ambiente virtual
# pip install selenium
# pip install pySmartDL
# pip install pwinput
# pip install pyinstaller
# -*- coding: utf-8 -*-

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import glob
import pySmartDL
import sys

def realizar_extracao_SACTK(url, empresa, caminho_exportacao, login, senha, data_inicial, data_final):
    # Configurar as opções do Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Executa o Chrome em modo headless, sem abrir uma janela do navegador
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
        driver.get(base_url)

        # Preencher informações de login
        driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").click()
        driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").send_keys(login)
        driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").send_keys(senha)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"lbtn\" or @class=\"ui-button ui-widget ui-state-default ui-corner-all ui-state-hover ui-state-focus\"]").click() # Fazendo Login

        # Navegar para a página de exportação
        time.sleep(3)
        elemento_1 = False
        while not elemento_1:
            try:
                print("Elemento_1")
                driver.find_element(By.XPATH, "//*[@id=\"main\"]/table/tbody/tr/td[2]/div/div[2]/div").click()  # Relatório Completo
                elemento_1 = True
            except:
                driver = webdriver.Chrome(options=chrome_options)
                driver.implicitly_wait(10)
                base_url = url
                driver.get(base_url)
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
                driver.find_element(By.XPATH, '//*[@id="main"]/div/button/span').click() # Data
                elemento_2 = True
            except:
                driver = webdriver.Chrome(options=chrome_options)
                driver.implicitly_wait(10)
                base_url = url
                driver.get(base_url)
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
                        time.sleep(3)
                        driver.find_element(By.XPATH, '//*[@id="main"]/table/tbody/tr/td[2]/div/div[2]/div').click() # Relatório Completo
                        elemento_3 =True
                    except:
                        driver = webdriver.Chrome(options=chrome_options)
                        driver.implicitly_wait(10)
                        base_url = url
                        driver.get(base_url)
                        driver.find_element(By.XPATH, '//*[@id="lgusuario"]').click()
                        driver.find_element(By.XPATH, '//*[@id="lgusuario"]').clear()
                        time.sleep(1)
                        driver.find_element(By.XPATH, '//*[@id="lgusuario"]').send_keys(login)
                        driver.find_element(By.XPATH, '//*[@id="lgsenha"]').clear()
                        time.sleep(1)
                        driver.find_element(By.XPATH, '//*[@id="lgsenha"]').send_keys(senha)
                        time.sleep(3)
                        driver.find_element(By.XPATH, '//*[@id="lbtn" or @class="ui-button ui-widget ui-state-default ui-corner-all ui-state-hover ui-state-focus"]').click()  # Login
                        time.sleep(1)
                        
        #time.sleep(1)
        #driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/button/span").click()  # Data

        # Preencher datas de filtro
        driver.find_element(By.XPATH, "//*[@id=\"data1\"]").click()
        driver.find_element(By.XPATH, "//*[@id=\"data1\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"data1\"]").send_keys(data_inicial)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"hora1\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"hora1\"]").send_keys("00:00")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"data2\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"data2\"]").send_keys(data_final)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"hora2\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"hora2\"]").send_keys("23:59")
        time.sleep(1)

        # Clicar no botão de exportação
        driver.find_element(By.XPATH, "//*[@id=\"exportar-button\"]/span[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"ui-id-3\"]").click()
        driver.find_element(By.XPATH, "//*[@id=\"main\"]/div[5]/button/span").click()
        time.sleep(5)
        #driver.find_element(By.XPATH, "//*[@id=\"usercont2\"]/a[4]/div").click()  # BOTÃO PARA SIAR DO SITE
        #time.sleep(5)

        # Esperar o download ser concluído
        caminho_download = caminho_exportacao
        arquivo_exportado_padrao = os.path.join(caminho_download, "mens-*.csv")
        while True:
            arquivo_encontrado = glob.glob(arquivo_exportado_padrao)
            if arquivo_encontrado and arquivo_completo(arquivo_encontrado[0]):
                nome_arquivo = arquivo_encontrado[0]
                caminho_arquivo = os.path.join(caminho_download, nome_arquivo)
                '''
                wait_time = 0 # talvez excluir
                while not os.path.exists(caminho_arquivo) and wait_time < 20: # talvez excluir
                    time.sleep(1) # talvez excluir
                    wait_time += 1 # talvez excluir'''

                # Usar pySmartDL para monitorar o progresso do download
                obj = pySmartDL.SmartDL(url, dest=caminho_download)
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

def realizar_extracao_SAC(url, empresa, caminho_exportacao, login, senha, data_inicial, data_final):
    # Configurar as opções do Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Executa o Chrome em modo headless, sem abrir uma janela do navegador
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
        driver.get(base_url)

        # Preencher informações de login
        driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").click()
        driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").send_keys(login)
        driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").send_keys(senha)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"lbtn\" or @class=\"ui-button ui-widget ui-state-default ui-corner-all ui-state-hover ui-state-focus\"]").click() # Fazendo Login

        # Navegar para a página de exportação
        time.sleep(3)
        elemento_1 = False
        while not elemento_1:
            try:
                print("Elemento_1")
                driver.find_element(By.XPATH, "//*[@id=\"main\"]/table/tbody/tr/td[2]/div/div[2]/div").click()  # Relatório Completo
                elemento_1 = True
            except:
                driver = webdriver.Chrome(options=chrome_options)
                driver.implicitly_wait(10)
                base_url = url
                driver.get(base_url)
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
                driver.find_element(By.XPATH, '//*[@id="main"]/div/button/span').click() # Data
                elemento_2 = True
            except:
                driver = webdriver.Chrome(options=chrome_options)
                driver.implicitly_wait(10)
                base_url = url
                driver.get(base_url)
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
                        time.sleep(3)
                        driver.find_element(By.XPATH, '//*[@id="main"]/table/tbody/tr/td[2]/div/div[2]/div').click() # Relatório Completo
                        elemento_3 =True
                    except:
                        driver = webdriver.Chrome(options=chrome_options)
                        driver.implicitly_wait(10)
                        base_url = url
                        driver.get(base_url)
                        driver.find_element(By.XPATH, '//*[@id="lgusuario"]').click()
                        driver.find_element(By.XPATH, '//*[@id="lgusuario"]').clear()
                        time.sleep(1)
                        driver.find_element(By.XPATH, '//*[@id="lgusuario"]').send_keys(login)
                        driver.find_element(By.XPATH, '//*[@id="lgsenha"]').clear()
                        time.sleep(1)
                        driver.find_element(By.XPATH, '//*[@id="lgsenha"]').send_keys(senha)
                        time.sleep(3)
                        driver.find_element(By.XPATH, '//*[@id="lbtn" or @class="ui-button ui-widget ui-state-default ui-corner-all ui-state-hover ui-state-focus"]').click()  # Login
                        time.sleep(1)
                        
        #time.sleep(1)
        #driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/button/span").click()  # Data

        # Preencher datas de filtro
        driver.find_element(By.XPATH, "//*[@id=\"data1\"]").click()
        driver.find_element(By.XPATH, "//*[@id=\"data1\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"data1\"]").send_keys(data_inicial)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"hora1\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"hora1\"]").send_keys("00:00")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"data2\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"data2\"]").send_keys(data_final)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"hora2\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"hora2\"]").send_keys("23:59")
        time.sleep(1)

        # Clicar no botão de exportação
        driver.find_element(By.XPATH, "//*[@id=\"exportar-button\"]/span[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"ui-id-3\"]").click()
        driver.find_element(By.XPATH, "//*[@id=\"main\"]/div[5]/button/span").click()
        time.sleep(5)
        #driver.find_element(By.XPATH, "//*[@id=\"usercont2\"]/a[4]/div").click()  # BOTÃO PARA SIAR DO SITE
        #time.sleep(5)

        # Esperar o download ser concluído
        caminho_download = caminho_exportacao
        arquivo_exportado_padrao = os.path.join(caminho_download, "mens-*.csv")
        while True:
            arquivo_encontrado = glob.glob(arquivo_exportado_padrao)
            if arquivo_encontrado and arquivo_completo(arquivo_encontrado[0]):
                nome_arquivo = arquivo_encontrado[0]
                caminho_arquivo = os.path.join(caminho_download, nome_arquivo)
                
                # Usar pySmartDL para monitorar o progresso do download
                obj = pySmartDL.SmartDL(url, dest=caminho_download)
                obj.start(blocking=False)
                
                # Aguardar até que o download seja concluído
                while not obj.isFinished():
                    time.sleep(1)

                # Renomear o arquivo baixado
                arquivo_renomeado = os.path.join(caminho_download, empresa + "-" + data_inicial + " a " + data_final + ".csv")
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

def excluir_arquivos_nao_csv(caminho_exportacao):
    for arquivo in os.listdir(caminho_exportacao):
        if not arquivo.lower().endswith('.csv'):
            caminho_arquivo = os.path.join(caminho_exportacao, arquivo)
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)
                #print(f"Arquivo excluído: {arquivo}")


def main(args):
    if len(args) < 6:
        print("Erro: Faltam argumentos. Uso: meu_script.py URL CAMINHO_EXPORTACAO LOGIN SENHA DATA_INICIAL DATA_FINAL")
        return

    url = args[0]
    caminho_exportacao = args[1]
    login = args[2]
    senha = args[3]
    data_inicial = args[4]
    data_final = args[5]

    empresas = ["EAC", "EBO", "EMS"]
    for empresa in empresas:
        url_sactk = url + empresa + "SACTK"
        print("ENDEREÇO: ", url_sactk)
        realizar_extracao_SACTK(url_sactk, empresa, caminho_exportacao, login, senha, data_inicial, data_final)

    for empresa in empresas:
        url_sac = url + empresa + "SAC"
        print("ENDEREÇO: ", url_sac)
        realizar_extracao_SAC(url_sac, empresa, caminho_exportacao, login, senha, data_inicial, data_final)

    excluir_arquivos_nao_csv(caminho_exportacao)
    print("Arquivos baixados no diretório:", caminho_exportacao)
    print("Processo encerrado!")

if __name__ == "__main__":
    main(sys.argv[1:])