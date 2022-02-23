from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    name = 'ffbb'
    return render(request, 'elgenral/home.html')

