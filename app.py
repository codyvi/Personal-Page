from flask import Flask, render_template, request
import logging
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('test.html')