from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def initial(request):
    return HttpResponse('<h1>Vista initial</h1>')