#import time
#import random
from task import Pool

rcvd = list()


def simple_task(t):
    '''Our simple little task.'''
    #s = random.random()
    #time.sleep(s)
    return t.args[0]


def inputs(size):
    '''Yields `size` (args, kwargs) for our `simple_task`.'''
    while True:
        if size <= 0:
            break
        yield (size,), {}
        size -= 1


def receiver(t, *args, **kwargs):
    '''Handle done tasks.'''
    global rcvd
    assert t.args[0] == args[0]
    rcvd.append(args[0])

if __name__ == '__main__':
    size = 1000
    parallel = 200
    pool = Pool(size, parallel, simple_task, inputs(size), receiver)
    pool.run()

    rcvd.sort()
    assert rcvd == range(1, size+1)
