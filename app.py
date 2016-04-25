from flask import Flask,render_template,request,redirect
from wtforms import Form, TextAreaField, validators
import os
import datetime
import sklearn
import pickle
import sqlite3
import numpy as np

#### Flask
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def root():
    if request.method == 'GET':
        return render_template('index.html', form=form)
    else:
        return render_template('userinfo.html')

if __name__ == "__main__":
    app.run(debug=True)
