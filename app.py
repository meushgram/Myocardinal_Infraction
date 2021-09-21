import pickle
from io import TextIOWrapper
import pandas as pd
from sklearn.model_selection  import  train_test_split
import csv,os
import numpy as np
#import pandas as pd
from flask import Flask, render_template, request, url_for
app = Flask(__name__)
l = pickle.load(open('testpred', 'rb'))
@app.route('/')
def hello_world():
    # newdata = pd.Series([200, 300])
    # data_pred = pd.DataFrame(newdata, columns=['YearsExperience'])
    # model = pickle.load(open('model-RF', 'rb'))
    # print(model.predict(l))
    # print(type(model.predict(l)))
    # print(l.shape)
    # print(l.dtype)
    # return f"<html>{model.predict(l)}</html>"
    # print(model.predict(data_pred))
    return render_template('test.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    model = pickle.load(open('model-RF', 'rb'))
    uploaded_file = request.files['file']
    csv_file = TextIOWrapper(uploaded_file, encoding='utf-8-sig')
    csv_reader = csv.reader(csv_file, delimiter=',')
    df = pd.DataFrame(csv_reader)
    print(df)
    data = np.array(df)
    print(data)
    return f"<h1>{model.predict(data)}</h1>"
    # if uploaded_file.filename != '':
    #     uploaded_file.save(uploaded_file.filename)
    # #return redirect(url_for('index'))

# @app.route('/upload',methods=['POST','GET'])
# def upload_file():
#     file = request.files['file']
#     data = pd.read_csv(file)
#     print(data)
#     return data

@app.route('/predict',methods=['POST'])
def hello_world1():
    model = pickle.load(open('model-SLR', 'rb'))
    #print(request.form.get('input'))
    newdata = pd.Series(int(request.form.get('input')))
    data_pred = pd.DataFrame(newdata, columns=['YearsExperience'])
    #print(model.predict(data_pred)[0])
    print(model.predict(l))
    print(type(model.predict(l)))
    return f"<html>{model.predict(l)}</html>"

# main driver function

#print(l)
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)