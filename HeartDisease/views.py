from django.shortcuts import render
import numpy as np

def home(request):
    return render(request, 'home.html')


def predict(request):
    return render(request, 'predict.html')

def results(request):
    from sklearn.ensemble import RandomForestClassifier
    import joblib

    model = joblib.load('D:\django\HeartDisease\cardio_deployment.joblib')

    v1 = int(request.GET['age'])
    v2 = int(request.GET['sex'])
    v4 = int(request.GET['atRestBps'])
    v5 = int(request.GET['cholestrol'])
    v6 = int(request.GET['maxHeartRate'])
    v8 = int(request.GET['oldpeak'])
    v3 = int(request.GET['chestPainType'])
    v7 = int(request.GET['excerciseInducedangina'])
    v9 = int(request.GET['slope'])

    pred = model.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9]])


    if pred == 1:
        result1 = "You have been diagnosed with heart disease"

    else:
        result1 = "Congratulations, you do not have heart disease"

    return render(request,'prediction.html', {"result2":result1})

def prediction(request):
    return render(request, 'prediction.html')
