import time
from unittest import TestCase
from task import controller


class TestDecorator(TestCase):

    def test_task(self):
        def ctrl(t, hello):
            t.send(hello)
            time.sleep(0.5)
            return t.result

        @controller(ctrl, "hello")
        def func(t):
            data = t.recv()
            assert data == "hello"
            return t.args[0]

        self.assertEqual(func("world"), "world")
