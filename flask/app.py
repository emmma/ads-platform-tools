from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

import client
import server

app = Flask(__name__)


@app.route('/')
def index():
    client.prompt()
    return render_template('index.html')


@app.route('/callback', methods=['GET'])
def oauth(name=None):
    name = server.oauth(request)
    return redirect(url_for('hello', name=name))


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name):
    return render_template('results.html', name=name)

if __name__ == '__main__':
    app.debug = True
    app.run()
