from django.shortcuts import render
from django.http import HttpResponse


def hello_django_bbs(request):
    html = '<h1>Hello, Django BBS!</h1>'
    return HttpResponse(html)
