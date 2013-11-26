# -*- coding: utf-8 -*-
"""
    task.controllers.redis_brpop
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) 2013 by Abhinav Singh.
    :license: BSD, see LICENSE for more details.
"""
import redis

def redis_brpop(t, key):
    r = redis.StrictRedis()
    
    while True:
        if t.done:
            break
        
        try:
            data = r.brpop(key)
            t.send(data)
        except KeyboardInterrupt, _: # pragma: no cover
            break
        finally:
            t.stop()
    
    if t.exception:
        raise t.exception
    
    return t.result
