#!/usr/bin/python
# encoding: utf-8

import time
import shutil
import settings
import library
import os
import unittest
import pyscreenshot as screen

class Report:

    def __init__(self, test_name):
        self._test_name = test_name
        self._reporting_folder = settings.reports_storage + '/' + library.get_date() + '/'
        self._screenshot_folder = self._reporting_folder + self._test_name + '/'

        if not os.path.isdir(self._reporting_folder):
            os.mkdir(self._reporting_folder)
        if os.path.isdir(self._screenshot_folder):
            shutil.rmtree(self._screenshot_folder)
        os.mkdir(self._screenshot_folder)

        self.__report = open(self._reporting_folder + self._test_name + '.htm', 'w')
        self.__report.write('<html>\n <body> \n')

    def add_screen(self, screen_text = ''):
        screen_name = library.get_date() + '_' + library.get_time() + '_' + screen_text.strip().replace(' ', '_') + '.png'
        screen.grab_to_file(self._screenshot_folder + screen_name)
        self.__report.write("<a href ='" + self._test_name + "/" + screen_name + "' target='_blank'><img src='" + self._test_name + "/" + screen_name + "' width=50%></a>\n<p>\n" + screen_text + "\n<br>\n<br>\n")


    def close(self):
        self.__report.write('</body>\n</html>')
        self.__report.close()

if __name__ == "__main__":
    unittest.main()