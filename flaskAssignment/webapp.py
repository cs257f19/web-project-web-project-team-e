import flask
from flask import render_template
from flask import request
import json
import sys

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Citizen of CS257.'

@app.route('/i', methods=['GET', 'POST'])
def form():
    return render_template('Create.html')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
