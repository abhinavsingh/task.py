#import time
#import random
from task import Pool


class Inputs(object):

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.n == 0:
            raise StopIteration
        m = self.n
        self.n -= 1
        return (m,), {}


class Receiver(object):

    def __init__(self):
        self.rcvd = list()

    def __call__(self, t, *args, **kwargs):
        assert t.args[0] == args[0]
        self.rcvd.append(args[0])


def simple_task(t):
    #s = random.random()
    #time.sleep(s)
    return t.args[0]

if __name__ == '__main__':
    size = 10000
    parallel = 1000
    pool = Pool(size, parallel, simple_task, Inputs(size), Receiver())
    pool.run()
    pool.receiver.rcvd.sort()
    assert pool.receiver.rcvd == range(1, size+1)
