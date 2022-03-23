from statistics import linear_regression
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from django.http import JsonResponse
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from joblib import load
from django.core.files import File
import os
import numpy as np
# import pandas as pd


def inicio(request):

    # cargo el archivo con el modelo para entrenar los datos,y descargar la ultima version
    linear_regression = open(
        os.path.dirname(os.path.realpath(__file__)) + "/model_linear_regression.pkl", "rb"
    )


    model_linear_regression = load(linear_regression)

    if request.POST:
        # fuelTypeId	km	makeId	modelId	price	provinceId	transmissionTypeId	year	cubicCapacity	doors	hp
        data_usuario = np.array(
            [[]]
        )

        predict = model_linear_regression.predict(data_usuario)

        return render(request, "resultado.html", {"predict": predict, "model": model_linear_regression})

    return render(request, "inicio.html")


def resultado(request):
    print(request.POST)
    if request.POST:
        data = {"dct":request.POST}
        print(f"DATA:{data}")
        return render(request,'resultado.html')
