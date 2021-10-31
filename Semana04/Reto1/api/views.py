from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return JsonResponse({
        'mensaje': 'Bienvenido a mi API'
    })