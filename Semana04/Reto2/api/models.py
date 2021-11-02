from django.db import models

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=20)
    edad = models.IntegerField()
    dueño = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)


class Vacunas(models.Model):
    nombre = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=20, decimal_places=3)
    caducidad = models.CharField(max_length=20)


