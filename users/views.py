from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('welcome to users')
# Create your views here.
