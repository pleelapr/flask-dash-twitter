from werkzeug.middleware.dispatcher import DispatcherMiddleware
import flask
from dash_app import dash_1
from werkzeug.serving import run_simple
from flask import render_template

server = flask.Flask(__name__)


@server.route('/')
def home():
    return render_template('index.html')


dash_1.create_dashboard(server)


run_simple('localhost', 8080, server, use_reloader=True, use_debugger=True)
