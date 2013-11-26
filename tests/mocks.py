class MockRedisPubSub(object):
    
    def subscribe(self, channel):
        if channel == "test":
            self.subscribed = True
    
    def listen(self):
        if self.subscribed:
            yield {"type":"message", "data":"done"}
    
    def unsubscribe(self, channel):
        self.subscribed = False

class MockStrictRedis(object):
    
    def brpop(self, key):
        if key == "test":
            return "done"
    
    def pubsub(self):
        return MockRedisPubSub()

class ToggleAfterNTimes(object):

    def __init__(self, n=1, initial=False):
        self.n = n
        self.i = 0
        self.initial = initial

    def __call__(self):
        if self.i < self.n:
            self.i += 1
            return bool(self.initial)
        return bool(not self.initial)
