task.py
=======

Run your task asynchronously in the background and control/communicate with them.

![Build Status](https://api.travis-ci.org/abhinavsingh/task.py.png)

Install
=======

`pip install task.py`

Usage
=====

Basic use case of `task.py` is to run some unit of work asynchronously 
(in a separate thread or process) while being able to control and 
communicate with that unit of work.

```
$ python
>>> import time
>>> from task import Task
>>> 
>>> # Define a simple task that:
>>> # 1) expects two arguments
>>> # 2) does some work until stopped
>>> # 3) return 'done.' as final result
>>> def simple_task(t): # will receive a Task instance as first argument
...     assert t.args[0] == 'hello'
...     assert t.kwargs['world'] == 'world'
...     while not t.stopped():
...         time.sleep(0.1)
...     return 'done.'
... 
>>> # Create Task instance with sleep_task as unit to work,
>>> # additionally specify arguments available to the sleep_task
>>> t1 = Task(simple_task, 'hello', world='world')
>>> 
>>> # start our task asynchronously
>>> t1.start()
>>> 
>>> # after 1 second signal our task to stop
>>> time.sleep(1)
>>> t1.stop()
>>> 
>>> t1.done
True
>>> 
>>> t1.result
'done.'
>>> 
>>> t1.exception == None
True
>>> 
>>> # Create a new Task instance, this time skipping the arguments
>>> # that sleep_task is expecting
>>> t2 = Task(simple_task)
>>> 
>>> # start our task asynchronously
>>> t2.start()
>>> 
>>> t2.done
True
>>> 
>>> # No result found
>>> t2.result == None
True
>>> 
>>> # our task raised an exception
>>> t2.exception
IndexError('tuple index out of range',)
```
