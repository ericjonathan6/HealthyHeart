#!flask/bin/python
from flask import Flask, request, render_template, jsonify
from sklearn.externals import joblib
from flask import make_response
import pandas as pd
import json
import numpy as np
import pickle

model = pickle.load(open('Model.sav', 'rb'))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def predict_data():
    data = [request.form['col1'], request.form['col2'], request.form['col3'], request.form['col4'], request.form['col5'],
           request.form['col6'], request.form['col7'], request.form['col8'], request.form['col9'], request.form['col10'],
           request.form['col11'], request.form['col12'], request.form['col13']]
    float_data = [[float(x) for x in data]]
    result = model.predict(float_data)
    return str(result[0])

if __name__ == '__main__':
    app.run(debug=True)