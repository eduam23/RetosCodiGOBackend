from django.db import models

# Create your models here.

class Usuario(models.Model):
  nombre = models.CharField(max_length=200)
  dni = models.CharField(max_length=8)
  telefono = models.CharField(max_length=20)
  email = models.CharField(max_length=20)

  def __str__(self):
        return self.nombre

class Ciudad(models.Model):
  nombre = models.CharField(max_length=200)

  def __str__(self):
        return self.nombre

class Pais(models.Model):
  nombre = models.CharField(max_length=20)

  def __str__(self):
        return self.nombre