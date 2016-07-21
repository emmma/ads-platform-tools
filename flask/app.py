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


@app.route('/callback', methods=['GET'])
def oauth():
    name = None
    name = server.oauth(request)
    return render_template('results.html', name=name)

# TODO Create separate route so code and state is not displayed in URL

if __name__ == '__main__':
    main()
