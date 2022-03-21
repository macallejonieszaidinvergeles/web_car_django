from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from django.http import JsonResponse


def inicio(request):

    # print(request.POST)

    if request.POST:
        data = {"dct":request.POST}
        print(f"DATA:{data}")
        return render(request,'inicio.html',data)

    return render(request,'inicio.html')


# def resultado(request):
#     print(request.POST)
#     if request.POST:
#         data = {"dct":request.POST}
#         print(f"DATA:{data}")
#         return render(request,'resultado.html',data)