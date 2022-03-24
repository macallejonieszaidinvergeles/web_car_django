# from statistics import linear_regression
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
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe
from django.template import Library


# import pandas as pd


def inicio(request):

    # cargo el archivo con el modelo para entrenar los datos,y descargar la ultima version
    linear_regression = open(
        os.path.dirname(os.path.realpath(__file__)) + "/model_linear_regression.pkl",
        "rb",
    )
    model_linear_regression = load(linear_regression)

    marcas_id = open(
        os.path.dirname(os.path.realpath(__file__)) + "/toda_info.json",
        "rb",
    )

    with marcas_id as file:
        data = json.load(file)
        data_json = json.dumps(data)

    if request.POST:
        # fuelTypeId	km	makeId	modelId	transmissionTypeId	year	cubicCapacity	doors	hp
        fuelTypeId = request.POST['fuelTypeId']

        data_usuario = np.array([[fuelTypeId, 41080, 46, 322.0, 2.0, 2015, 1329.0, 5.0, 99.0]])

        predict = model_linear_regression.predict(data_usuario)

        return render(
            request,
            "resultado.html",
            {"predict": predict, "model": model_linear_regression},
        )

    print("data json",data)
    return render(request, "inicio.html",{"todo_info":data_json})







def resultado(request):
    print(request.POST)
    if request.POST:
        data = {"dct": request.POST}
        print(f"DATA:{data}")
        return render(request, "resultado.html")
