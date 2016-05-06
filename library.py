#!/usr/bin/python
# encoding: utf-8

import time
import os
import settings
import random


def get_date():
    return str(time.strftime('%Y.%m.%d'))


def get_time():
    return str(time.strftime('%H:%M:%S'))


#print ''.join(random.choice(settings.name_allowed_chars) for x in range(settings.name_minimal_length))