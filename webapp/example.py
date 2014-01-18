import time
from socketio.namespace import BaseNamespace

class ExampleNamespace(BaseNamespace):
    def on_challenge(self, msg):
        print self, "challenge", msg
        self.emit("response", msg)
