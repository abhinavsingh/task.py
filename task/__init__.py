# -*- coding: utf-8 -*-
"""
    task
    ~~~~
    
    :copyright: (c) 2013 by Abhinav Singh.
    :license: BSD, see LICENSE for more details.
"""
VERSION = (0, 3)
__version__ = '.'.join(map(str, VERSION[0:2]))
__description__ = 'Run your task asynchronously and control/communicate with them.'
__author__ = 'Abhinav Singh'
__author_email__ = 'mailsforabhinav@gmail.com'
__homepage__ = 'https://github.com/abhinavsingh/task.py'
__license__ = 'BSD'

from .task import Task, controller
from .fsm import FSM
