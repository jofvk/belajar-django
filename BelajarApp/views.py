from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {
        'firstname': 'Jovanka',
        'lastname': 'Arya',
    }
    return render(request, 'index.html', context)
    # return HttpResponse("Hello world!")