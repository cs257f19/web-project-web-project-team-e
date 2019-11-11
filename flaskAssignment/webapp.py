from flask import Flask, render_template, request
import json
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

if __name__ == "__main__":
    app.run()
