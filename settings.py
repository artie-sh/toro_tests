#!/usr/bin/python
# encoding: utf-8



base_url = 'https://da3bfafd542957fc5510b97bc0fdb3c7d2f826ca-www.googledrive.com/host/0ByzZ1BtGk-YcNUFQdzBRTF9IeEU/'


reports_storage = './reports'
chrome_driver_location = './chromedriver'

name_allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password_allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=\'?'
comment_allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=\'? '

comment_length = 20

registration_data = {
    'user_name': '',
    'password': '',
    'color': '',
    'gender': '',
    'comment': ''
}