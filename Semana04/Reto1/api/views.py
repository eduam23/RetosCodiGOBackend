from django.http.response import JsonResponse
from django.shortcuts import render

from .models import Usuario, Ciudad, Pais

# Create your views here.

def index(request):
    return JsonResponse({
        'mensaje': 'Bienvenido a mi API'
    })

def usuarios(request):
    lstUsuarios = Usuario.objects.all()
    print(lstUsuarios)
    data = []
    for usuario in lstUsuarios:
        data.append({
            'nombre': usuario.nombre,
            'dni': usuario.dni,
            'telefono': usuario.telefono,
            'email': usuario.email

        })
    return JsonResponse(data, safe=False)

def ciudad(request):
    lstCiudad= Ciudad.objects.all()
    print(lstCiudad)
    data = []
    for ciudad in lstCiudad:
        data.append({
            'nombre': ciudad.nombre
        })
    return JsonResponse(data, safe=False)

def pais(request):
    lstPaises = Pais.objects.all()
    print(lstPaises)
    data = []
    for pais in lstPaises:
        data.append({
            'nombre': pais.nombre
        })
    return JsonResponse(data, safe=False)