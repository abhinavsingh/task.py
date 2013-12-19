from unittest import TestCase
from task import FSM

def init(t):
    t.kwargs['ctx'][t.kwargs['state']] = 'done'
    return 'nxt', t.kwargs['ctx']

def nxt(t):
    t.kwargs['ctx'][t.kwargs['state']] = 'done'
    return 'last', t.kwargs['ctx']

def last(t):
    t.kwargs['ctx'][t.kwargs['state']] = 'done'
    return t.kwargs['ctx']

class TestFSM(TestCase):
    
    def test_fsm(self):
        fsm = FSM({
            'init': 'tests.test_fsm.init',
            'nxt': 'tests.test_fsm.nxt',
            'last': 'tests.test_fsm.last',
        })
        fsm.run()
        self.assertEqual(fsm.state, 'last')
        self.assertDictEqual(fsm.ctx, {'init':'done', 'nxt':'done', 'last':'done'})
