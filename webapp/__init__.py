import logging
from socketio import socketio_manage
from gevent import monkey
from flask import Flask, Response, request, render_template
from example import ExampleNamespace



monkey.patch_all()

logging.basicConfig()

# Flask wsgi application
app = Flask(__name__)
app.debug = True

# Flask routes
@app.route("/")
def root():
    return render_template("example.html")

@app.route("/socket.io/<path:remaining>")
def socketio(remaining):
    try:
        socketio_manage(request.environ, {"/example": ExampleNamespace}, request)
    except:
        app.logger.error("Exception while handling socketio connection",
                         exc_info=True)
    return Response()



