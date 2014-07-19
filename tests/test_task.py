import time
from unittest import TestCase
from mock import Mock
from task import Task


class TestTask(TestCase):

    def test_func_called(self):
        func = Mock()
        func.return_value = "ok"
        t = Task(func, "hello", hello="world")
        t.run()
        func.assert_called_once_with(t)
        self.assertEqual(t.result, "ok")

    def test_func_exc_caught(self):
        def func(t):
            raise Exception("ok")
        t = Task(func, "hello", hello="world")
        t.run()
        self.assertEqual(t.exception.message, "ok")

    def test_func_can_recv_data(self):
        def func(t):
            return t.queue.get()
        t = Task(func)
        t.send("ok")
        t.run()
        self.assertEqual(t.result, "ok")

    def test_func_is_stopped(self):
        def func(t):
            while not t.stopped():
                time.sleep(0.1)
            return "stopped"
        t = Task(func)
        t.start()
        time.sleep(0.1)
        t.stop()
        time.sleep(0.1)
        self.assertEqual(t.result, "stopped")
