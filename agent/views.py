from django.shortcuts import render
from django.http import JsonResponse
import requests


# Create your views here.
def index(request):
    return render(request, 'index.html')



