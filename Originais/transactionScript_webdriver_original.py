# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TransactionScriptPy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://change-this-to-the-site-you-are-testing/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_transaction_script_py(self):
        driver = self.driver
        driver.get("https://webcorp.tww.com.br/energisa/EACSACTK")
        driver.find_element_by_xpath("//*[@id=\"lgusuario\"]").click()
        driver.find_element_by_xpath("//*[@id=\"lgusuario\"], ").clear()
        driver.find_element_by_xpath("//*[@id=\"lgusuario\"], ").send_keys("")
        driver.find_element_by_xpath("//*[@id=\"lgsenha\"], ").clear()
        driver.find_element_by_xpath("//*[@id=\"lgsenha\"], ").send_keys("")
        driver.find_element_by_xpath("//*[@id=\"lbtn\" or @class=\"ui-button ui-widget ui-state-default ui-corner-all ui-state-hover ui-state-focus\"]").click()
        driver.find_element_by_xpath("//*[@id=\"main\"]/table/tbody/tr/td[2]/div/div[2]/div").click()
        driver.find_element_by_xpath("//*[@id=\"main\"]/div/button/span").click()
        driver.find_element_by_xpath("//*[@id=\"data1\"]").click()
        driver.find_element_by_xpath("//*[@id=\"data1\"], 01/06/2023").clear()
        driver.find_element_by_xpath("//*[@id=\"data1\"], 01/06/2023").send_keys("")
        driver.find_element_by_xpath("//*[@id=\"hora1\"], 00:00").clear()
        driver.find_element_by_xpath("//*[@id=\"hora1\"], 00:00").send_keys("")
        driver.find_element_by_xpath("//*[@id=\"data2\"], 30/06/2023").clear()
        driver.find_element_by_xpath("//*[@id=\"data2\"], 30/06/2023").send_keys("")
        driver.find_element_by_xpath("//*[@id=\"hora2\"], 23:59").clear()
        driver.find_element_by_xpath("//*[@id=\"hora2\"], 23:59").send_keys("")
        driver.find_element_by_xpath("//*[@id=\"exportar-button\"]/span[2]").click()
        driver.find_element_by_xpath("//*[@id=\"ui-id-17\" or text()=\"Exportar: CSV\"]").click()
        driver.find_element_by_xpath("//*[text()=\"Gerar\"]").click()
        driver.find_element_by_xpath("//*[@id=\"usercont2\"]/a[4]/div").click()
    
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
