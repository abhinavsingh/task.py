# -*- coding: utf-8 -*-
"""
    task.fsm
    ~~~~~~~~
    
    :copyright: (c) 2013 by Abhinav Singh.
    :license: BSD, see LICENSE for more details.
"""

from .task import controller
from .utils import import_path
from .controllers import wait_until_done

class FSM(object):
    '''Run tasks that define your state machine.
    
    Accepts a dictionary where keys specify the 
    state name and value is a dotted path to the 
    function responsible for executing the state task.
    
    All state function must accept two arguments,
    first current state name and second a context variable. 
    
    State function should return the next state name to transition
    and updated context variable which is then passed onto next 
    state function.
    
    Optionally, state function can only return the update context
    variable if it wish to terminate the state machine. Returning
    `None` as next state name also results in similar behaviour.
    
    Finally, FSM returns final state name and context variable.
    
    Optionally, accepts a custom task controller. If not provided
    `wait_until_done` controller is used to wrap each state
    function.
    
    Optionally, accepts an initial context variable.
    '''
    
    def __init__(self, states, ctrl=None, ctx=None):
        self.state = 'init' # initial state
        self.states = states
        self.ctrl = ctrl if ctrl else wait_until_done
        self.ctx = ctx if ctx else dict()
    
    def run(self):
        while self.state:
            path = self.states[self.state]
            func = import_path(path)
            
            t = controller(self.ctrl)(func)
            result = t(state=self.state, ctx=self.ctx)
            
            if type(result) is not tuple:
                break
            
            next_state, self.ctx = result
            if next_state == None:
                break
            
            self.state = next_state
