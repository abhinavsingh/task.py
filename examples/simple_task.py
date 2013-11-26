import time
from task import Task

def simple_task(t):
    assert t.args[0] == "hello"
    assert t.kwargs['world'] == "world"
    time.sleep(1) # do some work
    return "done."

if __name__ == "__main__":
    t = Task(simple_task, "hello", world="world")
    t.start()
    
    while not t.done:
        time.sleep(0.5)
    
    print t.result
