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
