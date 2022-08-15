from django.shortcuts import render
# from django.http import HttpResponse
import random

# Create your views here.

def generator(request):
    return render(request, "generator/home.html", {'password': 'gdfgfgfgfg'})

def passw(request):

    characters = list('qwertyuioplkjhgfdsazxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))


    length = int(request.GET.get('length',12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, "generator/pass.html", {'password': thepassword})
