from flask import Flask, render_template, request
import logging
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('test.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        return render_template('about.html')