# -*- coding: utf-8 -*-
"""
    task.controllers.redis_pubsub
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2014 by Abhinav Singh.
    :license: BSD, see LICENSE for more details.
"""
import time
import redis


def redis_pubsub(t, channel):
    r = redis.StrictRedis()

    p = r.pubsub()
    p.subscribe(channel)

    for data in p.listen():
        if 'type' in data and data['type'] == 'message':
            t.send(data)
            # sleep required for t.done to set appropriately
            # TODO: use non-blocking listen and eliminate need of sleep
            time.sleep(0.1)
            if t.done:
                p.unsubscribe(channel)
                break
