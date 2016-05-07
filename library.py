#!/usr/bin/python
# encoding: utf-8

import time
import os
import settings
import random
from lxml import etree
from selenium import webdriver


def get_date():
    return str(time.strftime('%Y.%m.%d'))


def get_time():
    return str(time.strftime('%H:%M:%S'))



'''
driver = webdriver.Chrome(settings.chrome_driver_location)
driver.maximize_window()
driver.get(settings.base_url)

page_source = etree.HTML(driver.page_source)

gender_inputs = driver.find_elements_by_xpath("//input[contains(@name, 'genderinput')]")

for item in gender_inputs:
    print item
    print item.get_attribute('innerHTML')
'''