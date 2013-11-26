import sys
import redis

from task import controller
from task.controllers import redis_pubsub

@controller(redis_pubsub, 'redis_pubsub')
def pubsub_task(t):
    ret = None
    while True:
        data = t.queue.get()
        ret = data['data']
        break
    return ret

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print '** Starting pubsub_task, now pass data to this task by calling:'
        print '** $ python %s <data>' % sys.argv[0]
        print pubsub_task()
    else:
        r = redis.StrictRedis()
        print "sending data %s" % sys.argv[1]
        r.publish("redis_pubsub", sys.argv[1])
