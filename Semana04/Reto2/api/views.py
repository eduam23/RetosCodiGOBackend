from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Mascota, Vacunas
from .serializers import MascotasSerializer, VacunasSerializer

# Create your views here.

def index(request):
    return JsonResponse({
        'mensaje':'Bienvenido a mi API de Veterinaria',
        'opciones': 'Utiliza /mascota y /vacunas'
    })


@api_view(['GET','POST'])
def mascotas(request):
    if request.method == 'GET':
        lstMascotas = Mascota.objects.all()
        serMascotas = MascotasSerializer(lstMascotas, many=True)
        return Response(serMascotas.data)
    elif request.method == 'POST':
        serMascotas = MascotasSerializer(data = request.data)
        if serMascotas.is_valid():
            serMascotas.save()
            return Response(serMascotas.data)
        else:
            return Response(serMascotas.errors)


@api_view(['GET','PUT','DELETE'])
def mascotasedit(request,mascota_id):
    objMascota = Mascota.objects.get(id=mascota_id)
    if request.method == 'GET':
        serMascota = MascotasSerializer(objMascota)
        return Response(serMascota.data)
    elif request.method == 'PUT':
        serMascota = MascotasSerializer(objMascota,data = request.data)
        if serMascota.is_valid():
            serMascota.save()
            return Response(serMascota.data)
        else:
            return Response(serMascota.errors, status=400)
    elif request.method == 'DELETE':
        objMascota.delete()
        return Response(status=204) 


@api_view(['GET','POST'])
def vacunas(request):
    if request.method == 'GET':
        lstVacunas = Vacunas.objects.all()
        serVacunas = VacunasSerializer(lstVacunas,many=True)
        return Response(serVacunas.data)
    elif request.method == 'POST':
        serVacunas = VacunasSerializer(data = request.data)
        if serVacunas.is_valid():
            serVacunas.save()
            return Response(serVacunas.data)
        else:
            return Response(serVacunas.errors)


@api_view(['GET','PUT','DELETE'])
def vacunasedit(request,vacuna_id):
    objVacunas = Vacunas.objects.get(id=vacuna_id)
    if request.method == 'GET':
        serVacunas = VacunasSerializer(objVacunas)
        return Response(serVacunas.data)
    elif request.method == 'PUT':
        serVacuna = VacunasSerializer(objVacunas,data = request.data)
        if serVacuna.is_valid():
            serVacuna.save()
            return Response(serVacuna.data)
        else:
            return Response(serVacuna.errors, status=400)
    elif request.method == 'DELETE':
        objVacunas.delete()
        return Response(status=204)