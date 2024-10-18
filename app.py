from flask import Flask, redirect, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/")
def fun1():
    return render_template("info.html")

@app.route("/predict", methods = ["post"])
def fun2():
    age = int(request.form['age'])
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = request.form['smoker']
    if smoker=='yes':
        smoker=1
    else:
        smoker=0
    sex = request.form['sex']
    if sex=='female':
        sex=1
    else:
        sex=0
    region = request.form['region']
    if region=='Southeast':
        region=0
    elif region=='Southwest':
        region=1
    elif region=='Northwest':
        region=2
    elif region=='Northeast':
        region=3
    pred_info = [age,bmi,children,smoker,sex,region]

    print(pred_info)

    mymodel = pickle.load(open('model_HIPAP.pkl',"rb"))
    amt = round(mymodel.predict([pred_info])[0],2)
    #return "<h1>your predicted salary is {} </h1>".format(nm,sal)
    return render_template("result.html", amount = amt)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8080)