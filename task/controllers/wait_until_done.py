# -*- coding: utf-8 -*-
"""
    task.controllers.wait_until_done
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) 2013 by Abhinav Singh.
    :license: BSD, see LICENSE for more details.
"""
import time
from .base import base

@base
def wait_until_done(t, poll_every=0.1):
    while True:
        time.sleep(poll_every)
        if t.done:
            break
