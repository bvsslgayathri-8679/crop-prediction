from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import request
# Create your views here.

from django.http import HttpResponse
def home(request):
    # return HttpResponse("hi")
    return render(request,'homepage.html')


def predict(request):
    if request.method=='POST':
        N=float(request.POST['N'])
        K=float(request.POST['K'])
        P=float(request.POST['P'])
        temp=float(request.POST['temp'])
        humidity=float(request.POST['humidity'])
        PH=float(request.POST['PH'])
        rainfall=float(request.POST['rainfall'])
        import pandas as pd
        url='https://raw.githubusercontent.com/bvsslgayathri-8679/crop_prediction/main/Crop_recommendation.csv'
        df=pd.read_csv(url)

        import seaborn as sb
        from matplotlib import pyplot as plt
        from sklearn.model_selection import train_test_split 
        from sklearn.preprocessing import LabelEncoder

        lab_enc=LabelEncoder()

        df['label']=lab_enc.fit_transform(df['label'])
        crop_category = {index : label for index, label in enumerate(lab_enc.classes_)}
        

        X = df.drop('label', axis = 1)
        y = df['label']

        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8)


        from sklearn.neighbors import KNeighborsClassifier

        knn=KNeighborsClassifier()

        knn.fit(X_train,y_train)
        import numpy as np
        inp=[[N,P,K,temp,humidity,PH,rainfall]]
        # inp.reshape(-1, 1)
        predicted_values = knn.predict(inp)
        print(predicted_values)  

        return render(request,"homepage.html",{'ans':crop_category[predicted_values[0]]})   


