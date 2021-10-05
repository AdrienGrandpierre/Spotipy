from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import path


def hello(req):
    return HttpResponse("Bipbop")
