'''
    $ cd examples
    $ PYTHONPATH=.. celery -A celery_task worker --loglevel=debug
'''
import sys
import time
import redis
from celery import Celery
from task import controller
from task.controllers import redis_brpop

celery = Celery('celery_task', broker='redis://', backend='redis://')


@celery.task
@controller(redis_brpop, "celery_job_task")
def job(t):
    data = t.queue.get()
    return data[1]

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print '** Starting celery job, now pass data to this task by calling:'
        print '** $ python %s <data>' % sys.argv[0]
        r = job.delay()

        while not r.ready():
            time.sleep(1)

        print r.get()
    else:
        r = redis.StrictRedis()
        print "sending data %s" % sys.argv[1]
        r.rpush("celery_job_task", sys.argv[1])
