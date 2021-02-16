from django.http import request
from django.shortcuts import render


def hello(request):
    return render(request, 'base.html')