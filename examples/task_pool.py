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


def receiver(t, *args, **kwargs):
    print args[0]
    assert t.args[0] == args[0]


def simple_task(t, idx):
    return idx

if __name__ == '__main__':
    size = 100
    parallel = 22
    pool = Pool(size, parallel, simple_task, Inputs(size), receiver)
    pool.run()
