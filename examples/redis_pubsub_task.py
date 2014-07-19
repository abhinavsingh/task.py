import sys
import redis

import Queue
from task import controller
from task.controllers import redis_pubsub


@controller(redis_pubsub, 'redis_pubsub')
def pubsub_task(t):
    ret = None
    while True:
        try:
            data = t.queue.get(timeout=0.1)
            ret = data['data']
            break
        except Queue.Empty:
            pass
    return ret

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print '** Starting pubsub_task, now pass data to this task by calling:'
        print '** $ python %s <data>' % sys.argv[0]
        print '** in another shell'
        print pubsub_task()
    else:
        r = redis.StrictRedis()
        print "sending data %s" % sys.argv[1]
        r.publish("redis_pubsub", sys.argv[1])
