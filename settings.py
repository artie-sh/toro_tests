#!/usr/bin/python
# encoding: utf-8


#settings document is used to conveniently store the more static data, such as URL to test, locations, allowed chars, etc.
# in test then just referring to the values from settings

#url from which the test starts
base_url = 'https://da3bfafd542957fc5510b97bc0fdb3c7d2f826ca-www.googledrive.com/host/0ByzZ1BtGk-YcNUFQdzBRTF9IeEU/'

#folder for storing reports. inside reports folder, the new folder corresponding with the current date will be
# created where the actual testing reports will be saved.
reports_storage = './reports'
chrome_driver_location = './chromedriver'

#allowed chars from which each time new user name, pass, etc. are generated
# this will guarantee that our test will be unique each time and sometimes this
# randomly generated user data can disclose some unexpected hiden bugs
name_allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password_allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=\'?'
comment_allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=\'? '

comment_length = 20

#distionary for saving generated user data in order to attach to the report as a test evidence
registration_data = {
    'user_name': '',
    'password': '',
    'color': '',
    'gender': '',
    'comment': ''
}

#data for automated email notification
toro_email = 'toro.qa.automation@gmail.com'
toro_pass = '0905wrbn'
email_noification_recipients_list  = ('sinnlos@rambler.ru', 'artie.sh.87@gmail.com')
SMTP_server = 'smtp.gmail.com:587'