from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def generator(request):
    return render(request, "generator/home.html")
