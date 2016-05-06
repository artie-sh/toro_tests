#!/usr/bin/python
# encoding: utf-8

import unittest
import settings
import random
from report import Report
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(settings.chrome_driver_location)
        self.driver.maximize_window()
        self.rep = Report(self.__class__.__name__)



    def test_RegistrationFormTest(self):
        rep = self.rep
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.get(settings.base_url)

        if wait.until(EC.visibility_of_element_located((By.XPATH,'//fieldset/legend[normalize-space(text())="Please enter data"]'))):
            rep.add_screen('registration form open - PASS')
        else:
            rep.add_screen('registration form open - FAIL')

#        fieldset = driver.find_element_by_xpath('//fieldset')

        input_field = driver.find_element_by_id('nameinput')

        input_field.send_keys(''.join(random.choice(settings.name_allowed_chars) for x in range(settings.name_minimal_length-1)))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@id, 'nameinput')]/../../../div[contains(@class, 'form-group') and contains(@class, 'has-error')]")))
        rep.add_screen('short name filled in')

        input_field.send_keys(''.join(random.choice(settings.name_allowed_chars) for x in range(1)))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@id, 'nameinput')]/../../../div[contains(@class, 'form-group') and not(contains(@class, 'has-error'))]")))
        rep.add_screen('valid name filled in')

        password_field = driver.find_element_by_id('passwordinput')

        password_field.send_keys(''.join(random.choice(settings.password_allowed_chars) for x in range(settings.password_minimal_length-1)))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@id, 'passwordinput')]/../../../div[contains(@class, 'form-group') and contains(@class, 'has-error')]")))
        rep.add_screen('short pass filled in')

        password_field.send_keys(''.join(random.choice(settings.password_allowed_chars) for x in range(1)))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[contains(@id, 'passwordinput')]/../../../div[contains(@class, 'form-group') and not(contains(@class, 'has-error'))]")))
        rep.add_screen('valid pass filled in')



#    def tearDown(self):
#        self.driver.close()
#        self.rep.close()


if __name__ == "__main__":
    unittest.main()