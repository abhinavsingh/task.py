from unittest import TestCase
from mock import patch
from task import controller
from task.controllers import wait_until_done, redis_brpop, redis_pubsub
from .mocks import MockStrictRedis


class TestControllers(TestCase):

    def test_wait_until_done(self):
        @controller(wait_until_done)
        def func(t):
            return "ok"

        self.assertEqual(func(), "ok")

    def test_wait_until_done_raises(self):
        @controller(wait_until_done)
        def func(t):
            raise Exception("ok")

        with self.assertRaises(Exception) as e:
            func()
            self.assertEqual(e.message, "ok")

    @patch('redis.StrictRedis', MockStrictRedis)
    def test_redis_brpop(self):
        @controller(redis_brpop, "test")
        def func(t):
            return t.recv()

        self.assertEqual(func(), "done")

    @patch('redis.StrictRedis', MockStrictRedis)
    def test_redis_pubsub(self):
        @controller(redis_pubsub, "test")
        def func(t):
            return t.recv()['data']

        self.assertEqual(func(), "done")
