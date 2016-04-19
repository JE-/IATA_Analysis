from flask import Flask,render_template,request,redirect
import os
import datetime

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def root():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return render_template('userinfo.html')

@app.route('/trying',methods=['GET','POST'])
def root():
    if request.method == 'GET':
        return render_template('trying.html')
    else:
        return render_template('userinfo.html')

if __name__ == "__main__":
    app.run(debug=True)
