import sys
import redis

from task import controller
from task.controllers import redis_brpop

@controller(redis_brpop, 'redis_brpop')
def brpop_task(t):
    ret = None
    while True:
        data = t.queue.get()
        ret = data[1]
        break
    return ret

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print '** Starting brpop_task, now pass data to this task by calling:'
        print '** $ python %s <data>' % sys.argv[0]
        print brpop_task()
    else:
        r = redis.StrictRedis()
        print "sending data %s" % sys.argv[1]
        r.rpush("redis_brpop", sys.argv[1])
