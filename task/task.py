# -*- coding: utf-8 -*-
"""
    task.task
    ~~~~~~~~~
    
    :copyright: (c) 2013 by Abhinav Singh.
    :license: BSD, see LICENSE for more details.
"""
from threading import Thread, Event
from Queue import Queue
from functools import wraps

class Task(Thread):
    
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
    
    def stop(self, join=True):
        self.event.set()
        if join:
            self.join()
    
    def stopped(self):
        return self.event.is_set()
    
    def send(self, data, block=True, timeout=None):
        self.queue.put(data, block, timeout)

def controller(ctrl, *args1, **kwargs1):
    def outside(func):
        @wraps(func)
        def wrapper(*args2, **kwargs2):
            t = Task(func, *args2, **kwargs2)
            t.start()
            return ctrl(t, *args1, **kwargs1)
        return wrapper
    return outside
