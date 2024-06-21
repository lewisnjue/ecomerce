from django.urls import path 
from django.http import HttpResponseNotFound
from django.shortcuts import render


def handler404(request, exception):
    return render(request, '404.html', status=404)