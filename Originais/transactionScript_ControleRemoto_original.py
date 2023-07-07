# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class TransactionScriptPy(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://change-this-to-the-site-you-are-testing/")
        self.selenium.start()
    
    def test_transaction_script_py(self):
        sel = self.selenium
        sel.open("https://webcorp.tww.com.br/energisa/EACSACTK")
        sel.click("//*[@id=\"lgusuario\"]")
        sel.type("//*[@id=\"lgusuario\"], ", "")
        sel.type("//*[@id=\"lgsenha\"], ", "")
        sel.click("//*[@id=\"lbtn\" or @class=\"ui-button ui-widget ui-state-default ui-corner-all ui-state-hover ui-state-focus\"]")
        sel.click("//*[@id=\"main\"]/table/tbody/tr/td[2]/div/div[2]/div")
        sel.click("//*[@id=\"main\"]/div/button/span")
        sel.click("//*[@id=\"data1\"]")
        sel.type("//*[@id=\"data1\"], 01/06/2023", "")
        sel.type("//*[@id=\"hora1\"], 00:00", "")
        sel.type("//*[@id=\"data2\"], 30/06/2023", "")
        sel.type("//*[@id=\"hora2\"], 23:59", "")
        sel.click("//*[@id=\"exportar-button\"]/span[2]")
        sel.click("//*[@id=\"ui-id-17\" or text()=\"Exportar: CSV\"]")
        sel.click("//*[text()=\"Gerar\"]")
        sel.click("//*[@id=\"usercont2\"]/a[4]/div")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
