#!/usr/bin/python
# encoding: utf-8

import time
import smtplib
import settings


def get_date():
    return str(time.strftime('%Y.%m.%d'))

def get_time():
    return str(time.strftime('%H:%M:%S'))

#function for sending email notification on test results
def send_report(email_report_message):

    try:
        sender = settings.toro_email
        password = settings.toro_pass
        recipients = settings.email_noification_recipients_list

        server = smtplib.SMTP(settings.SMTP_server)
        server.ehlo()
        server.starttls()
        server.login(sender,password)

        for recipient in recipients:
            msg = "\r\n".join([
            "From: Toro QA Support",
            "To: %s" % recipient,
            "Subject: Automated Test Status Update",
            "%s" % email_report_message
            ])
            server.sendmail(sender, recipient, msg)
    except:
        print 'Failed to send email notifications'
    finally:
        server.quit()





send_report('hi there hest')











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