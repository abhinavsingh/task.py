# -*- coding: utf-8 -*-
"""
    task.task
    ~~~~~~~~~

    :copyright: (c) 2014 by Abhinav Singh.
    :license: BSD, see LICENSE for more details.
"""
from threading import Thread, Event
from Queue import Queue
from functools import wraps
import logging

logger = logging.getLogger('task')


class Task(Thread):
    '''Run your task asynchronously and control/communicate with them.

    Initialize a `Task` instance by passing the your callable to execute,
    optionally with arguments to pass to your callable. Example:

    >>> def sleep_task(t):
    ...     assert t.args == ('hello',)
    ...     assert t.kwargs == dict(world='world')
    ...     return 'done'

    >>> t = Task(sleep_task, 'hello', world='world')
    >>> t.start()

    >>> # let the task finish
    >>> import time
    >>> while not t.done:
    ...     time.sleep(0.1)

    >>> t.result
        'done'
    >>> t.exception
        None

    If an exception occurs during the execution of your callable, exc instance will be available as `t.exception`. Example:

    >>> def exc(t):
    ...     raise Exception('msg')

    >>> t = Task(exc)
    ... t.start()
    ...
    ... t.exception
    ... "Exception('msg',)"
    ...
    ... type(t.exception)
    ... "<type 'exceptions.Exception'>"

    '''

    def __init__(self, func, *args, **kwargs):
        super(Task, self).__init__()
        self.daemon = True

        self.func = func
        self.args = args
        self.kwargs = kwargs

        self.result = None
        self.exception = None
        self.done = False

        self.event = Event()
        self.queue = Queue()

    def run(self):
        try:
            self.result = self.func(self)
        except Exception, e:
            self.exception = e
        finally:
            self.done = True
            if self.exception:
                logger.exception(e)

    def stop(self, join=True):
        '''Set flag to signal stop to the underlying function.'''
        self.event.set()
        if join:
            self.join()

    def stopped(self):
        return self.event.is_set()

    def recv(self, block=True, timeout=None):
        '''Used by running function to receive data queued from external threads.'''
        return self.queue.get(block, timeout)

    def send(self, data, block=True, timeout=None):
        '''Queue up data for the running function.'''
        self.queue.put(data, block, timeout)


def controller(ctrl, *args1, **kwargs1):
    '''Controllers abstract out the pattern for communication with your `Task` instance.
    Accepts controller callable and arguments for the controller.

    Use `controller` decorator to apply controller pattern to your `Task` callable. Example:

    >>> from task.controllers import wait_until_done
    >>> @controller(wait_until_done)
    ... def sleep_task(t, delay=1):
    ...     import time
    ...     time.sleep(delay)
    ...     return 'done'
    ...
    >>> print sleep_task(delay=0.1)
        'done'

    While using controller if underlying an exception occurs during execution of your callable,
    that exception will be raised in the main process. Example:

    >>> @controller(wait_until_done)
    ... def exc(t, delay=1):
    ...     raise Exception(delay)
    ...
    >>> print exc(delay=0.1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "task/task.py", line 102, in wrapper
        Use `controller` decorator to apply controller pattern to your `Task` callable. Example:
      File "task/controllers/base.py", line 24, in wrapper
        raise t.exception
    Exception: 1

    '''

    def outside(func):

        @wraps(func)
        def wrapper(*args2, **kwargs2):
            '''Callable args and kwargs.'''
            t = Task(func, *args2, **kwargs2)

            try:
                t.start()
                ctrl(t, *args1, **kwargs1)
            except:
                raise
            finally:
                t.stop()

            if t.exception:
                raise t.exception
            return t.result

        return wrapper

    return outside


class Pool(object):

    def __init__(self, size, parallel, mapfunc, mapargs, reducer):
        self.size = size
        self.parallel = parallel

        # function to map and args iter for each function
        self.mapfunc = mapfunc
        self.mapargs = mapargs
        assert len(self.mapargs) == size, 'Map args must be size of pool %s' % size

        # function that receives `Task` of completed mapfunc tasks
        # to maintain pool parallelism new mapfunc task will be started immediately if required
        self.reducer = reducer

    def run(self):
        pass
