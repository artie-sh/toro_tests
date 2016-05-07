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
        self.__test_start_time = time.time()
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
        self.__report.write('%s %s: %s started<p>\n\n' % (library.get_date(), library.get_time(), test_name))

    def add_screen(self, screen_text = ''):
        screen_name = library.get_date() + '_' + library.get_time() + '_' + screen_text.strip().replace(' ', '_') + '.png'
        screen.grab_to_file(self._screenshot_folder + screen_name)
        self.__report.write("<a href ='" + self._test_name + "/" + screen_name + "' target='_blank'><img src='" + self._test_name + "/" + screen_name + "' width=50%></a>\n<p>\n" + screen_text + "\n<p>\n<br>\n")


    def add_comment(self, comment):
        self.__report.write('%s %s %s<p>\n\n' % (library.get_date(), library.get_time(), comment))


    def add_user_data(self, user_data):
        self.__report.write("User Data:<p>\n")
        self.__report.write("<table border=1>\n")
        self.__report.write("<tr><td>User Name</td><td>" + user_data['user_name'] + "</td></tr>\n")
        self.__report.write("<tr><td>Password</td><td>" + user_data['password'] + "</td></tr>\n")
        self.__report.write("<tr><td>Color</td><td>" + user_data['color'] + "</td></tr>\n")
        self.__report.write("<tr><td>Gender</td><td>" + user_data['gender'] + "</td></tr>\n")
        self.__report.write("<tr><td>Comment</td><td>" + user_data['comment'] + "</td></tr>\n")
        self.__report.write("</table><p>\n\n")

    def close(self):
        self.__test_finish_time = time.time()
        self.__report.write('TOTAL DURATION %d minutes %d seconds<p>\n' % (int((self.__test_finish_time - self.__test_start_time)/60), self.__test_finish_time - self.__test_start_time - int((self.__test_finish_time - self.__test_start_time)/60)*60))
        self.__report.write('</body>\n</html>')
        self.__report.close()

if __name__ == "__main__":
    unittest.main()