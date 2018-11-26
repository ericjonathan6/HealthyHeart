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
    col1 = request.form['col1']
    col2 = request.form['col2']
    col3 = request.form['col3']
    col4 = request.form['col4']
    col5 = request.form['col5']
    col6 = request.form['col6']
    col7 = request.form['col7']
    col8 = request.form['col8']
    col9 = request.form['col9']
    col10 = request.form['col10']
    col11 = request.form['col11']
    col12 = request.form['col12']
    col13 = request.form['col13']

    if (request.form['col1'] == ""):
        col1 = 54
    if (request.form['col2'] == "Please chooses"):
        col2 = 1
    if (request.form['col3'] == "Please chooses"):
        col3 = 4
    if (request.form['col4'] == ""):
        col4 = 130
    if (request.form['col5'] == ""):
        col5 = 225
    if (request.form['col6'] == "Please chooses"):
        col6 = 0
    if (request.form['col7'] == "Please chooses"):
        col7 = 0
    if (request.form['col8'] == ""):
        col8 = 140
    if (request.form['col9'] == "Please chooses"):
        col9 = 0
    if (request.form['col10'] == ""):
        col10 = 1
    if (request.form['col11'] == "Please chooses"):
        col11 = 2
    if (request.form['col12'] == "Please chooses"):
        col12 = 0
    if (request.form['col13'] == "Please chooses"):
        col13 = 3

    data = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13]
    float_data = [[float(x) for x in data]]
    result = model.predict(float_data)
    return str(result[0])
    

if __name__ == '__main__':
    app.run(debug=True)