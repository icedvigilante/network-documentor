from flask import render_template, url_for, redirect
from iptrack import app

@app.route('/')
def hello_world():
    return 'Hello World!'