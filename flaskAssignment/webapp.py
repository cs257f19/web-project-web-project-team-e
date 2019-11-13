from datasource import*
import flask
from flask import render_template
from flask import request
import json
import sys


app = flask.Flask(__name__)

'''
Renders the homepage when the user connects to http://perlman.mathcs.carleton.edu:5222/
'''
@app.route('/')
def renderHomepage():
    return render_template('Homepage.html')

'''
Renders the create page when the user directs to http://perlman.mathcs.carleton.edu:5222/create/
'''
@app.route('/create/')
def renderCreatePage():
    return render_template('Create.html')

'''
Renders the analyze page when the user directs to http://perlman.mathcs.carleton.edu:5222/create/
**THIS FUNCTION IS NOT RELEVANT TO THE SPECIFIC USER QUERY FOR THIS DELIVERABLE**
**DO NOT GRADE**
'''
@app.route('/analyze/')
def renderAnalyzePage():
    return render_template('Analyze.html')

'''
Renders the results page when the user is directed to http://perlman.mathcs.carleton.edu:5222/results/
Assigns variables 'category', 'currency', and 'goal' to their corresponding form submissions using 'request' from flask
Creates a datasource object and calculates the probabilityOfSuccess based of the given variables
'Results.html' is rendered using the form submissions and the probabilityOfSuccess variable
'''
@app.route('/results/', methods=['GET', 'POST'])
def displayProbabilityOfSuccess():
    category = request.form['category']
    currency = request.form['currency']
    goal = request.form['goal']
    ds = DataSource()
    #note: connection is not passed because this function can be ran independently of the database
    probabilityOfSuccess = ds.calculateProbabilityOfSuccess(category, currency, goal)
    return render_template('Results.html', category = category, currency = currency, goal = goal, probabilityOfSuccess = probabilityOfSuccess)



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
