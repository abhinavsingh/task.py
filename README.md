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
communicate with that unit of work. Example:

Lets define a `simple_task` that:

* Expects some arguments
* Does some work (sleep) until signaled to stop
* return "done." as final result

```
>>> def simple_task(t): # will receive a Task instance as first argument
...     assert t.args[0] == 'hello'
...     assert t.kwargs['world'] == 'world'
...     while not t.stopped():
...         time.sleep(0.1)
...     return 'done.'
```

Next, create a `Task` instance with `simple_task` as unit to work. 
Additionally specify arguments expected by our `sleep_task`:

```
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
```

Lets create a new `Task` instance, this time skipping the expected arguments:

```
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

Communicating with Task
=======================

`Task` provide a communication queue over which external threads can send data 
to the executing unit of work. Example:

Lets define a `sleep_task` which will receive amount of time to sleep 
over the communication queue:

```
>>> def sleep_task(t):
...     secs = t.recv() # recv API, default blocks until we have some data
...     time.sleep(int(secs))
...
>>> t3 = Task(sleep_task)
>>> t3.start()
>>>
>>> # our task is waiting
>>> t3.done
False
>>>
>>> # send 1 sec sleep time
>>> t3.send(1)
>>>
>>> # alright, done
>>> t3.done
True
```

Controllers
===========

- [wait_until_done](https://github.com/abhinavsingh/task.py/blob/master/examples/wait_until_done_task.py)
- [redis_brpop](https://github.com/abhinavsingh/task.py/blob/master/examples/redis_brpop_task.py)
- [redis_pubsub](https://github.com/abhinavsingh/task.py/blob/master/examples/redis_pubsub_task.py)

Task and Celery
===============

- [celery_task](https://github.com/abhinavsingh/task.py/blob/master/examples/celery_task.py)
