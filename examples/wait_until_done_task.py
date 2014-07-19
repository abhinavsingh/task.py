import time

from task import controller
from task.controllers import wait_until_done


@controller(wait_until_done)
def sleep_task(t, delay=1):
    # do some work
    time.sleep(delay)
    return "done."

if __name__ == '__main__':
    print sleep_task(delay=2)
