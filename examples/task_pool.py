import sys
from task import Pool

rcvd = list()


def simple_task(t):
    '''Our simple little task.'''
    return t.args[0]


def inputs(size):
    '''Yields `size` (args, kwargs) for our `simple_task`.'''
    while True:
        if size <= 0:
            break
        yield (size,), {}
        size -= 1


def receiver(t):
    '''Handle done tasks.'''
    global rcvd
    rcvd.append(t.result)

if __name__ == '__main__':
    size = 1000
    if len(sys.argv) >= 2:
        size = int(sys.argv[1])

    parallel = 100
    if len(sys.argv) >= 3:
        parallel = int(sys.argv[2])

    pool = Pool(size, parallel, simple_task, inputs(size), receiver)
    pool.run()

    rcvd.sort()
    assert rcvd == range(1, size+1)
