# -*- coding: utf-8 -*-
"""
    task.controllers.redis_brpop
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2014 by Abhinav Singh.
    :license: BSD, see LICENSE for more details.
"""
import redis


def redis_brpop(t, key, timeout=1):
    '''`Task` controller thats polls a redis key and sends received data to underlying task callable.'''
    r = redis.StrictRedis()

    while True:
        if t.done:
            break

        data = r.brpop(key, timeout=timeout)
        if data:
            t.send(data)
