from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rohit(request):
    return HttpResponse('<h1>Rohit one of the hitman</h1>')

def dhoni(request):
    return HttpResponse('<h1>dhoni is one of best cool captain</h1>')