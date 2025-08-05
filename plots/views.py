from django.shortcuts import render
from .models import Plot

def home(request):
    plots = Plot.objects.all()
    return render(request, 'home.html', {'plots': plots})

    
