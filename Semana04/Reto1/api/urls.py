
from django.urls import path

from . import views

urlpatterns = [
  path('',views.index),
  path('usuarios',views.usuario),
  path('ciudad',views.ciudad),
  path('pais',views.pais)
]