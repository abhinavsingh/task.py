import time
from task import Task


def simple_task(t):
    assert t.args[0] == "hello"
    assert t.kwargs['world'] == "world"
    while not t.stopped():
        # do some work until stopped externally
        time.sleep(0.1)
    return "done."

if __name__ == "__main__":
    t = Task(simple_task, "hello", world="world")
    t.start()

    # after 1 second signal our task to stop
    time.sleep(1)
    t.stop()

    print t.result
