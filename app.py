from flask import Flask,render_template,request,redirect
import os
import datetime

from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
import numpy as np

#from vectorizer import vect

### Preparing the Classifier
cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir,
                  'pickled_objects',
                  'classifier.pkl'), 'rb'))
#db = os.path.join(cur_dir, 'reviews.sqlite')
#
# def classify(document):
#     label = {0: 'negative', 1: 'positive'}
#     X = vect.transform([document])
#     y = clf.predict(X)[0]
#     proba = np.max(clf.predict_proba(X))
#     return label[y], proba
#
# def train(document, y):
#     X = vect.transform([document])
#     clf.partial_fit(X, [y])
#
# def sqlite_entry(path, document, y):
#     conn = sqlite3.connect(path)
#     c = conn.cursor()
#     c.execute("INSERT INTO review_db (review, sentiment, date)"\
#     " VALUES (?, ?, DATETIME('now'))", (document, y))
#     conn.commit()
#     conn.close()

#### Flask

class ReviewForm(Form):
    moviereview = TextAreaField('',
                                [validators.DataRequired(),
                                validators.length(min=15)])
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def root():
    if request.method == 'GET':
        form = ReviewForm(request.form)
        return render_template('index.html', form=form)
    else:
        return render_template('userinfo.html')

if __name__ == "__main__":
    app.run(debug=True)
