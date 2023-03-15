from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return render(request, 'post/hello.html')


def greet(request):
    return HttpResponse("welcome to django")


def rules(request):
    return HttpResponse("No rules here")


def page(request):
    return render(request, 'post/page.html')

