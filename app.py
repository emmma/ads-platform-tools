from flask import Flask
from flask import request
from flask import render_template

import client
import server

app = Flask(__name__)


@app.route('/')
def index():
    client.prompt()
    return render_template('index.html')

@app.route('/oauth', methods=['GET'])
def oauth():
    server.oauth(request)
    return render_template('results.html')

if __name__ == '__main__':
    main()