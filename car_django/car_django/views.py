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
import pandas as pd
from numpy import asarray


def inicio(request):

    # cargo el archivo con el modelo para entrenar los datos
    regression_model = open(os.path.dirname(
        os.path.realpath(__file__)) + '/regression2.joblib', "rb")
    model = load(regression_model)

    # cargo el minmaxescaler guardado para escalar los neuvos datos
    MinMaxScaler_file = open(os.path.dirname(
        os.path.realpath(__file__)) + '/min_max_scaler.pkl', "rb")
    # min_max_scaler = MinMaxScaler()
    min_max_scaler = load(MinMaxScaler_file)

    # enc = OneHotEncoder(handle_unknown='ignore')

    if request.POST:
        # print(f"DATOS:{request.POST}")
        # fuelTypeId	id	km	makeId	modelId	provinceId	transmissionTypeId	year	cubicCapacity	doors	hp
        data_usuario = np.array([[2,51040978,41080,46,222.0,22,1.0,2018,1429.0,4.0,199.0]])

        data_transform = min_max_scaler.fit_transform(data_usuario)
        predict = model.predict(np.array(data_transform))

        # data = {"dct": predict}
        # # print(f"DATA:{data}")
        # # print(f"FIT:{min_max_scaler.fit(data_usuario)}")
        print(f"DATA TRANSFORM:{data_transform}")
        # # print(f"regression_model:{model}")
        print(f"min_max_scaler:{min_max_scaler}")
        return render(request, 'inicio.html', {"predict": predict, "model": model})

    return render(request, 'inicio.html')


# def resultado(request):
#     print(request.POST)
#     if request.POST:
#         data = {"dct":request.POST}
#         print(f"DATA:{data}")
#         return render(request,'resultado.html',data)
