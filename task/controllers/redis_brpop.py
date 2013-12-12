# -*- coding: utf-8 -*-
"""
    task.controllers.redis_brpop
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) 2013 by Abhinav Singh.
    :license: BSD, see LICENSE for more details.
"""
import redis
from .base import base

@base
def redis_brpop(t, key):
    r = redis.StrictRedis()
    while True:
        if t.done:
            break
        data = r.brpop(key)
        t.send(data)
