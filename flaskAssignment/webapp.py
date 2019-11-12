import flask
from flask import render_template
from flask import request
import json
import sys
import datasourceImpTest

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return 'Test, Citizen of CS257.'

@app.route('/create/')
def renderTest():
    return render_template('Create.html')

@app.route('/results', methods=['GET', 'POST'])
def form():
    render_template('Results.html', category = request.form['category'], currency = request.form['currency'], goal = request.form['goal'])
    ds = Datasource()
    conncetion = ds.connect()
    return ds.calculateProbabilityOfSucesss(category, currency, goal)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
