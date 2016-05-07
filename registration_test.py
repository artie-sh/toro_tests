#!/usr/bin/python
# encoding: utf-8

import unittest
import settings
import random
from lxml import etree
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
        try:
            rep = self.rep
            driver = self.driver
            wait = WebDriverWait(driver, 10)
            driver.get(settings.base_url)
            reg_data = settings.registration_data


            wait.until(EC.visibility_of_element_located((By.XPATH,"//fieldset/legend[normalize-space(text())='Please enter data']")))
            assert EC.visibility_of_element_located((By.XPATH, "//button[contains(@type, 'submit') and contains(@class, 'disabled')]"))
            rep.add_screen('registration form open')

            page_source = etree.HTML(driver.page_source)

            minimal_name_length = int(page_source.xpath("//input[contains(@id, 'nameinput')]/@data-minlength")[0])
            minimal_pass_length = int(page_source.xpath("//input[contains(@id, 'passwordinput')]/@data-minlength")[0])


            name_field = driver.find_element_by_id('nameinput')
            reg_data['user_name'] = ''.join(random.choice(settings.name_allowed_chars) for x in range(minimal_name_length-1))
            name_field.send_keys(reg_data['user_name'])
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id, 'nameinput')]/../../../div[contains(@class, 'form-group') and contains(@class, 'has-error')]")))
            rep.add_screen('short name filled in')


            reg_data['user_name'] += random.choice(settings.name_allowed_chars)
            name_field.send_keys(reg_data['user_name'][-1:])
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id, 'nameinput')]/../../../div[contains(@class, 'form-group') and not(contains(@class, 'has-error'))]")))
            rep.add_screen('valid name filled in')


            password_field = driver.find_element_by_id('passwordinput')
            reg_data['password'] = ''.join(random.choice(settings.password_allowed_chars) for x in range(minimal_pass_length-1))
            password_field.send_keys(reg_data['password'])
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id, 'passwordinput')]/../../../div[contains(@class, 'form-group') and contains(@class, 'has-error')]")))
            rep.add_screen('short pass filled in')


            reg_data['password'] += random.choice(settings.password_allowed_chars)
            password_field.send_keys(reg_data['password'][-1:])
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id, 'passwordinput')]/../../../div[contains(@class, 'form-group') and not(contains(@class, 'has-error'))]")))
            rep.add_screen('valid pass filled in')


            random_color = random.randint(2,4)
            color_option = driver.find_element_by_xpath("//select[contains(@id, 'colorinput')]/option[%d]" % (random_color))
            color_option.click()
            reg_data['color'] = page_source.xpath("//select[contains(@id, 'colorinput')]/option[%d]/text()" % (random_color))[0]
            rep.add_screen('color picked')


            random_gender = random.randint(1,2)
            gender_option = driver.find_element_by_xpath("//label[contains(@class, 'radio-inline')][%d]/input" % (random_gender))
            gender_option.click()
            reg_data['gender'] = page_source.xpath("//label[contains(@class, 'radio-inline')][%d]/input/@value" % (random_gender))[0]
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@type, 'submit') and not(contains(@class, 'disabled'))]")))
            rep.add_screen('gender selected, submit button active')


            comment_field = driver.find_element_by_xpath("//textarea[contains(@id, 'textarea')]")
            reg_data['comment'] = ''.join(random.choice(settings.comment_allowed_chars) for x in range(settings.comment_length))
            comment_field.send_keys(reg_data['comment'])
            rep.add_screen('comment filled in')


            submit_button = driver.find_element_by_xpath("//button[contains(@type, 'submit')]")
            submit_button.click()

            wait.until(EC.visibility_of_element_located((By.XPATH,"//h1[text() = 'Success']")))
            rep.add_screen('success screen shown')

            rep.add_comment('<big>SUCCESS</big>')

        except:
            rep.add_screen('exception call')
            rep.add_comment('<big>FAIL</big>')

        finally:
            rep.add_user_data(reg_data)


    def tearDown(self):
        self.driver.close()
        self.rep.close()


if __name__ == "__main__":
    unittest.main()