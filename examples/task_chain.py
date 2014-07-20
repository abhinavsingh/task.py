import sys
from task import Chain


def chain_task(t):
    return t.prev + 1


if __name__ == '__main__':
    n = 5
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    chain = Chain(n, chain_task, 1)
    assert chain.run() == n + 1
