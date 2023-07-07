# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time

''' CHROME FECHADO
class TransactionScriptPy(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Executa o Chrome em modo headless, sem abrir uma janela do navegador
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://change-this-to-the-site-you-are-testing/"
        self.verificationErrors = []
        self.accept_next_alert = True
'''

''' CHROME ABERTO
class TransactionScriptPy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://change-this-to-the-site-you-are-testing/"
        self.verificationErrors = []
        self.accept_next_alert = True'''

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
            "download.default_directory": r"C:\Users\paulo\Downloads",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://webcorp.tww.com.br/energisa/EACSACTK"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_transaction_script_py(self):
        self.driver.get("https://webcorp.tww.com.br/energisa/EACSACTK")
        self.driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").clear()
        self.driver.find_element(By.XPATH, "//*[@id=\"lgusuario\"]").send_keys("psouto")
        self.driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").clear()
        self.driver.find_element(By.XPATH, "//*[@id=\"lgsenha\"]").send_keys("M*02052018h")
        self.driver.find_element(By.XPATH, "//*[@id=\"lbtn\" or @class=\"ui-button ui-widget ui-state-default ui-corner-all ui-state-hover ui-state-focus\"]").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"main\"]/table/tbody/tr/td[2]/div/div[2]/div").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/button/span").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"data1\"]").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"data1\"]").clear()
        self.driver.find_element(By.XPATH, "//*[@id=\"data1\"]").send_keys("01/06/2023")
        self.driver.find_element(By.XPATH, "//*[@id=\"hora1\"]").clear()
        self.driver.find_element(By.XPATH, "//*[@id=\"hora1\"]").send_keys("00:00")
        self.driver.find_element(By.XPATH, "//*[@id=\"data2\"]").clear()
        self.driver.find_element(By.XPATH, "//*[@id=\"data2\"]").send_keys("30/06/2023")
        self.driver.find_element(By.XPATH, "//*[@id=\"hora2\"]").clear()
        self.driver.find_element(By.XPATH, "//*[@id=\"hora2\"]").send_keys("23:59")
        self.driver.find_element(By.XPATH, "//*[@id=\"exportar-button\"]/span[2]").click()
        self.driver.execute_script("arguments[0].setAttribute('download', 'EACTK.csv');", self.driver.find_element(By.XPATH, "//*[@id=\"ui-id-3\"]"))
        self.driver.find_element(By.XPATH, "//*[@id=\"ui-id-3\"]").click()
        self.driver.find_element(By.XPATH, "//*[@id=\"main\"]/div[5]/button/span").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id=\"usercont2\"]/a[4]/div").click() 
            
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()