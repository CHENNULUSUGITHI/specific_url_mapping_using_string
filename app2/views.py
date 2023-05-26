from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h1>virat one of best batter</h1>')

def sky(request):
    return HttpResponse('<h1>sky one of best batter</h1>')    