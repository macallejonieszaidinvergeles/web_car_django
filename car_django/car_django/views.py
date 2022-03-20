from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def inicio(request):
    return render(request,'inicio.html')

def resultado(request):
    return render(request,'resultado.html')