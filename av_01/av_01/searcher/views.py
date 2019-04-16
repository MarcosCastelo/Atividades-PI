from django.shortcuts import render
import requests
import bs4

# Create your views here.
def index(request):
    return render(request, 'index.html')


def search(request):
    pass
