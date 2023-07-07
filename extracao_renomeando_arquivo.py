# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time
import glob

# Variáveis
empresas = "EAC" # EBO, EMG, EMS, EMT, ENF, EPB, ERO, ESE, ESS, ETO]
login = input("Digita o login: ")
senha = input("Digita a senha: ")
url = "https://webcorp.tww.com.br/energisa/" + empresas +"SACTK"
caminho_exportacao = r"C:\Users\paulo\OneDrive\Área de Trabalho\DIEC\extracao_de_bases SMS\arquivos"
data_inicial = "01.06.2023"
data_final = "30.06.2023"
arquivo_exportado_padrao = caminho_exportacao + r"\mens-*.csv"
arquivo_encontrado = ""
arquivo_renomeado = empresas + "-" + data_inicial + " a " + data_final + ".csv"

class TransactionScriptPy(unittest.TestCase):
    def setUp(self):
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
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(30)
        self.base_url = url
        
    def test_transaction_script_py(self):
        self.driver.get(url)
        self.driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").clear()
        self.driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").send_keys(login)
        self.driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").clear()
        self.driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").send_keys(senha)
        self.driver.find_element(By.XPATH, "//*[@id=\"lbtn\" or @class=\"ui-button ui-widget ui-state-default ui-corner-all ui-state-hover ui-state-focus\"]").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"main\"]/table/tbody/tr/td[2]/div/div[2]/div").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/button/span").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"data1\"]").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"data1\"]").clear()
        self.driver.find_element(By.XPATH, "//*[@id=\"data1\"]").send_keys(data_inicial)
        self.driver.find_element(By.XPATH, "//*[@id=\"hora1\"]").clear()
        self.driver.find_element(By.XPATH, "//*[@id=\"hora1\"]").send_keys("00:00")
        self.driver.find_element(By.XPATH, "//*[@id=\"data2\"]").clear()
        self.driver.find_element(By.XPATH, "//*[@id=\"data2\"]").send_keys(data_final)
        self.driver.find_element(By.XPATH, "//*[@id=\"hora2\"]").clear()
        self.driver.find_element(By.XPATH, "//*[@id=\"hora2\"]").send_keys("23:59")
        
        # Clicar no botão de exportação
        self.driver.find_element(By.XPATH, "//*[@id=\"exportar-button\"]/span[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"ui-id-3\"]").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"main\"]/div[5]/button/span").click()
        time.sleep(5)
        
        # Esperar o download ser concluído (aguardar até 20 segundos)
        download_path = caminho_exportacao
        arquivo_encontrado = glob.glob(arquivo_exportado_padrao)
        file_name = arquivo_encontrado[0]
        file_path = os.path.join(download_path, file_name)
        wait_time = 0
        while not os.path.exists(file_path) and wait_time < 20:
            time.sleep(1)
            wait_time += 1
        
        # Renomear o arquivo baixado
        if os.path.exists(file_path):
            new_file_name = arquivo_renomeado
            new_file_path = os.path.join(download_path, new_file_name)
            os.rename(file_path, new_file_path)
            print(f"Arquivo renomeado para: {new_file_name}")
        else:
            print("O arquivo não foi baixado com o nome especificado.")
        
        # Continuar com as etapas restantes do teste       
        
        self.driver.find_element(By.XPATH, "//*[@id=\"usercont2\"]/a[4]/div").click() 
    
    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main()
