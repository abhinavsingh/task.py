import sys
import redis

import Queue
from task import controller
from task.controllers import redis_brpop


@controller(redis_brpop, 'redis_brpop')
def brpop_task(t):
    ret = None
    while not t.stopped():
        try:
            data = t.queue.get(timeout=0.1)
            ret = data[1]
            break
        except Queue.Empty:
            pass
    return ret

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print '** Starting brpop_task, now pass data to this task by calling:'
        print '** $ python %s <data>' % sys.argv[0]
        print '** in another shell'
        print brpop_task()
    else:
        r = redis.StrictRedis()
        print "sending data %s" % sys.argv[1]
        r.rpush("redis_brpop", sys.argv[1])
