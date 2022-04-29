from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'index.html', context)


def about(request):
    return HttpResponse("this is aboutpage")


def services(request):
    return HttpResponse("this is services page")


def contact(request):
    return HttpResponse("this is contact page")
